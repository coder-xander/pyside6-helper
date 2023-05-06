from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QDialog, QMessageBox

from model.setting_manager import Project
from view.qt_py_ui_files.ui_main_window import Ui_MainWindow
from view.qt_py_ui_files.ui_project_widget import Ui_ProjectSetting


class MainWindowController:
    def __init__(self, ui):
        # 控制的对象
        self.ui: Ui_MainWindow = ui

        # 现在是不是在添加一个新的项目中
        self.isAddingProjectFlag = False


    def showAddProjectDialog(self):
        # 初始化一个空widget进行收集项目的信息
        dialogUi = Ui_ProjectSetting()
        dialog = QDialog()
        dialog.ui = dialogUi
        dialogUi.setupUi(dialog)
        saveBtn = QPushButton()
        saveBtn.setText("save")
        saveBtn.setProperty("func", "save")
        cancelBtn = QPushButton()
        cancelBtn.setText("cancel")
        cancelBtn.setProperty("func", "cancel")
        dialogUi.widget_3.layout().addWidget(saveBtn)
        dialogUi.widget_3.layout().addWidget(cancelBtn)
        # dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        def onSaveBtnClicked():
            #读取界面信息
            project =  Project()
            project.in_ui_files_dir =  dialog.ui.lineEdit_5.text()
            project.out_py_files_dir =  dialog.ui.lineEdit_6.text()
            project.pyside6_uic_path = dialog.ui.lineEdit_8.text()
            project.pyside6_rcc_path = dialog.ui.lineEdit_9.text()
            project.pyside6_assistant_path = dialog.ui.lineEdit_12.text()
            project.pyside6_linguist_path = dialog.ui.lineEdit_16.text()
            project.pyside6_designer_path = dialog.ui.lineEdit_15.text()
            project.name = dialog.ui.pushButton_5.text()
            if not project.isVaild():
                QMessageBox.information(dialog, "info", "Project info is not complete")
                return
            self.addOneProject(project)
            QMessageBox.information(dialog,"info","add success")
            #构造Project对象
            pass
        def onCancelBtnClicked():
            dialog.close()
            pass
        saveBtn.clicked.connect(onSaveBtnClicked)
        cancelBtn.clicked.connect(onCancelBtnClicked)
        dialog.exec()

    def run(self):
        if self.ui is None:
            raise "control target is none"
        # 新建一个项目
        self.ui.pushButton_35.clicked.connect(self.showAddProjectDialog)

    def addOneProject(self, project: Project):
        #添加到界面
        #序列化到文件
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
