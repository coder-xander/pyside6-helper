from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QDialog, QMessageBox, QListWidgetItem, QInputDialog

from model.setting_manager import Project, SettingManager
from view.qt_py_ui_files.ui_main_window import Ui_MainWindow
from view.qt_py_ui_files.ui_project_widget import Ui_ProjectSetting


class MainWindowController:
    def __init__(self, ui):
        # 控制的对象
        self.ui: Ui_MainWindow = ui
        # 现在是不是在添加一个新的项目中
        self.isAddingProjectFlag = False
        self.initAllProject2Ui()

    def initAllProject2Ui(self):
        self.ui.listWidget.doubleClicked.connect(self.onListWidgetItemDoubleClicked)
        settingManager = SettingManager()
        print(settingManager.setting.projects)
        for p in settingManager.setting.projects:
            widget = self.project2ProjectWidget(p)
            self.ui.listWidget.addItem(p.name)

    def onListWidgetItemDoubleClicked(self, item: QListWidgetItem):
        for i in range(0, self.ui.stackedWidget.count()):
            ui: Ui_ProjectSetting = self.ui.stackedWidget.widget(i).ui
            if ui.pushButton_5.text() == item.text():
                self.ui.stackedWidget.setCurrentIndex(i)

    def showAddProjectDialog(self):
        # 初始化一个空widget进行收集项目的信息
        widget = self.project2ProjectWidget(Project())

        saveBtn = QPushButton()
        saveBtn.setText("save")
        saveBtn.setProperty("func", "save")
        cancelBtn = QPushButton()
        cancelBtn.setText("cancel")
        cancelBtn.setProperty("func", "cancel")
        widget.ui.widget_3.layout().addWidget(saveBtn)
        widget.ui.widget_3.layout().addWidget(cancelBtn)

        # dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        def onSaveBtnClicked():
            # 读取界面信息
            project = Project()
            project.in_ui_files_dir = widget.ui.lineEdit_5.text()
            project.out_py_files_dir = widget.ui.lineEdit_6.text()
            project.pyside6_uic_path = widget.ui.lineEdit_8.text()
            project.pyside6_rcc_path = widget.ui.lineEdit_9.text()
            project.pyside6_assistant_path = widget.ui.lineEdit_12.text()
            project.pyside6_linguist_path = widget.ui.lineEdit_16.text()
            project.pyside6_designer_path = widget.ui.lineEdit_15.text()
            project.name = widget.ui.pushButton_5.text()
            # if not project.isVaild():
            #     QMessageBox.information(dialog, "info", "Project info is not complete")
            #     return
            self.addOneProject(project)
            QMessageBox.information(widget, "info", "add success")
            widget.ui.close()
            # 构造Project对象
            pass

        def onCancelBtnClicked():
            widget.ui.close()
            pass

        saveBtn.clicked.connect(onSaveBtnClicked)
        cancelBtn.clicked.connect(onCancelBtnClicked)
        widget.show()

    def run(self):
        if self.ui is None:
            raise "control target is none"
        # 新建一个项目
        self.ui.pushButton_35.clicked.connect(self.showAddProjectDialog)

    def addOneProject(self, project):
        # 添加到界面
        widget = self.project2ProjectWidget(project)
        self.ui.stackedWidget.addWidget(widget)
        self.ui.stackedWidget.setCurrentWidget(widget)
        # 序列化到文件
        settingManager = SettingManager()
        settingManager.setting.projects.append(project)
        settingManager.save()

    def project2ProjectWidget(self, project: Project):
        WidgetUi = Ui_ProjectSetting()
        widget = QWidget()
        WidgetUi.setupUi(widget)
        widget.ui: Ui_ProjectSetting = WidgetUi
        widget.ui.lineEdit_5.setText(project.in_ui_files_dir)
        widget.ui.lineEdit_6.setText(project.out_py_files_dir)
        widget.ui.lineEdit_8.setText(project.pyside6_uic_path)
        widget.ui.lineEdit_9.setText(project.pyside6_rcc_path)
        widget.ui.lineEdit_12.setText(project.pyside6_assistant_path)
        widget.ui.lineEdit_16.setText(project.pyside6_linguist_path)
        widget.ui.lineEdit_15.setText(project.pyside6_designer_path)
        widget.ui.pushButton_5.setText(project.name)

        def onProjecNameBtnClicked():
            projectName = QInputDialog.getText(widget, "input project name", "project name")

        widget.ui.pushButton_5.clicked.connect(onProjecNameBtnClicked)
        return widget
