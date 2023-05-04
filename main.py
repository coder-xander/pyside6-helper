from PySide6.QtWidgets import QApplication
import sys
from model import app_data
from controller import file_watch_handler
from tools import find_file_by_filename
from view.views import main_window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow =  main_window.MainWindow()
    appData  =  app_data.AppData()
    # myselfDir =  os.path.dirname(script_path)
    # script_path = os.path.abspath(__file__)#脚本所在的路径

    # all_pyside6_uic = find_file_by_filename("pyside6-uic.exe")
    # for item in all_pyside6_uic:
    #     print(item)
    #设置配置文件
    appData.setData(  {
            "path_info": {
                "qt_ui_file_path": r"C:\Users\EPR\Documents\xander\github\pyside6-helper\view\qt_ui_files",
                "qt_py_ui_path": r"C:\Users\EPR\Documents\xander\github\pyside6-helper\view\qt_py_ui_files",
                "qt_pyside6_uic_path": r"C:\Users\EPR\.virtualenvs\pyside6-helper-pP3pfM4F\Scripts\pyside6-uic.exe",
                "qt_pyside6_rcc_path": None,
            }
        })
    appData.save()
    appData.load()
    fileWatchHelper =  file_watch_handler.fileWatchHelper()
    fileWatchHelper.startFileWatch()
    mainWindow.show()
    sys.exit(app.exec())
