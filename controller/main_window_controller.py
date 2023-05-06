from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QDialog, QMessageBox, \
    QListWidgetItem, QInputDialog, QLineEdit

from file_watch_handler import FileWatchHelper
from model.setting_manager import Project, SettingManager
from view.qt_py_ui_files.ui_main_window import Ui_MainWindow
from view.qt_py_ui_files.ui_project_widget import Ui_ProjectSetting


class MainWindowController:
    def __init__(self, ui):
        # 控制的对象
        self.settingManager = SettingManager()
        self.ui: Ui_MainWindow = ui
        # 现在是不是在添加一个新的项目中
        self.isAddingProjectFlag = False
        self.initAllProject2Ui()

    def initAllProject2Ui(self):
        self.ui.listWidget.doubleClicked.connect(self.onListWidgetItemDoubleClicked)
        print(self.settingManager.setting.projects)
        for p in self.settingManager.setting.projects:
            widget = self.project2ProjectWidget(p)
            item = QListWidgetItem()
            item.setText(p.name)
            item.widgetRef = widget
            self.ui.listWidget.addItem(item)

    def onListWidgetItemDoubleClicked(self, index: QListWidgetItem):
        # 先看看item代表的widget在stackwidget里面是不是存在的，存在就直接显示 不存在再放上去
        item = self.ui.listWidget.item(index.row())
        print(item.text())
        isExsit = False
        for i in range(0, self.ui.stackedWidget.count()):
            widgetUi: Ui_ProjectSetting = self.ui.stackedWidget.widget(i).ui
            if widgetUi.lineEdit.text() == item.text():
                isExsit = True
                break
        if not isExsit:
            self.ui.stackedWidget.addWidget(item.widgetRef)
        self.ui.stackedWidget.setCurrentWidget(item.widgetRef)

    def refreshProjectList(self):
        allExsitNams = []
        for i in range(0, self.ui.listWidget.count()):
            allExsitNams.append(self.ui.listWidget.item(i).text())
            pass
        for project in self.settingManager.setting.projects:
            # 把listWidget里面不存在的Project放进来
            if project.name in allExsitNams:
                continue
            else:
                widget = self.project2ProjectWidget(project)
                item = QListWidgetItem()
                item.setText(project.name)
                item.widgetRef = widget
                self.ui.listWidget.addItem(item)
                pass

    def updateProjectFromProjectWidget(self, project: Project, projectWidget: QWidget):
        ui:Ui_ProjectSetting = projectWidget.ui
        project.ui_in_dir = ui.lineEdit_5.text()
        project.ui_out_dir = ui.lineEdit_8.text()
        project.qrc_in_dir = ui.lineEdit_6.text()
        project.qrc_out_dir = ui.lineEdit_9.text()
        project.pyside6_assistant_path = ui.lineEdit_12.text()
        project.pyside6_linguist_path = ui.lineEdit_16.text()
        project.pyside6_designer_path = ui.lineEdit_15.text()
        project.name = ui.lineEdit.text()
        project.isUicEnable = ui.checkBox.isChecked()
        project.isRccEnable = ui.checkBox_2.isChecked()
        self.settingManager.save()

    def showAddProjectDialog(self):
        self.isAddingProjectFlag = True
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
        widget.ui.lineEdit.setText("project name")
        widget.setWindowModality(Qt.WindowModality.ApplicationModal)
        pass

        def onSaveBtnClicked():
            # 读取界面信息
            project = Project()
            self.updateProjectFromProjectWidget(project, widget)
            # if not project.isVaild():
            #     QMessageBox.information(dialog, "info", "Project info is not complete")
            #     return

            self.settingManager.setting.projects.append(project)
            # 刷新项目列表
            self.refreshProjectList()
            # 序列化到文件
            self.settingManager.save()
            QMessageBox.information(widget, "info", "add success")
            widget.close()
            self.isAddingProjectFlag = False
            pass

        def onCancelBtnClicked():
            widget.close()
            self.isAddingProjectFlag = False
            pass

        saveBtn.clicked.connect(onSaveBtnClicked)
        cancelBtn.clicked.connect(onCancelBtnClicked)
        widget.show()

    def findListWidgetItemByProjectWidget(self, widget: QWidget):
        # 由于使用listwidgetitem的widgetref属性存下QWidget
        for index in range(0, self.ui.listWidget.count()):
            if self.ui.listWidget.item(index).widgetRef is widget:
                return self.ui.listWidget.item(index)

    def run(self):
        if self.ui is None:
            raise "control target is none"
        # 新建一个项目
        self.ui.pushButton_35.clicked.connect(self.showAddProjectDialog)

    def project2ProjectWidget(self, project: Project):
        WidgetUi = Ui_ProjectSetting()
        widget = QWidget()
        WidgetUi.setupUi(widget)
        widget.ui: Ui_ProjectSetting = WidgetUi
        widget.ui.lineEdit_5.setText(project.ui_in_dir)
        widget.ui.lineEdit_8.setText(project.ui_out_dir)
        widget.ui.lineEdit_6.setText(project.qrc_in_dir)
        widget.ui.lineEdit_9.setText(project.qrc_out_dir)
        widget.ui.lineEdit_12.setText(project.pyside6_assistant_path)
        widget.ui.lineEdit_16.setText(project.pyside6_linguist_path)
        widget.ui.lineEdit_15.setText(project.pyside6_designer_path)
        widget.ui.checkBox.setChecked(project.isUicEnable)
        widget.ui.checkBox_2.setChecked(project.isRccEnable)
        widget.ui.lineEdit.setText(project.name if project.name != "" else "project name")
        widget.ui.pushButton_6.clicked.connect(lambda: runProject(project, widget))

        def onProjectNameChanged():
            # 更改项目的名字
            if not self.isAddingProjectFlag:
                #TODO 查重
                self.updateProjectFromProjectWidget(project, widget)
                item = self.findListWidgetItemByProjectWidget(widget)
                item.setText(project.name)
                pass

        def runProject(project, widget):
            #运行项目
            fileWatchHelper = FileWatchHelper(project)
            fileWatchHelper.startFileWatch()
            print("启动uic成功")
            pass

        widget.ui.pushButton_6.clicked.connect(lambda :runProject)
        widget.ui.lineEdit.editingFinished.connect(onProjectNameChanged)
        widget.ui.lineEdit_5.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_6.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_8.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_12.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_16.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_15.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        pass



        pass
        return widget
