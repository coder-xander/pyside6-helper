# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setttings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_settings_dialog(object):
    def setupUi(self, settings_dialog):
        if not settings_dialog.objectName():
            settings_dialog.setObjectName(u"settings_dialog")
        settings_dialog.resize(633, 295)
        self.gridLayout_2 = QGridLayout(settings_dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(settings_dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_10 = QPushButton(self.widget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout.addWidget(self.pushButton_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(111, 0))

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.pushButton_27 = QPushButton(self.widget_3)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.pushButton_27, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)

        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_17, 0, 4, 1, 1)

        self.lineEdit_22 = QLineEdit(self.widget_3)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.lineEdit_22, 0, 5, 1, 1)

        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(111, 0))

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.widget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 1, 1, 1, 1)

        self.pushButton_28 = QPushButton(self.widget_3)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.pushButton_28, 1, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 1, 3, 1, 1)

        self.label_23 = QLabel(self.widget_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_23, 1, 4, 1, 1)

        self.lineEdit_21 = QLineEdit(self.widget_3)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.lineEdit_21, 1, 5, 1, 1)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(111, 0))

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.pushButton_29 = QPushButton(self.widget_3)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.pushButton_29, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 5, 1, 1)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(111, 0))

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.pushButton_30 = QPushButton(self.widget_3)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.pushButton_30, 3, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 3, 5, 1, 1)

        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(111, 0))

        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 4, 1, 1, 1)

        self.pushButton_31 = QPushButton(self.widget_3)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMaximumSize(QSize(30, 16777215))

        self.gridLayout.addWidget(self.pushButton_31, 4, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 4, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 4, 5, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.pushButton_18 = QPushButton(settings_dialog)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_2.addWidget(self.pushButton_18)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.retranslateUi(settings_dialog)

        QMetaObject.connectSlotsByName(settings_dialog)
    # setupUi

    def retranslateUi(self, settings_dialog):
        settings_dialog.setWindowTitle(QCoreApplication.translate("settings_dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("settings_dialog", u"path setting", None))
        self.pushButton_10.setText(QCoreApplication.translate("settings_dialog", u"probe all", None))
        self.pushButton_11.setText(QCoreApplication.translate("settings_dialog", u"import from another project", None))
        self.label_4.setText(QCoreApplication.translate("settings_dialog", u"uic.exe path", None))
        self.lineEdit_4.setText("")
        self.pushButton_27.setText(QCoreApplication.translate("settings_dialog", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("settings_dialog", u"probe ", None))
        self.label_17.setText(QCoreApplication.translate("settings_dialog", u"pre paras:", None))
        self.lineEdit_22.setText(QCoreApplication.translate("settings_dialog", u"-o", None))
        self.label_12.setText(QCoreApplication.translate("settings_dialog", u"rcc.exe path", None))
        self.pushButton_28.setText(QCoreApplication.translate("settings_dialog", u"...", None))
        self.pushButton_9.setText(QCoreApplication.translate("settings_dialog", u"probe ", None))
        self.label_23.setText(QCoreApplication.translate("settings_dialog", u"pre paras:", None))
        self.lineEdit_21.setText(QCoreApplication.translate("settings_dialog", u"-o", None))
        self.label_9.setText(QCoreApplication.translate("settings_dialog", u"linguist.exe path", None))
        self.pushButton_29.setText(QCoreApplication.translate("settings_dialog", u"...", None))
        self.pushButton_2.setText(QCoreApplication.translate("settings_dialog", u"probe ", None))
        self.label_10.setText(QCoreApplication.translate("settings_dialog", u"designer.exe path", None))
        self.pushButton_30.setText(QCoreApplication.translate("settings_dialog", u"...", None))
        self.pushButton_3.setText(QCoreApplication.translate("settings_dialog", u"probe ", None))
        self.label_11.setText(QCoreApplication.translate("settings_dialog", u"qt assistant.exe path", None))
        self.pushButton_31.setText(QCoreApplication.translate("settings_dialog", u"...", None))
        self.pushButton_4.setText(QCoreApplication.translate("settings_dialog", u"probe ", None))
        self.pushButton_18.setText(QCoreApplication.translate("settings_dialog", u"ok", None))
    # retranslateUi

