from PySide6.QtWidgets import QWidget, QMessageBox

from model.global_status import GlobalStatus
from view.qt_py_ui_files.ui_project_widget import Ui_ProjectSetting

from model.setting_manager import Setting,Project
#还没用到这个文件袋额
class ProjectWidget(QWidget):
    def __init__(self,project,item):
        super().__init__()
        self.ui = Ui_ProjectSetting()
        self.ui.setupUi(self)
        pass

    @staticmethod
    def getNewWidgetInstanceByProject(project:Project):
        #通过project得到widget的实例
        widget =  ProjectWidget()
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
    def onProjectNameChanged(self):
        # 更改项目的名字
        if not GlobalStatus.isAddingProject:
            # 查找self.ui.listwidget里面的item有没有这个widget，但是不要查找自身
            for index in range(0, self.ui.listWidget.count()):
                if self.ui.listWidget.item(index).widgetRef is self:
                    continue
                if self.ui.listWidget.item(index).text() == widget.ui.lineEdit.text():
                    QMessageBox.information(self, "info", "project name is already exist")
                    self.ui.lineEdit.setText(self.name)
                    return
                    pass
            self.updateProjectFromProjectWidget(project, widget)
            self.item.setText(project.name)
            pass