# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buddy_builder.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_BuddyBuilder(object):
    def setupUi(self, BuddyBuilder):
        if not BuddyBuilder.objectName():
            BuddyBuilder.setObjectName(u"BuddyBuilder")
        BuddyBuilder.resize(600, 400)
        BuddyBuilder.setMinimumSize(QSize(600, 400))
        self.horizontalLayout = QHBoxLayout(BuddyBuilder)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 20, -1, -1)
        self.create_layout = QVBoxLayout()
        self.create_layout.setObjectName(u"create_layout")
        self.create_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.create_layout.setContentsMargins(-1, 0, 0, -1)
        self.title = QLabel(BuddyBuilder)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(14)
        self.title.setFont(font)

        self.create_layout.addWidget(self.title)

        self.vertical_spacer1 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.create_layout.addItem(self.vertical_spacer1)

        self.name_label = QLabel(BuddyBuilder)
        self.name_label.setObjectName(u"name_label")

        self.create_layout.addWidget(self.name_label)

        self.name_edit = QLineEdit(BuddyBuilder)
        self.name_edit.setObjectName(u"name_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())
        self.name_edit.setSizePolicy(sizePolicy)

        self.create_layout.addWidget(self.name_edit)

        self.not_empty_name = QLabel(BuddyBuilder)
        self.not_empty_name.setObjectName(u"not_empty_name")
        self.not_empty_name.setEnabled(True)
        self.not_empty_name.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.create_layout.addWidget(self.not_empty_name)

        self.profile_label = QLabel(BuddyBuilder)
        self.profile_label.setObjectName(u"profile_label")

        self.create_layout.addWidget(self.profile_label)

        self.profile_layout = QHBoxLayout()
        self.profile_layout.setSpacing(6)
        self.profile_layout.setObjectName(u"profile_layout")
        self.profile_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.profile_edit = QLineEdit(BuddyBuilder)
        self.profile_edit.setObjectName(u"profile_edit")
        sizePolicy.setHeightForWidth(self.profile_edit.sizePolicy().hasHeightForWidth())
        self.profile_edit.setSizePolicy(sizePolicy)
        self.profile_edit.setReadOnly(True)

        self.profile_layout.addWidget(self.profile_edit)

        self.profile_tool = QPushButton(BuddyBuilder)
        self.profile_tool.setObjectName(u"profile_tool")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(22)
        sizePolicy1.setVerticalStretch(22)
        sizePolicy1.setHeightForWidth(self.profile_tool.sizePolicy().hasHeightForWidth())
        self.profile_tool.setSizePolicy(sizePolicy1)
        self.profile_tool.setMinimumSize(QSize(22, 22))
        self.profile_tool.setMaximumSize(QSize(22, 22))

        self.profile_layout.addWidget(self.profile_tool)


        self.create_layout.addLayout(self.profile_layout)

        self.not_empty_profile = QLabel(BuddyBuilder)
        self.not_empty_profile.setObjectName(u"not_empty_profile")
        self.not_empty_profile.setEnabled(True)
        self.not_empty_profile.setMinimumSize(QSize(0, 0))
        self.not_empty_profile.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.not_empty_profile.setFrameShape(QFrame.NoFrame)

        self.create_layout.addWidget(self.not_empty_profile)

        self.buddy_label = QLabel(BuddyBuilder)
        self.buddy_label.setObjectName(u"buddy_label")

        self.create_layout.addWidget(self.buddy_label)

        self.buddy_layout = QHBoxLayout()
        self.buddy_layout.setObjectName(u"buddy_layout")
        self.buddy_edit = QLineEdit(BuddyBuilder)
        self.buddy_edit.setObjectName(u"buddy_edit")
        sizePolicy.setHeightForWidth(self.buddy_edit.sizePolicy().hasHeightForWidth())
        self.buddy_edit.setSizePolicy(sizePolicy)
        self.buddy_edit.setReadOnly(True)

        self.buddy_layout.addWidget(self.buddy_edit)

        self.buddy_tool = QPushButton(BuddyBuilder)
        self.buddy_tool.setObjectName(u"buddy_tool")
        self.buddy_tool.setMinimumSize(QSize(22, 22))
        self.buddy_tool.setMaximumSize(QSize(22, 22))
        self.buddy_tool.setBaseSize(QSize(22, 22))

        self.buddy_layout.addWidget(self.buddy_tool)


        self.create_layout.addLayout(self.buddy_layout)

        self.not_empty_buddy = QLabel(BuddyBuilder)
        self.not_empty_buddy.setObjectName(u"not_empty_buddy")
        self.not_empty_buddy.setEnabled(True)
        self.not_empty_buddy.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.create_layout.addWidget(self.not_empty_buddy)

        self.vertical_spacer0 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.create_layout.addItem(self.vertical_spacer0)


        self.horizontalLayout.addLayout(self.create_layout)

        self.apply_layout_out = QVBoxLayout()
        self.apply_layout_out.setSpacing(6)
        self.apply_layout_out.setObjectName(u"apply_layout_out")
        self.apply_layout_out.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.apply_layout_out.setContentsMargins(9, -1, -1, -1)
        self.preview_layout = QVBoxLayout()
        self.preview_layout.setObjectName(u"preview_layout")
        self.preview_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.preview_layout.setContentsMargins(-1, 0, -1, -1)
        self.top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.preview_layout.addItem(self.top_spacer)

        self.profile_preview = QLabel(BuddyBuilder)
        self.profile_preview.setObjectName(u"profile_preview")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.profile_preview.sizePolicy().hasHeightForWidth())
        self.profile_preview.setSizePolicy(sizePolicy2)
        self.profile_preview.setMinimumSize(QSize(150, 150))
        self.profile_preview.setMaximumSize(QSize(150, 150))
        font1 = QFont()
        font1.setStrikeOut(True)
        self.profile_preview.setFont(font1)
        self.profile_preview.setLayoutDirection(Qt.RightToLeft)
        self.profile_preview.setAutoFillBackground(False)
        self.profile_preview.setFrameShape(QFrame.NoFrame)
        self.profile_preview.setFrameShadow(QFrame.Plain)
        self.profile_preview.setPixmap(QPixmap(u"../gura.png"))
        self.profile_preview.setScaledContents(True)
        self.profile_preview.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.profile_preview.setMargin(0)

        self.preview_layout.addWidget(self.profile_preview)

        self.mini_buddy_preview = QLabel(BuddyBuilder)
        self.mini_buddy_preview.setObjectName(u"mini_buddy_preview")
        sizePolicy2.setHeightForWidth(self.mini_buddy_preview.sizePolicy().hasHeightForWidth())
        self.mini_buddy_preview.setSizePolicy(sizePolicy2)
        self.mini_buddy_preview.setMinimumSize(QSize(100, 100))
        self.mini_buddy_preview.setMaximumSize(QSize(100, 100))
        self.mini_buddy_preview.setLayoutDirection(Qt.RightToLeft)
        self.mini_buddy_preview.setPixmap(QPixmap(u"../gura_spin.gif"))
        self.mini_buddy_preview.setScaledContents(True)
        self.mini_buddy_preview.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.preview_layout.addWidget(self.mini_buddy_preview)


        self.apply_layout_out.addLayout(self.preview_layout)

        self.vertical_spacer_apply = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.apply_layout_out.addItem(self.vertical_spacer_apply)

        self.apply_layout = QHBoxLayout()
        self.apply_layout.setObjectName(u"apply_layout")
        self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.apply_layout.addItem(self.left_spacer)

        self.back_button = QPushButton(BuddyBuilder)
        self.back_button.setObjectName(u"back_button")

        self.apply_layout.addWidget(self.back_button)

        self.create_button = QPushButton(BuddyBuilder)
        self.create_button.setObjectName(u"create_button")

        self.apply_layout.addWidget(self.create_button)

        self.right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.apply_layout.addItem(self.right_spacer)


        self.apply_layout_out.addLayout(self.apply_layout)


        self.horizontalLayout.addLayout(self.apply_layout_out)


        self.retranslateUi(BuddyBuilder)

        QMetaObject.connectSlotsByName(BuddyBuilder)
    # setupUi

    def retranslateUi(self, BuddyBuilder):
        BuddyBuilder.setWindowTitle(QCoreApplication.translate("BuddyBuilder", u"Buddy Builder", None))
        self.title.setText(QCoreApplication.translate("BuddyBuilder", u"Create a new buddy", None))
        self.name_label.setText(QCoreApplication.translate("BuddyBuilder", u"Name:", None))
        self.not_empty_name.setText(QCoreApplication.translate("BuddyBuilder", u"This field cannot be empty.", None))
        self.profile_label.setText(QCoreApplication.translate("BuddyBuilder", u"Profile Picture:", None))
#if QT_CONFIG(tooltip)
        self.profile_tool.setToolTip(QCoreApplication.translate("BuddyBuilder", u"Loads a file from your computer.", None))
#endif // QT_CONFIG(tooltip)
        self.profile_tool.setText(QCoreApplication.translate("BuddyBuilder", u"...", None))
        self.not_empty_profile.setText(QCoreApplication.translate("BuddyBuilder", u"This field cannot be empty.", None))
        self.buddy_label.setText(QCoreApplication.translate("BuddyBuilder", u"Mini Buddy Picture:", None))
#if QT_CONFIG(tooltip)
        self.buddy_edit.setToolTip(QCoreApplication.translate("BuddyBuilder", u"Loads a file from your computer.", None))
#endif // QT_CONFIG(tooltip)
        self.buddy_tool.setText(QCoreApplication.translate("BuddyBuilder", u"...", None))
        self.not_empty_buddy.setText(QCoreApplication.translate("BuddyBuilder", u"This field cannot be empty.", None))
#if QT_CONFIG(tooltip)
        self.profile_preview.setToolTip(QCoreApplication.translate("BuddyBuilder", u"This is the profile picture preview.", None))
#endif // QT_CONFIG(tooltip)
        self.profile_preview.setText("")
#if QT_CONFIG(tooltip)
        self.mini_buddy_preview.setToolTip(QCoreApplication.translate("BuddyBuilder", u"This is the Mini Buddy preview.", None))
#endif // QT_CONFIG(tooltip)
        self.mini_buddy_preview.setText("")
        self.back_button.setText(QCoreApplication.translate("BuddyBuilder", u"Back", None))
        self.create_button.setText(QCoreApplication.translate("BuddyBuilder", u"Create", None))
    # retranslateUi

