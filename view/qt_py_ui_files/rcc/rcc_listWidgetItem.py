# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rcc_listWidgetItem.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_0(object):
    def setupUi(self, 0):
        if not 0.objectName():
            0.setObjectName(u"0")
        0.resize(359, 46)
        self.gridLayout = QGridLayout(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(0)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_rcc_in = QLineEdit(0)
        self.lineEdit_rcc_in.setObjectName(u"lineEdit_rcc_in")

        self.horizontalLayout.addWidget(self.lineEdit_rcc_in)

        self.pushButton_open_in_file = QPushButton(0)
        self.pushButton_open_in_file.setObjectName(u"pushButton_open_in_file")

        self.horizontalLayout.addWidget(self.pushButton_open_in_file)

        self.label_2 = QLabel(0)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_rcc_out = QLineEdit(0)
        self.lineEdit_rcc_out.setObjectName(u"lineEdit_rcc_out")

        self.horizontalLayout.addWidget(self.lineEdit_rcc_out)

        self.pushButton_open_out_file = QPushButton(0)
        self.pushButton_open_out_file.setObjectName(u"pushButton_open_out_file")

        self.horizontalLayout.addWidget(self.pushButton_open_out_file)

        self.checkBox_is_enable = QCheckBox(0)
        self.checkBox_is_enable.setObjectName(u"checkBox_is_enable")

        self.horizontalLayout.addWidget(self.checkBox_is_enable)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(0)

        QMetaObject.connectSlotsByName(0)
    # setupUi

    def retranslateUi(self, 0):
        0.setWindowTitle(QCoreApplication.translate("0", u"Form", None))
        self.label.setText(QCoreApplication.translate("0", u"in", None))
        self.pushButton_open_in_file.setText(QCoreApplication.translate("0", u"open", None))
        self.label_2.setText(QCoreApplication.translate("0", u"out", None))
        self.pushButton_open_out_file.setText(QCoreApplication.translate("0", u"open", None))
        self.checkBox_is_enable.setText("")
    # retranslateUi

