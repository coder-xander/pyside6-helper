import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
import sys
import app_data
import file_watch_handler
from tools import find_file_by_filename
from views import  main_window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window =  main_window.MainWindow()
    app_config  =  app_data.AppData()
    # script_path = os.path.abspath(__file__)#脚本所在的路径
    # myselfDir =  os.path.dirname(script_path)

    # all_pyside6_uic = find_file_by_filename("pyside6-uic.exe")
    # for item in all_pyside6_uic:
    #     print(item)
    #设置配置文件
    app_config.setData(  {
            "path_info": {
                "qt_ui_file_path": r"C:\Users\EPR\Documents\xander\github\pyside-auto-c\qt_ui_files",
                "qt_py_ui_path": r"C:\Users\EPR\Documents\xander\github\pyside-auto-c\qt_py_ui_files",
                "qt_pyside6_uic_path": "\\Users\\oct-x\\.virtualenvs\\pyside6-assistant-11h-AmLd\\Scripts\\pyside6-uic.exe",
                "qt_pyside6_rcc_path": None,
            }
        })
    app_config.save()
    app_config.load()
    file_watch_helper =  file_watch_handler.fileWatchHelper()
    file_watch_helper.startFileWatch()
    main_window.show()
    sys.exit(app.exec())
