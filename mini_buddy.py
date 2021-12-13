from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, QPoint

from compiled_ui.mini_buddy import Ui_MiniBuddy


class MiniBuddy(QMainWindow, Ui_MiniBuddy):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Variables:
        self.dragging = False
        self.offset = QPoint()

        self.initialize()

    # Initializers:
    def initialize(self):
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self._set_background_color()

        self.setAttribute(Qt.WA_TranslucentBackground)

    # Events:
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.globalPosition().toPoint()
            self.dragging = True

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
