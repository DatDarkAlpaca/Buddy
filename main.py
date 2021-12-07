from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtGui import QPixmap, QMovie

from qt_material import apply_stylesheet

from compiled_ui.main_window import Ui_MainWindow
from compiled_ui.mini_buddy import Ui_MiniBuddy

import pickle
import sys

# Todo: change the stylesheet according to the most frequent color.

buddy_path = 'gura.png'
spin_path = 'gura_spin.gif'


# Main Widget:
class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Mini Buddy:
        self.mini_buddy = MiniBuddy(self)
        self.mini_buddy.installEventFilter(self)

        # Buddy Image:
        self.load_buddy_image()

    # Initializers:
    def load_buddy_image(self):
        self.buddy_display.setPixmap(QPixmap(buddy_path))

    # Events:
    def mouseDoubleClickEvent(self, event):
        child = self.childAt(event.position().toPoint())
        if child:
            if child.objectName() == 'buddy_display':
                if event.button() == Qt.LeftButton:
                    self.show_mini_buddy()

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


# Mini Buddy:
class MiniBuddy(QMainWindow, Ui_MiniBuddy):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        # Draggable:
        self.offset = None

        # Movie:
        self.movie = QMovie(spin_path)
        self.playing = True

        # Transparency:
        self._set_background_color()

        self.initialize()

    # Initializers:
    def initialize(self):
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.mini_buddy_display.setMovie(self.movie)
        self.movie.start()

        self.setAttribute(Qt.WA_TranslucentBackground)

    # Events:
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.globalPosition().toPoint()

        elif event.button() == Qt.RightButton:
            if self.playing:
                self.movie.stop()
                self.playing = False
            else:
                self.movie.start()
                self.playing = True

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPosition().toPoint() - self.offset)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.offset = event.globalPosition().toPoint()

    # Helpers:
    def _set_background_color(self):
        self.setStyleSheet("background-color: rgba(35, 38, 41);")


# Buddy Class:
class Buddy:
    def __init__(self):
        self.max_status = 3
        self.fun, self.satiation, self.sleep, self.hygiene = [3] * 4

    @property
    def overall_state(self):
        return (self.fun + self.satiation + self.sleep + self.hygiene) / 4 * self.max_status

    # Actions:
    def feed_action(self):
        if self.satiation < self.max_status:
            self.satiation += 1

    def play_action(self):
        if self.fun < self.max_status:
            self.fun += 1

    def sleep_action(self):
        if self.sleep < self.max_status:
            self.sleep += 1

    def bath_action(self):
        if self.sleep < self.max_status:
            self.sleep += 1


# Data Serialization:
def save_buddy(b: Buddy):
    with open('buddy.sv', 'wb') as f:
        pickle.dump([b], f, protocol=2)


def load_buddy():
    with open('buddy.sv', 'rb') as f:
        b = pickle.load(f)

    return b


if __name__ == '__main__':
    buddy = Buddy()

    app = QApplication(sys.argv)
    widget = MainApplication()
    apply_stylesheet(app, theme='dark_teal.xml')

    widget.show()
    sys.exit(app.exec())
