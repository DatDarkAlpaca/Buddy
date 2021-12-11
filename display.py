from PySide6.QtCore import QTimer, SIGNAL, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel

from collections import deque


class Display(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Animation:
        self.frames = deque()
        self.playing = True
        self.delay = 50

        # Timer:
        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL("timeout()"), self._animate)
        self.timer.start(self.delay)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.playing = not self.playing

        event.ignore()

    def set_buddy(self, buddy_resource):
        self.frames.clear()

        if isinstance(buddy_resource, QImage):
            self.frames.append(buddy_resource)

        elif isinstance(buddy_resource, list):
            self.frames = deque(buddy_resource)

        self.setPixmap(QPixmap.fromImage(self.frames[0]))

    def _animate(self):
        if self.frames and self.playing:
            self.setPixmap(QPixmap.fromImage(self.frames[0]))
            self.frames.rotate(-1)
