from PySide6.QtWidgets import QWidget, QMainWindow
from qt_py_ui_files import ui_main_window


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow,self).__init__()
    self.ui = ui_main_window.Ui_MainWindow()
    self.ui.setupUi(self)
    pass