from PySide6.QtGui import QPixmap, QImage, QMovie
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtWidgets import QMainWindow, QMessageBox

from compiled_ui.main_window import Ui_MainWindow
from buddy_builder import BuddyBuilder
from mini_buddy import MiniBuddy


class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, name=None, profile_picture=None, mini_buddy_image=None):
        super().__init__(parent)

        # Setup:
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.statusBar()
        self.loaded = False

        # Name:
        if not name:
            self.buddy_name.setText('Buddy')
        else:
            self.buddy_name.setText(name)
            self.change_output('Hello, my name is ' + name + '!')
            self.loaded = True

        # Profile Picture:
        if profile_picture:
            if isinstance(profile_picture, QImage):
                self.buddy_display.setPixmap(QPixmap.fromImage(profile_picture))

            elif isinstance(profile_picture, str):
                self.buddy_movie = QMovie(profile_picture)
                self.buddy_display.setMovie(self.buddy_movie)
                self.buddy_movie.start()

        # Mini Buddy:
        self.mini_buddy = MiniBuddy(self, mini_buddy_image)
        self.mini_buddy.installEventFilter(self)

        # Buddy Builder:
        self.buddy_builder = BuddyBuilder(self)

        # Dragging:
        self.dragging_window = False
        self.offset = QPoint()

        self.initialize()

    # Initialize:
    def initialize(self):
        # Minimize button:
        self.minimize_button.setIcon(QPixmap('res/minus.png'))
        self.minimize_button.clicked.connect(self.showMinimized)

        # Settings button:
        self.settings_button.setIcon(QPixmap('res/setting.png'))
        self.settings_button.clicked.connect(self.buddy_builder_method)

        # Close button:
        self.close_button.setIcon(QPixmap('res/close.png'))
        self.close_button.clicked.connect(self.close)

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

    # Buddy Builder:
    def buddy_builder_method(self):
        self.buddy_builder.exec()

        msg = QMessageBox()
        msg.setWindowFlags(Qt.FramelessWindowHint)
        msg.setText('You need to restart the application in order to update your changes.')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

