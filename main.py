import copy

import qdarkstyle
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from main_window import MainWindow
from model.setting_manager import SettingManager, Project
from controller.file_watch_handler import FileWatchHelper
from view.qt_py_ui_files.main_window import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # SettingManager().clearProjects()
    # SettingManager().save()
    mainwindow = MainWindow()
    mainwindow.setWindowTitle("pyside helper")
    # mainwindow.setWindowIconText(QIcon())
    # mainwindow.show()
    # mainwindow.raise_()
    mainwindow.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    app.exec_()
    # 添加一个项目
    # newProject = Project()
    # newProject.name = "auto c"
    # newProject.qt_ui_dir = r"C:\Users\EPR\Documents\xander\github\pyside6-helper\view\qt_ui_files"
    # newProject.qt_py_ui_dir = r"C:\Users\EPR\Documents\xander\github\pyside6-helper\view\qt_py_ui_files"
    # newProject.pyside6_uic_path = r"C:\Users\EPR\.virtualenvs\pyside6-helper-pP3pfM4F\Scripts\pyside6-uic.exe"
    # mainWindowController.addOneProject(newProject)

    # myselfDir =  os.path.dirname(script_path)
    # script_path = os.path.abspath(__file__)#脚本所在的路径

    # all_pyside6_uic = find_file_by_filename("pyside6-uic.exe")
    # for item in all_pyside6_uic:
    #     print(item)
    # 设置配置文件
    # 如果两个数组全部相同，则返回 -1
    # 将输入路径中的斜杠替换为系统默认的路径分隔符

