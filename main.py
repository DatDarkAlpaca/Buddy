from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
import sys

from serialization import load_buddy
from main_app import MainApplication
from os import mkdir, path


if __name__ == '__main__':
    name = None
    buddy_profile, mini_buddy = None, None

    if not path.isdir('./saves'):
        mkdir('saves')

    buddy_file = load_buddy('/saves/', None)
    if buddy_file:
        buddy_profile = buddy_file.get('profile_picture')
        mini_buddy = buddy_file.get('mini_buddy_picture')
        name = buddy_file.get('name')

    # Main Application:
    app = QApplication(sys.argv)
    widget = MainApplication(None, name, buddy_profile, mini_buddy)

    # Stylesheet:
    apply_stylesheet(app, theme='dark_cyan.xml')

    widget.show()
    sys.exit(app.exec())
