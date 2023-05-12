# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rcc_setting_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_RccSettingDlg(object):
    def setupUi(self, RccSettingDlg):
        if not RccSettingDlg.objectName():
            RccSettingDlg.setObjectName(u"RccSettingDlg")
        RccSettingDlg.resize(282, 479)
        self.gridLayout = QGridLayout(RccSettingDlg)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(21, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 2)

        self.pushButton_ok = QPushButton(RccSettingDlg)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.gridLayout.addWidget(self.pushButton_ok, 2, 4, 1, 2)

        self.listWidget = QListWidget(RccSettingDlg)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 6)

        self.horizontalSpacer_3 = QSpacerItem(47, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.label = QLabel(RccSettingDlg)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.pushButton__new_item = QPushButton(RccSettingDlg)
        self.pushButton__new_item.setObjectName(u"pushButton__new_item")

        self.gridLayout.addWidget(self.pushButton__new_item, 0, 3, 1, 1)

        self.pushButton_del_item = QPushButton(RccSettingDlg)
        self.pushButton_del_item.setObjectName(u"pushButton_del_item")

        self.gridLayout.addWidget(self.pushButton_del_item, 2, 3, 1, 1)


        self.retranslateUi(RccSettingDlg)

        QMetaObject.connectSlotsByName(RccSettingDlg)
    # setupUi

    def retranslateUi(self, RccSettingDlg):
        RccSettingDlg.setWindowTitle(QCoreApplication.translate("RccSettingDlg", u"Dialog", None))
        self.pushButton_ok.setText(QCoreApplication.translate("RccSettingDlg", u"ok", None))
        self.label.setText(QCoreApplication.translate("RccSettingDlg", u"rcc watchers", None))
        self.pushButton__new_item.setText(QCoreApplication.translate("RccSettingDlg", u"new", None))
        self.pushButton_del_item.setText(QCoreApplication.translate("RccSettingDlg", u"del", None))
    # retranslateUi

