from PySide6.QtWidgets import QMainWindow, QFileDialog
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

        # Setup:
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.statusBar()

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
        # Loading the first available buddy:
        buddy_file = load_buddy('/saves/', None)
        name, buddy_profile, mini_buddy_image = [None] * 3
        if buddy_file:
            buddy_profile = buddy_file.get('profile_picture')
            mini_buddy_image = buddy_file.get('mini_buddy_picture')
            name = buddy_file.get('name')

        # Name:
        if not name:
            self.buddy_name.setText('Buddy')
        else:
            self.buddy_name.setText(name)
            self.change_output('Hello, my name is ' + name + '!')
            self.loaded = True

        # Profile Picture:
        self.buddy_display.set_buddy(buddy_profile)

        # Buddy Picture:
        self.mini_buddy.mini_buddy_display.set_buddy(mini_buddy_image)

    def bind_buttons(self):
        # Minimize button:
        self.minimize_button.setIcon(QPixmap('res/minus.png'))
        self.minimize_button.clicked.connect(self.showMinimized)

        # Settings button:
        self.settings_button.setIcon(QPixmap('res/setting.png'))
        self.settings_button.clicked.connect(self.buddy_builder_method)

        # Import button:
        self.import_button.setIcon(QPixmap('res/import.png'))
        self.import_button.clicked.connect(self.import_buddy)

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

    # Output
    def change_output(self, text):
        self.buddy_output.setText('<center>' + text + '</center>')

    def import_buddy(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                              str(Path().resolve()), 'Image files (*.buddy)')
        if path == '':
            return

        buddy_file = load_buddy(path, basename(path))

        if not buddy_file:
            return

        buddy_profile = buddy_file.get('profile_picture')
        mini_buddy = buddy_file.get('mini_buddy_picture')
        name = buddy_file.get('name')

        self.mini_buddy.mini_buddy_display.set_buddy(mini_buddy)

        self.buddy_display.set_buddy(buddy_profile)

        self.buddy_name.setText(name)

        self.change_output('Hello, my name is ' + name + '!')

        self.loaded = True

    # Buddy Builder:
    def buddy_builder_method(self):
        self.buddy_builder.exec()

        buddy_name = self.buddy_builder.file_save
        buddy_file = load_buddy(f"./saves/{buddy_name}/{buddy_name}.cif", buddy_name)

        if not buddy_file:
            return

        buddy_profile = buddy_file.get('profile_picture')
        mini_buddy = buddy_file.get('mini_buddy_picture')
        name = buddy_file.get('name')

        self.mini_buddy.mini_buddy_display.set_buddy(mini_buddy)

        self.buddy_display.set_buddy(buddy_profile)

        self.buddy_name.setText(name)

        self.change_output('Hello, my name is ' + name + '!')

        self.loaded = True