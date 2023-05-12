from PySide6.QtCore import QObject, Signal
from watchdog.events import FileSystemEventHandler


class FileWatchHandleBase(QObject,FileSystemEventHandler):
    signal_log = Signal(str)
    def __init__(self):
        super().__init__()
        self.observer = None
        pass


    def isPassFileter(self, path: str):
        pass
