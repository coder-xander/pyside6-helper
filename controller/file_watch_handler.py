import os.path
import subprocess

from PySide6.QtCore import QObject
from watchdog.events import FileSystemEventHandler
from watchdog import observers

from model.setting_manager import SettingManager, Project


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


class FileWatchHandle(FileSystemEventHandler):
    def __init__(self, project,projectWidget):
        super().__init__()
        self.project = project
        self.projectWidget = projectWidget
        self.appConfig: SettingManager = SettingManager()

    def uicCompile(self,uiFile,pyFile):
        result = subprocess.run([self.project.pyside6_uic_path, uiFile, "-o", pyFile], capture_output=True,
                                text=True)
        print(result.stdout)
        dirname ,filename =  os.path.split(uiFile)
        if result.returncode == 0:
            self.projectWidget.log(f"compile {filename} done.")

    def isPassFileter(self,path:str):
        filterList = [".ui"]
        for i in filterList:
            if path.endswith(i):
                return True
    def getVirtualPathByUiInPathRelatedPyOutPath(self,rawpath):
        relNewFilePath = os.path.relpath(rawpath, self.project.ui_in_dir)
        relNewFilePathDir, relNewFilePathFileName = os.path.split(relNewFilePath)
        # 转换文件名
        relNewFilePathFileNameList: list = relNewFilePathFileName.split(".")
        if relNewFilePathFileNameList[-1] == "ui":
            relNewFilePathFileNameList[-1] = "py"
        pyfilePath = os.path.normpath(".".join(relNewFilePathFileNameList))
        pyRelPath = os.path.join(relNewFilePathDir, pyfilePath)  # 相对路径
        # 得到目标文件路径
        pyOutPath = os.path.join(self.project.ui_out_dir, pyRelPath)
        return pyOutPath
    def on_created(self, event):
        if not self.isPassFileter(event.src_path):
            return
        print(f"create file {event.src_path}")
        newFile: str = event.src_path
        if event.is_directory:
            print("新文件夹")
            return
        pyOutPath = self.getVirtualPathByUiInPathRelatedPyOutPath(event.src_path)
        pyOutDir, pyOutFilename = os.path.split(pyOutPath)
        if not os.path.exists(pyOutDir):
            os.makedirs(pyOutDir)
        # 编译
        self.uicCompile(newFile,pyOutPath)
        pass
    def on_deleted(self, event):
        print(f"delete file {event.src_path}")

        #在project.ui_out_dir中找到对对应的文件路径，存在就删除
        path = self.getVirtualPathByUiInPathRelatedPyOutPath(event.src_path)
        if os.path.exists(path):
            os.remove(path)
            print("Reverse direction deleted successfully!")
        pass

    def on_moved(self, event):
        if not  self.isPassFileter(event.dest_path):
            return
        print(f"Moved {event.src_path} to {event.dest_path}")
        pyFilePath = self.getVirtualPathByUiInPathRelatedPyOutPath(event.dest_path)
        self.uicCompile(event.dest_path, pyFilePath)
        print("Moved - Recompile ui files successfully!")
        pass

    def on_closed(self, event):
        print(f"closed file {event.src_path}")
        pass

    def on_modified(self, event):
        if not self.isPassFileter(event.src_path):
            return
        print(f"modified file {event.src_path}")
        pyFilePath =  self.getVirtualPathByUiInPathRelatedPyOutPath(event.src_path)
        self.uicCompile(event.src_path,pyFilePath)
        print("modified - Recompile ui files successfully!")
        pass


class FileWatchHelper(QObject):
    def __init__(self, project: Project,projectWidget):
        self.observer = observers.Observer()
        self.appData: SettingManager = SettingManager()
        self.fileWatchHandle = FileWatchHandle(project,projectWidget)
        self.project = project
        pass

    def startFileWatch(self):
        self.observer = observers.Observer()
        watch = self.observer.schedule(self.fileWatchHandle, path=self.project.ui_in_dir, recursive=True)
        self.observer.start()

    def stopFileWatch(self):
        self.observer.stop()
        self.observer.join()
        pass

    def restartFileWatch(self):
        self.startFileWatch()
        self.stopFileWatch()
        pass
