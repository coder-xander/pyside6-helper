import os
import threading
import joblib
from PySide6.QtCore import QTimer
from PySide6.QtCore import QObject
import tools

g_save_file_name = "pyside6-helper-setting.pyh"
class Project:
    def __init__(self):
        self.ui_in_dir = ""
        self.ui_out_dir = ""
        self.uic_run_paras = ""
        self.rcc_run_paras = ""
        self.qrc_in_dir = ""
        self.qrc_out_dir = ""
        self.pyside6_uic_path = ""
        self.pyside6_rcc_path = ""
        self.pyside6_assistant_path = ""
        self.pyside6_linguist_path = ""
        self.pyside6_designer_path = ""
        self.logs = []
        self.name = ""
        self.isRunning = False
        self.isUicEnable = False
        self.isRccEnable = False

    def isVaild(self):
        res = os.path.isdir(self.ui_in_dir) and \
              os.path.isdir(self.ui_out_dir) and \
              os.path.isfile(self.pyside6_uic_path) and \
              self.name != ""
        return res
        # 配置文件

    def isProjecUicRunable(self):
        # 项目配置是不是可以启动uic监控
        if not os.path.isfile(self.pyside6_uic_path):
            return False, self.pyside6_uic_path
        if not os.path.isdir(self.ui_in_dir):
            return False, self.ui_in_dir
        if not os.path.isdir(self.ui_out_dir):
            return False, self.ui_out_dir
        return True, None


class Setting:
    def __init__(self):
        self.save_timer = None
        self.setting_name = ""
        self.projects: list = []


class SettingManager(QObject):
    # 线程安全的单例
    def __init__(self):
        super().__init__()
        self.file_save_lock = threading.Lock()
        self.setting = Setting()

    def clearProjects(self):
        self.setting.projects = []
        self.save()

    def save(self):
        script_path = os.path.abspath(__file__)
        # 获取当前脚本文件所在的目录
        script_dir = os.path.dirname(script_path)
        with self.file_save_lock:
            joblib.dump(self.setting, f'{script_dir}\{g_save_file_name}')
            names = []
            for p in self.setting.projects:
                names.append(p.name)
            print(f"save--{names}")
        return self

    def load(self):
        print("load setting file")
        with self.file_save_lock:
            script_path = os.path.abspath(__file__)
            # 获取当前脚本文件所在的目录
            script_dir = os.path.dirname(script_path)
            file_path = f'{script_dir}\{g_save_file_name}'
            if not os.path.exists(file_path):
                with open(file_path, 'w'):
                    pass
            self.setting = joblib.load(file_path)
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
