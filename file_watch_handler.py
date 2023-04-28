import os.path

from PySide6.QtCore import  QObject
from watchdog.events import FileSystemEventHandler
from watchdog import observers

import app_data
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

    def getReflectPathFromRawPath(self,rawPath):
        fileDirAndName = os.path.split(rawPath)
        dir = fileDirAndName[0]
        name = fileDirAndName[1]
        if not fileInFilter(name):
            return None
        name = renameFileSuffix(name, "py")
        dirList = dir.split("\\")
        print(dirList)
        dirList[-1] = self.appConfig.data["path_info"]["qt_py_ui_path"].split("\\")[-1]
        newPath = "\\".join(dirList)
        return os.path.join(newPath, name)
    def on_created(self, event):
        print(f"new file {event.src_path}")
        print(self.getReflectPathFromRawPath(event.src_path))
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