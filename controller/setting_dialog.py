from _ast import Global

from PySide6.QtCore import QFile, QFileInfo
from PySide6.QtWidgets import QDialog, QInputDialog, QFileDialog, QMessageBox

from tools import GlobalValues

from view.qt_py_ui_files.setttings_dialog import Ui_settings_dialog

#动态创建的setting dialog
class SettingDialog(QDialog):
    def __init__(self,project):
        super().__init__()
        self.project = project
        self.ui = Ui_settings_dialog()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.refreshUiByProject()
        def getPath(lineEdit):
            filePath, _ = QFileDialog.getOpenFileName(self, "select your file")
            print(filePath)
            self.ui.lineEdit_4.setText(filePath)
            print(_)
        self.ui.pushButton_27.clicked.connect(lambda: getPath(self.ui.lineEdit_4))
        self.ui.pushButton_28.clicked.connect(lambda: getPath(self.ui.lineEdit_8))
        self.ui.pushButton_29.clicked.connect(lambda: getPath(self.ui.lineEdit_5))
        self.ui.pushButton_30.clicked.connect(lambda: getPath(self.ui.lineEdit_6))
        self.ui.pushButton_31.clicked.connect(lambda: getPath(self.ui.lineEdit_7))

        def ok():
            self.refreshProjectByUi()
            self.accept()

        self.ui.pushButton_18.clicked.connect(ok)
    def refreshProjectByUi(self):
        self.project.pyside6_uic_path = self.ui.lineEdit_4.text()
        self.project.pyside6_rcc_path = self.ui.lineEdit_8.text()
        self.project.pyside6_designer_path = self.ui.lineEdit_6.text()
        self.project.pyside6_linguist_path = self.ui.lineEdit_5.text()
        self.project.pyside6_assistant_path = self.ui.lineEdit_7.text()
        pass
        #参数
        uicParaList =  self.ui.lineEdit_22.text().split(",")
        paras =  " ".join(uicParaList)
        self.project.uic_run_paras = paras
        pass
        rccParaList = self.ui.lineEdit_21.text().split(",")
        paras = " ".join(rccParaList)
        self.project.rcc_run_paras = paras
        GlobalValues.settingManager.save()
    def refreshUiByProject(self):
        pass
        self.ui.lineEdit_4.setText(self.project.pyside6_uic_path)
        self.ui.lineEdit_8.setText(self.project.pyside6_rcc_path)
        self.ui.lineEdit_6.setText(self.project.pyside6_designer_path)
        self.ui.lineEdit_5.setText(self.project.pyside6_linguist_path)
        self.ui.lineEdit_7.setText(self.project.pyside6_assistant_path)
