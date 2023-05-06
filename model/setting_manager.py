import os
import pickle
import threading
from PySide6.QtCore import QTimer
import orjson
from PySide6.QtCore import QObject
import tools

g_save_file_name = "pyside6-helper-setting.pyh"


class Project:
    def __init__(self):
        self.in_ui_files_dir = ""
        self.out_py_files_dir = ""
        self.pyside6_uic_path = ""
        self.pyside6_rcc_path = ""
        self.pyside6_assistant_path = ""
        self.pyside6_linguist_path = ""
        self.pyside6_designer_path = ""
        self.logs = []
        self.name = ""
        self.isRunning = False

    def isVaild(self):
        res = os.path.isdir(self.in_ui_files_dir) and \
              os.path.isdir(self.out_py_files_dir) and \
              os.path.isfile(self.pyside6_linguist_path)and \
              os.path.isfile(self.pyside6_assistant_path)and\
              os.path.isfile(self.pyside6_rcc_path)and \
              os.path.isfile(self.pyside6_uic_path)and \
              self.name != ""
        return res
        # 配置文件
class Setting:
    def __init__(self):
        self.save_timer = None
        self.setting_name = ""
        self.projects: list = []


@tools.singleton
class SettingManager(QObject):
    # 线程安全的单例
    def __init__(self):
        super().__init__()
        self.file_save_lock = threading.Lock()
        self.setting = Setting()

    def save(self):
        script_path = os.path.abspath(__file__)
        # 获取当前脚本文件所在的目录
        script_dir = os.path.dirname(script_path)
        with self.file_save_lock:
            with open(f'{script_dir}\{g_save_file_name}', 'wb') as f:
                pickle.dump(self.setting, f, -1)
                print("save file now")
        return self

    def load(self):
        with self.file_save_lock:
            script_path = os.path.abspath(__file__)
            # 获取当前脚本文件所在的目录
            script_dir = os.path.dirname(script_path)
            if not os.path.exists(f'{script_dir}\{g_save_file_name}'):
                with open(f'{script_dir}\{g_save_file_name}', 'w'):
                    pass
            with open(f'{script_dir}\{g_save_file_name}', 'rb') as f:
                self.setting = pickle.load(f)
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
