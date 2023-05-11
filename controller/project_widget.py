from PySide6.QtWidgets import QWidget, QMessageBox, QListWidgetItem, QDialog, QListWidget

from file_watch_handler import FileWatchHelper
from setting_dialog import SettingDialog
from view.qt_py_ui_files.ui_project_widget import Ui_ProjectWidget

from model.setting_manager import Setting, Project, SettingManager


#还没用到这个文件袋额
class ProjectWidget(QWidget):
    def __init__(self,project):
        super().__init__()
        self.ui = Ui_ProjectWidget()
        self.ui.setupUi(self)
        self.project = project
        self.settingManager = SettingManager()
        self.item :QListWidgetItem = QListWidgetItem()
        self.item.widget = self
        self.setNewProjectMode(False)
        self.mainwindow = None

    def initConnects(self):
        #初始化信号槽
        #lineedits
        lineEdits =  [self.ui.lineEdit_9,self.ui.lineEdit_6,self.ui.lineEdit_5,self.ui.lineEdit_8,\
                      self.ui.lineEdit_12,self.ui.lineEdit_16,self.ui.lineEdit_15]
        for l in lineEdits:
            l.editingFinished.connect(lambda: self.refreshProjectByUiAndSave())
        self.ui.lineEdit.editingFinished.connect(self.onProjectNameChanged)
        #commboboxs
        self.ui.checkBox.stateChanged.connect(lambda: self.refreshProjectByUiAndSave())
        self.ui.checkBox_2.stateChanged.connect(lambda: self.refreshProjectByUiAndSave())
        #pushbuttons
        self.ui.pushButton_9.clicked.connect(self.onShowSettingPanel)
        self.ui.pushButton_6.clicked.connect(lambda: self.runProject())

        pass
    def applyNewProject(self):
        print("applyNewProject")
        #新建一个项目
        self.refreshProjectByUiAndSave()
        self.settingManager.setting.projects.append(self.project)
        self.item.setText(self.project.name)
        self.mainwindow.ui.listWidget.addItem(self.item)
        self.mainwindow.isAddingProject = False
        self.close()
        self.mainwindow.ui.stackedWidget.addWidget(self)
        self.mainwindow.ui.stackedWidget.setCurrentWidget(self)
        self.setNewProjectMode(False)
        self.settingManager.save()
        self.item.setSelected(True)
        pass
    def cancelNewProject(self):
        #取消新建一个项目
        print("cancelNewProject")
        pass

    def setNewProjectMode(self,isNewProjectMode = False):
        #设置新建项目模式
        if not isNewProjectMode:
            self.ui.pushButton_10.setVisible(False)
            self.ui.pushButton_12.setVisible(False)

        else:
            self.ui.pushButton_12.setVisible(True)
            self.ui.pushButton_10.setVisible(True)
            self.ui.pushButton_10.clicked.connect(self.applyNewProject)
            self.ui.pushButton_12.clicked.connect(self.cancelNewProject)

    def onShowSettingPanel(self):
        # 显示项目的设置面板
        settingDialog = SettingDialog(self.project)
        res = settingDialog.exec()
        if res == QDialog.Accepted:
            #TODO 设置面板的设置之后
            pass
    def runProject(self):
        # 运行项目
        if self.project.isUicEnable:
            fileWatchHelper = FileWatchHelper(self.project)
            fileWatchHelper.startFileWatch()
            self.log("uic watcher run successfully!")
        pass
    def onProjectNameChanged(self):
        print(self.project)
        # 当项目的名字改变的时候
        if not self.mainwindow.isAddingProject:
            # 查找self.ui.listwidget里面的item有没有这个widget，但是不要查找自身
            for index in range(0, self.mainwindow.ui.listWidget.count()):
                if self.mainwindow.ui.listWidget.item(index).widget is self:
                    continue
                if self.mainwindow.ui.listWidget.item(index).text() == self.ui.lineEdit.text():
                    QMessageBox.information(self, "info", "project name is already exist")
                    self.ui.lineEdit.setText(self.project.name)
                    pass
                else:
                    self.project.name = self.ui.lineEdit.text()
                    self.item.setText(self.project.name)
                    self.settingManager.save()
                    pass

    def refreshUiByProjcet(self):
        # 通过project得到widget的实例
        self.ui.lineEdit_5.setText(self.project.ui_in_dir)
        self.ui.lineEdit_8.setText(self.project.ui_out_dir)
        self.ui.lineEdit_6.setText(self.project.qrc_in_dir)
        self.ui.lineEdit_9.setText(self.project.qrc_out_dir)
        self.ui.lineEdit_12.setText(self.project.pyside6_assistant_path)
        self.ui.lineEdit_16.setText(self.project.pyside6_linguist_path)
        self.ui.lineEdit_15.setText(self.project.pyside6_designer_path)
        self.ui.checkBox.setChecked(self.project.isUicEnable)
        self.ui.checkBox_2.setChecked(self.project.isRccEnable)
        self.ui.lineEdit.setText(self.project.name if self.project.name != "" else "project name")
        return self

    def refreshProjectByUiAndSave(self):
        self.project.ui_in_dir = self.ui.lineEdit_5.text()
        self.project.ui_out_dir = self.ui.lineEdit_8.text()
        self.project.qrc_in_dir = self.ui.lineEdit_6.text()
        self.project.qrc_out_dir = self.ui.lineEdit_9.text()
        self.project.pyside6_assistant_path = self.ui.lineEdit_12.text()
        self.project.pyside6_linguist_path = self.ui.lineEdit_16.text()
        self.project.pyside6_designer_path = self.ui.lineEdit_15.text()
        self.project.name = self.ui.lineEdit.text()
        self.project.isUicEnable = self.ui.checkBox.isChecked()
        self.project.isRccEnable = self.ui.checkBox_2.isChecked()
        self.settingManager.save()

    def log(self,msg):
        if self.ui.listWidget_2.count()>100:
            self.ui.listWidget_2.removeItemWidget(self.ui.listWidget_2.item(self.ui.listWidget_2.count()-1))
            self.project.logs.remove(self.project.logs[-1])
        self.ui.listWidget_2.insertItem(0, QListWidgetItem(msg))
        self.project.logs.append(msg)