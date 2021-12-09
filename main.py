from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtGui import QPixmap, QMovie

from compiled_ui import main_window, mini_buddy, buddy_builder
from qt_material import apply_stylesheet

from pathlib import Path

import pickle
import sys

g_buddy_path = 'gura.png'
spin_path = 'gura_spin.gif'


# Main Widget:
class MainApplication(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Mini Buddy:
        self.mini_buddy = MiniBuddy(self)
        self.mini_buddy.installEventFilter(self)

        # Buddy Builder:
        self.buddy_builder = BuddyBuilder(self)
        self.buddy_builder.show()

        # Buddy Image:
        self.load_buddy_image()
        self.buddy_display.setScaledContents(True)

        # Todo: check whether the user has loaded a buddy previously.

    # Initializers:
    def load_buddy_image(self):
        self.buddy_display.setPixmap(QPixmap(g_buddy_path))

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
class MiniBuddy(QMainWindow, mini_buddy.Ui_MiniBuddy):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        # Draggable:
        self.offset = QPoint()

        # Movie:
        self.movie = QMovie(spin_path)
        self.playing, self.dragging = True, False

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
            self.dragging = True

        if event.button() == Qt.RightButton:
            if self.playing:
                self.movie.stop()
                self.playing = False
            else:
                self.movie.start()
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


# Buddy Builder:
class BuddyBuilder(QMainWindow, buddy_builder.Ui_BuddyBuilder):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Validation:
        self.valid = True

        self.initialize()
        self.binding()

        # Fixing paths:
        self.profile_preview.setPixmap(g_buddy_path)
        self.mini_buddy_preview.setPixmap(spin_path)

        # Buddy Properties:
        self.profile_path, self.mini_buddy_path = '', ''

    def initialize(self):
        self.not_empty_name.setVisible(False)
        self.not_empty_profile.setVisible(False)
        self.not_empty_buddy.setVisible(False)

    def binding(self):
        # Apply Buttons:
        self.create_button.clicked.connect(self.create_buddy)
        self.back_button.clicked.connect(self.close)

        # Path Buttons:
        self.profile_tool.clicked.connect(self.set_profile_picture_path)
        self.buddy_tool.clicked.connect(self.set_mini_buddy_path)

    def set_profile_picture_path(self):
        path = QFileDialog.getOpenFileName(self, 'Open file', str(Path().resolve()), 'Image files (*.jpg *.gif)')
        if path != '':
            self.profile_path = path[0]

        self.profile_preview.setPixmap(QPixmap(self.profile_path))

    def set_mini_buddy_path(self):
        path = QFileDialog.getOpenFileName(self, 'Open file', str(Path().resolve()), 'Image files (*.png *.jpg *.gif)')
        if path != '':
            self.mini_buddy_path = path[0]

        self.mini_buddy_preview.setPixmap(QPixmap(self.mini_buddy_path))

    # Create Buddy:
    def create_buddy(self):
        self.validate()

        if self.valid:
            self.close()

    # Helpers:
    def validate(self):
        self.valid = True

        if self.name_edit.text() == '':
            self.not_empty_name.setVisible(True)
            self.valid = False
        else:
            self.not_empty_name.setVisible(False)

        if self.profile_edit.text() == '':
            self.not_empty_profile.setVisible(True)
            self.valid = False
        else:
            self.not_empty_profile.setVisible(False)

        if self.buddy_edit.text() == '':
            self.not_empty_buddy.setVisible(True)
            self.valid = False
        else:
            self.not_empty_buddy.setVisible(False)

    def _is_path_valid(self):
        pass

    def _determine_resource_type(self):
        pass


# Buddy file:
class BuddyFile:
    def __init__(self, name='', profile_path='', buddy_path='', is_profile_movie=False, is_buddy_movie=False):
        self.name = name

        # Profile Pixmap/Movie:
        if is_profile_movie:
            self.profile_picture = QMovie(profile_path)
        else:
            self.profile_picture = QPixmap(profile_path)

        # Buddy Pixmap/Movie:
        if is_buddy_movie:
            self.buddy_picture = QMovie(buddy_path)
        else:
            self.buddy_picture = QPixmap(buddy_path)


# Buddy Class:
class Buddy:
    def __init__(self):
        # Todo: add owner ID/name.
        # Todo: add the images here too.
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
    app = QApplication(sys.argv)
    widget = MainApplication()
    apply_stylesheet(app, theme='dark_teal.xml')

    widget.show()
    sys.exit(app.exec())
