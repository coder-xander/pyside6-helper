import os
import threading
from PySide6.QtCore import QTimer
import orjson
from PySide6.QtCore import QObject
import tools


# 配置文件
@tools.singleton
class AppData(QObject):
    @property
    def path_info_str(self):
        return "path_info"
    # ----------------------------------------
    @property
    def qt_py_ui_dir_str(self):
        return "qt_py_ui_dir"
    @property
    def qt_py_ui_dir_path(self) -> str:
        return self.data[self.path_info_str][self.qt_py_ui_dir_str]

    @qt_py_ui_dir_path.setter
    def qt_py_ui_dir_path(self, value):
        self.data[self.path_info_str][self.qt_py_ui_dir_str] = value

    # ----------------------------------------

    @property
    def qt_ui_dir_str(self):
        return "qt_ui_dir"
    @property
    def qt_ui_dir_path(self) -> str:
        return self.data[self.path_info_str][self.qt_ui_dir_str]

    @qt_ui_dir_path.setter
    def qt_ui_dir_path(self, value):
        self.data[self.path_info_str][self.qt_ui_dir_str] = value

    # ----------------------------------------
    @property
    def pyside6_uic_path_str(self):
        return "pyside6_uic_path"
    @property
    def pyside6_uic_path(self) -> str:
        return self.data[self.path_info_str][self.pyside6_uic_path_str]

    @pyside6_uic_path.setter
    def pyside6_uic_path(self, value):
        self.data[self.path_info_str][self.pyside6_uic_path_str] = value

    # ----------------------------------------
    @property
    def pyside6_rcc_path_str(self):
        return "pyside6_rcc_path"

    @property
    def pyside6_rcc_path(self) -> str:
        return self.data[self.path_info_str][self.pyside6_uic_path_str]

    @pyside6_rcc_path.setter
    def pyside6_rcc_path(self, value):
        self.data[self.path_info_str][self.pyside6_uic_path_str] = value

    # ----------------------------------------
    # 线程安全的单例
    def __init__(self):
        super().__init__()
        self.save_timer = None
        self.data = {
            self.path_info_str: {
                self.qt_ui_dir_str: r"C:\Users\EPR\Documents\xander\github\pyside6-helper\view\qt_ui_files",
                self.qt_py_ui_dir_str: r"C:\Users\EPR\Documents\xander\github\pyside6-helper\view\qt_py_ui_files",
                self.pyside6_uic_path_str: r"C:\Users\EPR\.virtualenvs\pyside6-helper-pP3pfM4F\Scripts\pyside6-uic.exe",
                self.pyside6_rcc_path_str: None,
            }
        }
        self.file_save_lock = threading.Lock()

    def setData(self, data):
        self.data = data
        return self

    def save(self):
        if self.data is None:
            raise Exception("没有设置json的文件格式")
        data_bytes = orjson.dumps(self.data)
        # 获取当前脚本文件的绝对路径
        script_path = os.path.abspath(__file__)
        # 获取当前脚本文件所在的目录
        script_dir = os.path.dirname(script_path)
        with self.file_save_lock:
            with open(f'{script_dir}\pysideAssistant.json', 'w') as f:
                f.write(data_bytes.decode('utf-8'))
                print("save file now")
        return self

    def load(self):
        with self.file_save_lock:
            script_path = os.path.abspath(__file__)
            # 获取当前脚本文件所在的目录
            script_dir = os.path.dirname(script_path)
            if not os.path.exists(f'{script_dir}\pysideAssistant.json'):
                with open(f'{script_dir}\pysideAssistant.json', 'w'):
                    pass
            with open(f'{script_dir}\pysideAssistant.json', 'r') as f:
                self.data = orjson.loads(f.read())
                print("load file now")
        return self

    def startAutoSave(self):
        if self.save_timer is None:
            self.save_timer = QTimer()
            self.save_timer.setInterval(1000)
            self.save_timer.timeout.connect(self.save)
            self.save_timer.start()
        else:
            self.save_timer.stop()
            self.save_timer.start()
        pass

    def cacelAutoSave(self):
        if self.save_timer is not None:
            self.save_timer.stop()
        else:
            raise Exception("timer 还没创建")
        pass
