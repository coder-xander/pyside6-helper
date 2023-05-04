import os

from PySide6.QtWidgets import QApplication
import sys
from model.app_data import AppData
from controller import file_watch_handler
from tools import find_file_by_filename
from view.views import main_window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = main_window.MainWindow()
    appData = AppData()
    # myselfDir =  os.path.dirname(script_path)
    # script_path = os.path.abspath(__file__)#脚本所在的路径

    # all_pyside6_uic = find_file_by_filename("pyside6-uic.exe")
    # for item in all_pyside6_uic:
    #     print(item)
    # 设置配置文件
    # 如果两个数组全部相同，则返回 -1
    # 将输入路径中的斜杠替换为系统默认的路径分隔符


    appData.save()
    appData.load()
    fileWatchHelper = file_watch_handler.fileWatchHelper()
    fileWatchHelper.startFileWatch()
    mainWindow.show()
    sys.exit(app.exec())
