from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtGui import QPixmap

from compiled_ui.buddy_builder import Ui_BuddyBuilder
from pathlib import Path

from serialization import BuddyFile, save_buddy


class BuddyBuilder(QDialog, Ui_BuddyBuilder):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Validation:
        self.file_save = ''
        self.valid = True

        self.initialize()
        self.binding()

        # Buddy Properties:
        self.buddy_name, self.profile_path, self.mini_buddy_path = [''] * 3

    def initialize(self):
        # Todo: use the text rather than the visibility.
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
        path, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                              str(Path().resolve()), 'Image files (*.png *.jpg *.gif)')
        if path != '':
            self.profile_path = path

        self.profile_edit.setText(self.profile_path)

        self.profile_preview.setPixmap(QPixmap(self.profile_path))

    def set_mini_buddy_path(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                              str(Path().resolve()), 'Image files (*.png *.jpg *.gif)')
        if path != '':
            self.mini_buddy_path = path

        self.buddy_edit.setText(self.mini_buddy_path)

        self.mini_buddy_preview.setPixmap(QPixmap(self.mini_buddy_path))

    # Create Buddy:
    def create_buddy(self):
        self._validate()

        if self.valid:
            buddy_obj = BuddyFile(self.name_edit.text(), self.profile_path, self.mini_buddy_path)

            self.file_save = self.name_edit.text().replace(' ', '-')
            save_buddy(buddy_obj, self.file_save)

            self.close()

    # Helpers:
    def _validate(self):
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
