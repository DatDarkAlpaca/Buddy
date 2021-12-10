from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMovie, QPixmap, QImage

from compiled_ui.mini_buddy import Ui_MiniBuddy


class MiniBuddy(QMainWindow, Ui_MiniBuddy):
    def __init__(self, parent, mini_buddy_image):
        super().__init__(parent)
        self.setupUi(self)

        # Draggable:
        self.offset = QPoint()

        # Mini Buddy:
        self.mini_buddy = None

        if isinstance(mini_buddy_image, QImage):
            self.mini_buddy = QPixmap().fromImage(mini_buddy_image)

        elif isinstance(mini_buddy_image, str):
            self.mini_buddy = QMovie(mini_buddy_image)

        # Variables:
        self.playing, self.dragging = True, False

        # Transparency:
        self._set_background_color()

        self.initialize()

    # Initializers:
    def initialize(self):
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)

        if isinstance(self.mini_buddy, QPixmap):
            self.mini_buddy_display.setPixmap(self.mini_buddy)

        elif isinstance(self.mini_buddy, QMovie):
            self.mini_buddy_display.setMovie(self.mini_buddy)
            self.mini_buddy.start()

        self.setAttribute(Qt.WA_TranslucentBackground)

    # Events:
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.globalPosition().toPoint()
            self.dragging = True

        if event.button() == Qt.RightButton:
            if not isinstance(self.mini_buddy, QMovie):
                return

            if self.playing:
                self.mini_buddy.stop()
                self.playing = False
            else:
                self.mini_buddy.start()
                self.playing = True

    def mouseReleaseEvent(self, event):
        self.dragging = False

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = QPoint(event.globalPosition().toPoint() - self.offset)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.offset = event.globalPosition().toPoint()

    # Helpers:
    def _set_background_color(self):
        self.setStyleSheet("background-color: rgba(35, 38, 41);")
