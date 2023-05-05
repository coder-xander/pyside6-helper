from PySide6.QtWidgets import QMainWindow, QWidget

from view.qt_py_ui_files.ui_main_window import Ui_MainWindow
from view.qt_py_ui_files.ui_project_widget import Ui_ProjectSetting


class MainWindowController:
    def __init__(self):
        #控制的对象
        self.ui : Ui_MainWindow = None
    def run(self):
        if self.ui is None:
            raise "control target is none"
        #新建一个项目
        self.ui.pushButton_35.clicked.connect(self.newProject)
    def newProject(self,project):
        newProjectUi =  Ui_ProjectSetting()
        widget = QWidget()
        newProjectUi.setupUi(widget)
        self.ui.stackedWidget.addWidget(widget)
        widget.show()
        widget.raise_()
        newProjectUi.lineEdit_5.setText(project.pyside6_uic_path)
        self.ui.stackedWidget.setCurrentIndex(0)

        print("dsds")
        pass

