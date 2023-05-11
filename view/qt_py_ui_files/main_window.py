# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 495)
        self.action_new_project = QAction(MainWindow)
        self.action_new_project.setObjectName(u"action_new_project")
        self.actiondestroy_project = QAction(MainWindow)
        self.actiondestroy_project.setObjectName(u"actiondestroy_project")
        self.actionsetting = QAction(MainWindow)
        self.actionsetting.setObjectName(u"actionsetting")
        self.actionimport_and_export = QAction(MainWindow)
        self.actionimport_and_export.setObjectName(u"actionimport_and_export")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.newProjectBtn = QPushButton(self.widget)
        self.newProjectBtn.setObjectName(u"newProjectBtn")
        self.newProjectBtn.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.newProjectBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 845, 22))
        self.menuproject = QMenu(self.menuBar)
        self.menuproject.setObjectName(u"menuproject")
        self.menuhelp = QMenu(self.menuBar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuproject.menuAction())
        self.menuBar.addAction(self.menuhelp.menuAction())
        self.menuproject.addAction(self.action_new_project)
        self.menuproject.addAction(self.actionimport_and_export)
        self.menuproject.addAction(self.actionsetting)
        self.menuproject.addAction(self.actionexit)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_new_project.setText(QCoreApplication.translate("MainWindow", u"new project", None))
        self.actiondestroy_project.setText(QCoreApplication.translate("MainWindow", u"destroy project", None))
        self.actionsetting.setText(QCoreApplication.translate("MainWindow", u"setting", None))
        self.actionimport_and_export.setText(QCoreApplication.translate("MainWindow", u"import and export", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"projects", None))
        self.newProjectBtn.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.menuproject.setTitle(QCoreApplication.translate("MainWindow", u"application", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

