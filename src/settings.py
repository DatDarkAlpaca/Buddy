from PySide6.QtWidgets import QMainWindow

from compiled_ui.settings import Ui_Settings


class Settings(QMainWindow, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
