import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

qt_ui_file_path = r"aaaaa"
qt_py_ui_path = r"pyaaaaa"
qt_pyside6_uic_path = ""
if __name__ == '__main__':
    #检查文件夹是不是存在的
    # if not os.path.exists(qt_ui_file_path):
    #     os.mkdir(qt_ui_file_path)
    #     pass
    # if not os.path.exists(qt_py_ui_path):
    #     os.mkdir(qt_py_ui_path)
    #     pass


    app = QApplication(sys.argv)
    uiLoader = QUiLoader()
    mainWindow = uiLoader.load(r"qt_ui_files/main_window.ui")
    mainWindow.show()
    sys.exit(app.exec())
