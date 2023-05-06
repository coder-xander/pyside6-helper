import copy

from PySide6.QtWidgets import QApplication, QMainWindow
import sys

from controller.main_window_controller import MainWindowController
from model.setting_manager import SettingManager, Project
from controller import file_watch_handler
from view.qt_py_ui_files.ui_main_window import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    settingManager = SettingManager()
    settingManager.load()

    mainWindow = QMainWindow()
    uiMainwindow = Ui_MainWindow()
    uiMainwindow.setupUi(mainWindow)
    mainWindowController = MainWindowController(uiMainwindow)
    mainWindowController.run()

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
    # settingManager.setting.projects=[]
    settingManager.save()
    fileWatchHelper = file_watch_handler.fileWatchHelper()
    fileWatchHelper.startFileWatch()
    mainWindow.show()
    sys.exit(app.exec())
