# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(755, 479)
        self.centralwidget = QWidget(Settings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.settings_list = QListWidget(self.centralwidget)
        QListWidgetItem(self.settings_list)
        QListWidgetItem(self.settings_list)
        self.settings_list.setObjectName(u"settings_list")

        self.horizontalLayout.addWidget(self.settings_list)

        self.stacked_settings = QStackedWidget(self.centralwidget)
        self.stacked_settings.setObjectName(u"stacked_settings")
        self.help_page = QWidget()
        self.help_page.setObjectName(u"help_page")
        self.stacked_settings.addWidget(self.help_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.stacked_settings.addWidget(self.about_page)

        self.horizontalLayout.addWidget(self.stacked_settings)

        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))

        __sortingEnabled = self.settings_list.isSortingEnabled()
        self.settings_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.settings_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Settings", u"About", None));
        ___qlistwidgetitem1 = self.settings_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Settings", u"Help", None));
        self.settings_list.setSortingEnabled(__sortingEnabled)

    # retranslateUi

