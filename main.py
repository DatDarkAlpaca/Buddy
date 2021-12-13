# Special thanks to flaticon, joalfa, Ranah Pixel Studio
# from Flaticon for the icons. I'll add an about page later.

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
import sys

from src.main_app import MainApplication
from os import mkdir, path


if __name__ == '__main__':
    if not path.isdir('./saves'):
        mkdir('saves')

    # Main Application:
    app = QApplication(sys.argv)
    widget = MainApplication(None)

    # Stylesheet:
    apply_stylesheet(app, theme='dark_cyan.xml')

    widget.show()
    sys.exit(app.exec())
