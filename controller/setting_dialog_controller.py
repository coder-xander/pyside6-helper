from PySide6.QtWidgets import QDialog

from view.qt_py_ui_files.setttings_dialog import Ui_settings_dialog


class SettingDialogController(QDialog):
    def __init__(self):
        self.ui = Ui_settings_dialog()
        dialog = QDialog()
        self.ui.setupUi(self)
    def outputInfoToProject(self,project):
        pass
