from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QDialog, QMessageBox, \
    QListWidgetItem, QInputDialog, QLineEdit

from controller.file_watch_handler import FileWatchHelper
from controller.setting_dialog import SettingDialog
from model.setting_manager import Project, SettingManager
from project_widget import ProjectWidget
from tools import singleton
from view.qt_py_ui_files.main_window import Ui_MainWindow
from view.qt_py_ui_files.setttings_dialog import Ui_settings_dialog
from view.qt_py_ui_files.ui_project_widget import Ui_ProjectWidget

@singleton
class MainWindow(QMainWindow):
#单例
    def __init__(self):
        super().__init__()
        # 控制的对象
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settingManager = SettingManager()
        self.isAddingProject = False
        # 现在是不是在添加一个新的项目中
        self.init()
    def showAddProjectDialog(self):
        #新建项目面板弹出
        self.isAddingProject = True
        project =  Project()
        widget = ProjectWidget(project)
        widget.mainwindow = self
        widget.setNewProjectMode(True)
        widget.setWindowModality(Qt.WindowModality.ApplicationModal)
        widget.show()
        pass



    def init(self):
        self.settingManager.load()
        self.ui.listWidget.doubleClicked.connect(self.onListWidgetItemDoubleClicked)
        self.ui.pushButton_35.clicked.connect(self.showAddProjectDialog)
        print(self.settingManager.setting.projects)
        #加载所有的项目
        for project in self.settingManager.setting.projects:
            project.pyside6_uic_path = r"C:\Users\EPR\.virtualenvs\pyside6-helper-pP3pfM4F\Scripts\pyside6-uic.exe"
            project.isUicEnable = True
            widget = ProjectWidget(project)
            widget.refreshUiByProjcet()
            widget.initConnects()
            widget.item.setText(project.name)
            widget.mainwindow  = self
            self.ui.listWidget.addItem(widget.item)
    def onListWidgetItemDoubleClicked(self, index: QListWidgetItem):
        # 先看看item代表的widget在stackwidget里面是不是存在的，存在就直接显示 不存在再放上去
        item = self.ui.listWidget.item(index.row())
        print(f"clicked! {item.text()}")
        self.ui.stackedWidget.addWidget(item.widget)
        self.ui.stackedWidget.setCurrentWidget(item.widget)



    def findListWidgetItemByProjectWidget(self, widget: QWidget):
        # 由于使用listwidgetitem的widgetref属性存下QWidget
        for index in range(0, self.ui.listWidget.count()):
            if self.ui.listWidget.item(index).widgetRef is widget:
                return self.ui.listWidget.item(index)
                pass
    def findProjectItemByName(self, name: str):
        # 通过name查找Project在ui。listwidget里面的item是不是已经存在
        for i in range(0, self.ui.listWidget.count()):
            if self.ui.listWidget.item(i).text() == name:
                return self.ui.listWidget.item(i)
        return None
        pass
