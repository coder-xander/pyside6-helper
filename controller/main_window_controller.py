from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton

from setting_manager import Project
from view.qt_py_ui_files.ui_main_window import Ui_MainWindow
from view.qt_py_ui_files.ui_project_widget import Ui_ProjectSetting


class MainWindowController:
    def __init__(self, ui):
        # 控制的对象
        self.ui: Ui_MainWindow = ui
        # 现在是不是在添加一个新的项目中
        self.isAddingProjectFlag = False
        # 初始化一个空widget进行收集项目的信息
        blankWidgetUi = Ui_ProjectSetting()
        widget = QWidget()
        self.forNewProjectWidget: QWidget = widget
        blankWidgetUi.setupUi(widget)
        saveBtn = QPushButton()
        saveBtn.setText("save")
        saveBtn.setProperty("func", "save")
        cancelBtn = QPushButton()
        cancelBtn.setText("cancel")
        cancelBtn.setProperty("func", "cancel")
        blankWidgetUi.widget_3.layout().addWidget(saveBtn)
        blankWidgetUi.widget_3.layout().addWidget(cancelBtn)
        self.ui.stackedWidget.addWidget(widget)
        self.forNewProjectWidget.hide()

    def run(self):
        if self.ui is None:
            raise "control target is none"
        # 新建一个项目
        self.ui.pushButton_35.clicked.connect(self.uiAddOneProject)

    def uiAddOneProject(self):
        if self.forNewProjectWidget is not None:
            self.ui.stackedWidget.setCurrentWidget(self.forNewProjectWidget)
            self.forNewProjectWidget.show()
        else:
            raise "error"

    def addOneProject(self, project: Project):
        self.ui.stackedWidget.removeWidget(self.ui.stackedWidget.widget(0))
        newProjectUi = Ui_ProjectSetting()
        widget = QWidget()
        newProjectUi.setupUi(widget)
        self.ui.stackedWidget.addWidget(widget)
        widget.show()
        newProjectUi.lineEdit_5.setText(project.pyside6_uic_path)
        self.ui.stackedWidget.setCurrentIndex(0)

        print("dsds")
        pass
