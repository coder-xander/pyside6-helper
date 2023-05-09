from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QDialog, QMessageBox, \
    QListWidgetItem, QInputDialog, QLineEdit

from controller.file_watch_handler import FileWatchHelper
from controller.setting_dialog_controller import SettingDialogController
from model.setting_manager import Project, SettingManager
from view.qt_py_ui_files.main_window import Ui_MainWindow
from view.qt_py_ui_files.setttings_dialog import Ui_settings_dialog
from view.qt_py_ui_files.ui_project_widget import Ui_ProjectSetting


class MainWindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        # 控制的对象
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.settingManager = SettingManager()
        # 现在是不是在添加一个新的项目中
        self.isAddingProjectFlag = False
        self.initAllProject2Ui()

    def initAllProject2Ui(self):
        self.ui.listWidget.doubleClicked.connect(self.onListWidgetItemDoubleClicked)
        print(self.settingManager.setting.projects)
        for p in self.settingManager.setting.projects:
            p.pyside6_uic_path = r"C:\Users\EPR\.virtualenvs\pyside6-helper-pP3pfM4F\Scripts\pyside6-uic.exe"
            p.isUicEnable = True
            widget = self.project2ProjectWidget(p)
            item = QListWidgetItem()
            item.setText(p.name)
            item.widgetRef = widget
            widget.item: QListWidgetItem = item
            self.ui.listWidget.addItem(item)

    def generateQlistwidgetItem(self, projecName):
        pass
        item = QListWidgetItem()
        item.setText(projecName)
        #
        return item

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
                widget.item = item
                self.ui.listWidget.addItem(item)
                pass

    def updateProjectFromProjectWidget(self, project: Project, projectWidget: QWidget):
        ui: Ui_ProjectSetting = projectWidget.ui
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

    # 通过name查找Project在ui。listwidget里面的item是不是已经存在
    def findProjectItemByName(self, name: str):
        for i in range(0, self.ui.listWidget.count()):
            if self.ui.listWidget.item(i).text() == name:
                return self.ui.listWidget.item(i)
        return None

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
            # 判断在self.ui.listWidget里面有没有重名的,有的话就不添加
            if self.findProjectItemByName(project.name) is not None:
                return
            # 添加到setting里面
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
                # 查找self.ui.listwidget里面的item有没有这个widget，但是不要查找自身
                for index in range(0, self.ui.listWidget.count()):
                    if self.ui.listWidget.item(index).widgetRef is widget:
                        continue
                    if self.ui.listWidget.item(index).text() == widget.ui.lineEdit.text():
                        QMessageBox.information(widget, "info", "project name is already exist")
                        widget.ui.lineEdit.setText(project.name)
                        return
                        pass
                self.updateProjectFromProjectWidget(project, widget)
                widget.item.setText(project.name)
                pass

        def runProject(project, widget):
            # 运行一个项目
            isrunable, errorPath = project.isProjecUicRunable()
            if isrunable:
                fileWatchHelper = FileWatchHelper(project)
                fileWatchHelper.startFileWatch()
                print("启动uic成功")
            else:
                QMessageBox.information(widget, "info", "run failed ，project info is not complete！")

        pass

        def onShowSettingPanel():
            # 显示项目的设置面板
            settingDialog = SettingDialogController(project)
            res = settingDialog.exec()
            if res == QDialog.Accepted:
                self.updateProjectFromProjectWidget(project, widget)
                pass

        widget.ui.pushButton_9.clicked.connect(onShowSettingPanel)
        widget.ui.pushButton_6.clicked.connect(lambda: runProject)
        widget.ui.lineEdit.editingFinished.connect(onProjectNameChanged)
        widget.ui.lineEdit_5.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_6.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_9.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_8.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_12.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_16.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.lineEdit_15.editingFinished.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.checkBox.stateChanged.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        widget.ui.checkBox_2.stateChanged.connect(lambda: self.updateProjectFromProjectWidget(project, widget))
        return widget
