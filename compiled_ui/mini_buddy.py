# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mini_buddy.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from src.display import Display


class Ui_MiniBuddy(object):
    def setupUi(self, MiniBuddy):
        if not MiniBuddy.objectName():
            MiniBuddy.setObjectName(u"MiniBuddy")
        MiniBuddy.resize(150, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MiniBuddy.sizePolicy().hasHeightForWidth())
        MiniBuddy.setSizePolicy(sizePolicy)
        MiniBuddy.setMinimumSize(QSize(150, 150))
        self.central_widget = QWidget(MiniBuddy)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.central_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mini_buddy_display = Display(self.central_widget)
        self.mini_buddy_display.setObjectName(u"mini_buddy_display")
        self.mini_buddy_display.setPixmap(QPixmap(u"../gura.png"))
        self.mini_buddy_display.setScaledContents(True)
        self.mini_buddy_display.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mini_buddy_display, 0, 0, 1, 1)

        MiniBuddy.setCentralWidget(self.central_widget)

        self.retranslateUi(MiniBuddy)

        QMetaObject.connectSlotsByName(MiniBuddy)
    # setupUi

    def retranslateUi(self, MiniBuddy):
        MiniBuddy.setWindowTitle(QCoreApplication.translate("MiniBuddy", u"Mini Buddy", None))
        self.mini_buddy_display.setText("")
    # retranslateUi

