from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
import sys

from serialization import check_for_saves, load_buddy
from main_app import MainApplication


if __name__ == '__main__':
    # Loading:
    buddy_save = check_for_saves()

    name = None
    buddy_profile, mini_buddy = None, None

    if buddy_save:
        buddy_file = load_buddy(buddy_save)
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
