from PySide6.QtCore import QTimer, SIGNAL
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QImage, QPixmap

from collections import deque


class Display(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.delay = 100
        self.frames = deque()

        # Timer:
        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL("timeout()"), self._animate)
        self.timer.start(self.delay)

    def set_buddy(self, buddy_resource):
        if isinstance(buddy_resource, QImage):
            self.frames.append(buddy_resource)

        elif isinstance(buddy_resource, list):
            self.frames = deque(buddy_resource)

        else:
            print(self.frames)

        self.setPixmap(QPixmap.fromImage(self.frames[0]))

    def _animate(self):
        self.setPixmap(QPixmap.fromImage(self.frames[0]))
        self.frames.rotate(1)
