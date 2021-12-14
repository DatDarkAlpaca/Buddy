from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtGui import QPixmap

from compiled_ui.main_window import Ui_MainWindow
from src.buddy_builder import BuddyBuilder
from src.mini_buddy import MiniBuddy
from src.settings import Settings

from src.serialization import load_buddy, load_icons
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

        # Settings:
        self.settings = Settings(self)
        self.settings.show()

        self.dragging_window, self.loaded = False, False
        self.offset = QPoint()
        self.icons = []

        self.initialize()
        self.bind_buttons()

    # Initialize:
    def initialize(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.statusBar()

        self.load_icons()
        self.load_buddy()

        # Name:
        if self.buddy_name.text() == '':
            self.buddy_name.setText('Buddy')

    def bind_buttons(self):
        # Minimize button:
        self.minimize_button.setIcon(QPixmap(self.icons['minus']))
        self.minimize_button.clicked.connect(self.showMinimized)

        # Settings button:
        self.settings_button.setIcon(QPixmap(self.icons['setting']))

        # Import button:
        self.import_button.setIcon(QPixmap(self.icons['import']))
        self.import_button.clicked.connect(self.new_buddy_action)

        # Close button:
        self.close_button.setIcon(QPixmap(self.icons['close']))
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
        self.change_output('Snore')

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
        dialog.addButton('Import', dialog.ActionRole)
        dialog.addButton('Create', dialog.ActionRole)

        button_option = dialog.exec()

        if button_option == 0:
            dialog.close()
            self.import_buddy_action()

        elif button_option == 1:
            dialog.close()
            self.buddy_builder_action()

    def buddy_builder_action(self):
        self.buddy_builder.exec()

        self.load_buddy(self.buddy_builder.file_save)

    def import_buddy_action(self):
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

    def load_icons(self):
        self.icons = load_icons('./res/icons.res')
        if not self.icons:
            self.icons = load_icons('./res/icons')
