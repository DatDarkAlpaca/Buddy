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
        MainWindow.setMinimumSize(QSize(300, 400))
        MainWindow.setMaximumSize(QSize(500, 600))
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 0, 9, 9)
        self.buddy_display = QLabel(self.central_widget)
        self.buddy_display.setObjectName(u"buddy_display")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buddy_display.sizePolicy().hasHeightForWidth())
        self.buddy_display.setSizePolicy(sizePolicy)
        self.buddy_display.setPixmap(QPixmap(u"../gura.png"))
        self.buddy_display.setScaledContents(False)
        self.buddy_display.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.buddy_display)

        self.buddy_output = QTextEdit(self.central_widget)
        self.buddy_output.setObjectName(u"buddy_output")
        self.buddy_output.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buddy_output.sizePolicy().hasHeightForWidth())
        self.buddy_output.setSizePolicy(sizePolicy1)
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
        self.buddy_display.setText("")
        self.buddy_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hello! My name is Blank!</p></body></html>", None))
        self.feed_button.setText(QCoreApplication.translate("MainWindow", u"Feed", None))
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.sleep_button.setText(QCoreApplication.translate("MainWindow", u"Sleep", None))
    # retranslateUi

