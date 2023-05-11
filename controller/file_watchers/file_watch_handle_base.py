from PySide6.QtCore import QObject, Signal
from watchdog.events import FileSystemEventHandler


class FileWatchHandleBase(FileSystemEventHandler, QObject):
    signal_log = Signal(str)

    def __init__(self):
        super().__init__()
        pass
