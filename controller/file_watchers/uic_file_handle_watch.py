import os
import subprocess

from watchdog import observers

from file_watchers.file_watch_handle_base import FileWatchHandleBase
from setting_manager import Project


class UicFileWatchHandle(FileWatchHandleBase):
    def __init__(self,project:Project):
        super().__init__()
        self.project = project

    def run(self):
        self.observer = observers.Observer()
        self.observer.schedule(self, path=self.project.ui_in_dir, recursive=True)
        self.observer.start()
        self.signal_log.emit("start uic file watch")

    def connectLog(self,logFunc):
        self.signal_log.connect(logFunc)

    def uicCompile(self, uiFile, pyFile):
        result = subprocess.run([self.project.pyside6_uic_path, uiFile, "-o", pyFile], capture_output=True,
                                text=True)
        print(result.stdout)
        dirname, filename = os.path.split(uiFile)
        if result.returncode == 0:
            self.signal_log.emit(f"compile {filename} done.")

    def isPassFileter(self, path: str):
        filterList = [".ui"]
        for i in filterList:
            if path.endswith(i):
                return True

    def getVirtualPathByUiInPathRelatedPyOutPath(self, rawpath):
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
        self.uicCompile(newFile, pyOutPath)
        pass

    def on_deleted(self, event):
        print(f"delete file {event.src_path}")

        # 在project.ui_out_dir中找到对对应的文件路径，存在就删除
        path = self.getVirtualPathByUiInPathRelatedPyOutPath(event.src_path)
        if os.path.exists(path):
            os.remove(path)
            print("Reverse direction deleted successfully!")
        pass

    def on_moved(self, event):
        if not self.isPassFileter(event.dest_path):
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
        pyFilePath = self.getVirtualPathByUiInPathRelatedPyOutPath(event.src_path)
        self.uicCompile(event.src_path, pyFilePath)
        print("modified - Recompile ui files successfully!")
        pass