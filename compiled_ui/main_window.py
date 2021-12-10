# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 400))
        MainWindow.setMaximumSize(QSize(500, 600))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 0, 9, 9)
        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.buddy_name = QLabel(self.central_widget)
        self.buddy_name.setObjectName(u"buddy_name")

        self.horizontalLayout.addWidget(self.buddy_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minimize_button = QPushButton(self.central_widget)
        self.minimize_button.setObjectName(u"minimize_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_button.sizePolicy().hasHeightForWidth())
        self.minimize_button.setSizePolicy(sizePolicy1)
        self.minimize_button.setMinimumSize(QSize(16, 16))
        self.minimize_button.setMaximumSize(QSize(16, 16))
        icon = QIcon()
        icon.addFile(u"../res/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setFlat(True)

        self.horizontalLayout.addWidget(self.minimize_button)

        self.settings_button = QPushButton(self.central_widget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(16, 16))
        self.settings_button.setMaximumSize(QSize(16, 16))
        self.settings_button.setLayoutDirection(Qt.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u"../res/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon1)
        self.settings_button.setFlat(True)

        self.horizontalLayout.addWidget(self.settings_button)

        self.close_button = QPushButton(self.central_widget)
        self.close_button.setObjectName(u"close_button")
        sizePolicy1.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy1)
        self.close_button.setMinimumSize(QSize(16, 16))
        self.close_button.setMaximumSize(QSize(16, 16))
        icon2 = QIcon()
        icon2.addFile(u"../res/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon2)
        self.close_button.setFlat(True)

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buddy_display = QLabel(self.central_widget)
        self.buddy_display.setObjectName(u"buddy_display")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buddy_display.sizePolicy().hasHeightForWidth())
        self.buddy_display.setSizePolicy(sizePolicy2)
        self.buddy_display.setPixmap(QPixmap(u"../gura.png"))
        self.buddy_display.setScaledContents(False)
        self.buddy_display.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.buddy_display)

        self.buddy_output = QTextEdit(self.central_widget)
        self.buddy_output.setObjectName(u"buddy_output")
        self.buddy_output.setEnabled(True)
        sizePolicy.setHeightForWidth(self.buddy_output.sizePolicy().hasHeightForWidth())
        self.buddy_output.setSizePolicy(sizePolicy)
        self.buddy_output.setMaximumSize(QSize(16777215, 100))
        self.buddy_output.setMouseTracking(True)
        self.buddy_output.setFocusPolicy(Qt.NoFocus)
        self.buddy_output.setReadOnly(True)

        self.verticalLayout.addWidget(self.buddy_output)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.button_spacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_layout.addItem(self.button_spacer_left)

        self.feed_button = QPushButton(self.central_widget)
        self.feed_button.setObjectName(u"feed_button")

        self.button_layout.addWidget(self.feed_button)

        self.play_button = QPushButton(self.central_widget)
        self.play_button.setObjectName(u"play_button")

        self.button_layout.addWidget(self.play_button)

        self.sleep_button = QPushButton(self.central_widget)
        self.sleep_button.setObjectName(u"sleep_button")

        self.button_layout.addWidget(self.sleep_button)

        self.button_spacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.button_layout.addItem(self.button_spacer_right)


        self.verticalLayout.addLayout(self.button_layout)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Buddy v1.0", None))
        self.buddy_name.setText(QCoreApplication.translate("MainWindow", u"Buddy", None))
        self.minimize_button.setText("")
        self.settings_button.setText("")
        self.close_button.setText("")
        self.buddy_display.setText("")
        self.buddy_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It loosk like you haven't created a Buddy yet.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click the gear icon to create one!</p></body></html>", None))
        self.feed_button.setText(QCoreApplication.translate("MainWindow", u"Feed", None))
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.sleep_button.setText(QCoreApplication.translate("MainWindow", u"Sleep", None))
    # retranslateUi

