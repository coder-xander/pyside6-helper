import os.path
import subprocess

from PySide6.QtCore import  QObject
from watchdog.events import FileSystemEventHandler
from watchdog import observers

from model import app_data


# def syncDirBetweenTwoDir(targetDir, rawDir, reverse=False):
#     """
#     在 a 文件夹下检查是否有 b 文件夹下的所有文件夹，没有的则创建。
#     如果 reverse 为 True，则同时删除 a 文件夹下多余的文件夹。
#     """
#     # 遍历 b 文件夹下所有子文件夹
#     for root, dirs, _ in os.walk(rawDir):
#         # 获取对应的 a 文件夹下的路径
#         rel_path = os.path.relpath(root, rawDir)
#         a_dir_path = os.path.join(targetDir, rel_path)
#
#         # 如果在 a 目录下不存在对应的子文件夹，就创建它
#         if not os.path.exists(a_dir_path):
#             os.makedirs(a_dir_path)
#
#         # 如果 reverse 为 True，且 a 目录中存在 b 目录中不存在的文件夹，就删除它
#         if reverse and rel_path and not os.path.exists(os.path.join(rawDir, rel_path)):
#             shutil.rmtree(a_dir_path)
#
#     # 如果 reverse 为 True，且 a 目录中存在 b 目录中不存在的文件夹，就删除它
#     if reverse:
#         for root, dirs, _ in os.walk(targetDir):
#             rel_path = os.path.relpath(root, targetDir)
#             if rel_path and not os.path.exists(os.path.join(rawDir, rel_path)):
#                 shutil.rmtree(root)
def fileInFilter(fileName):
    return fileName.split(".")[-1] in ["ui"]
def renameFileSuffix(uiFilename, suffixName):
    nameList  =uiFilename.split(".")
    nameList[-1] = suffixName
    return ".".join(nameList)

class fileWatchHandle(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.appConfig= app_data.AppData()

    def getReflectPathFromRawPath(self,rawPath,isDir=False):
        fileDirAndName = os.path.split(rawPath)
        dir = fileDirAndName[0]
        for i in range(len(dir)):
            if dir[i] == self.appConfig.data["path_info"]["qt_ui_file_path"].split("\\")[-1]:
                dir[i] = self.appConfig.data["path_info"]["qt_py_ui_path"].split("\\")[-1]
                break
                pass
        name = fileDirAndName[1]
        if not fileInFilter(name):
            return None
        name = renameFileSuffix(name, "py")
        return os.path.join(dir, name)
    def on_created(self, event):
        print(f"new file {event.src_path}")
        if event.is_directory:
            print("新文件夹")
            return
        path = self.getReflectPathFromRawPath(event.src_path)
        if path is None:
            return

        result =  subprocess.run([self.appConfig.data["path_info"]["qt_pyside6_uic_path"],"-o",path],capture_output=True,text=True)
        print(result.stdout)
        if result.returncode == 0:
            print("编译成功")
        pass
    def on_deleted(self, event):
        print(f"delete file {event.src_path}")
        pass
    def on_moved(self, event):
        pass
    def on_closed(self, event):
        pass

    def on_modified(self, event):
        pass


class fileWatchHelper(QObject):
    def __init__(self):
        self.observer = observers.Observer()
        self.appData = app_data.AppData()
        pass
    def startFileWatch(self):
        self.observer = observers.Observer()
        self.observer.schedule(fileWatchHandle(),path=self.appData.data["path_info"]["qt_ui_file_path"],recursive=True)
        self.observer.start()
        pass

    def stopFileWatch(self):
        self.observer.stop()
        self.observer.join()
        pass
    def restartFileWatch(self):
        self.startFileWatch()
        self.stopFileWatch()
        pass