from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtGui import QPixmap

from compiled_ui.main_window import Ui_MainWindow
from buddy_builder import BuddyBuilder
from mini_buddy import MiniBuddy

from serialization import load_buddy
from os.path import basename
from pathlib import Path


class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Mini Buddy:
        self.mini_buddy = MiniBuddy(self)
        self.mini_buddy.installEventFilter(self)

        # Buddy Builder:
        self.buddy_builder = BuddyBuilder(self)

        # Dragging:
        self.dragging_window = False
        self.offset = QPoint()
        self.loaded = False

        self.initialize()
        self.bind_buttons()

    # Initialize:
    def initialize(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.statusBar()

        self.load_buddy()

        # Name:
        if self.buddy_name.text() == '':
            self.buddy_name.setText('Buddy')

    def bind_buttons(self):
        # Minimize button:
        self.minimize_button.setIcon(QPixmap('res/minus.png'))
        self.minimize_button.clicked.connect(self.showMinimized)

        # Settings button:
        self.settings_button.setIcon(QPixmap('res/setting.png'))
        # self.settings_button.clicked.connect(self.buddy_builder_method)

        # Import button:
        self.import_button.setIcon(QPixmap('res/import.png'))
        self.import_button.clicked.connect(self.new_buddy_action)

        # Close button:
        self.close_button.setIcon(QPixmap('res/close.png'))
        self.close_button.clicked.connect(self.close)

        # Action buttons::
        self.feed_button.clicked.connect(self.feed_action)
        self.play_button.clicked.connect(self.play_action)
        self.sleep_button.clicked.connect(self.sleep_action)

    # Events:
    def mouseDoubleClickEvent(self, event):
        child = self.childAt(event.position().toPoint())
        if child:
            if child.objectName() == 'buddy_display':
                if event.button() == Qt.LeftButton:
                    if self.loaded:
                        self.show_mini_buddy()

    def mousePressEvent(self, event):
        self.offset = event.globalPosition().toPoint()

        if event.button() == Qt.LeftButton:
            self.dragging_window = True

    def mouseReleaseEvent(self, event):
        self.dragging_window = False

    def mouseMoveEvent(self, event):
        if self.dragging_window:
            delta = QPoint(event.globalPosition().toPoint() - self.offset)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.offset = event.globalPosition().toPoint()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonDblClick and event.button() == Qt.LeftButton:
            self.hide_mini_buddy()

        return super().eventFilter(obj, event)

    # Actions:
    def feed_action(self):
        self.change_output('Nom nom nom')

    def play_action(self):
        self.change_output('Yay! such playing')

    def sleep_action(self):
        self.change_output('*snore')

    # Mini Buddy Methods:
    def show_mini_buddy(self):
        self.hide()
        self.mini_buddy.show()

    def hide_mini_buddy(self):
        self.mini_buddy.hide()
        self.show()

    # Buddy Builder:
    def new_buddy_action(self):
        dialog = QMessageBox()
        dialog.setText('Would you like to create or import a Buddy?')
        dialog.setWindowTitle('Buddy')

        dialog.addButton(dialog.Close)
        dialog.addButton('Create', dialog.ActionRole)
        dialog.addButton('Import', dialog.ActionRole)

        button_option = dialog.exec()

        if button_option == 0:
            dialog.close()
            self.import_buddy()

        elif button_option == 1:
            dialog.close()
            self.buddy_builder_method()

    def buddy_builder_method(self):
        self.buddy_builder.exec()

        self.load_buddy(self.buddy_builder.file_save)

    def import_buddy(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                              str(Path().resolve()), 'Image files (*.buddy)')

        self.load_buddy(basename(path))

    # Helper:
    def change_output(self, text):
        self.buddy_output.setText('<center>' + text + '</center>')

    def load_buddy(self, path=None):
        buddy_file = load_buddy(path)
        if buddy_file:
            # Profile Picture:
            self.buddy_display.set_buddy(buddy_file.get('profile_picture'))

            # Buddy Picture:
            self.mini_buddy.mini_buddy_display.set_buddy(buddy_file.get('mini_buddy_picture'))

            # Name:
            self.buddy_name.setText(buddy_file.get('name'))
            self.change_output('Hello, my name is ' + self.buddy_name.text() + '!')

            self.loaded = True
