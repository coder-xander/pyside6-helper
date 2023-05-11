import copy
import os.path

import qdarkstyle
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from tools import GlobalValues
from main_window import MainWindow
from model.setting_manager import SettingManager, Project
from view.qt_py_ui_files.main_window import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GlobalValues.settingManager = SettingManager()
    mainwindow = MainWindow()
    GlobalValues.mainwindow = mainwindow
    mainwindow.setWindowTitle("pyside helper")
    mainwindow.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    #---------------------------------------------------------test---------------------------
    #---------------------------------------------------------test---------------------------

    app.exec()


