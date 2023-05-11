import os
from pathlib import Path
import threading
class GlobalValues:
    mainwindow = None
    settingManager = None
    singletonLock =  threading.Lock()
    def __getattribute__(self, item):
        with GlobalValues.singletonLock:
            return item

def find_file_by_filename(filename):
    paths = []
    for drive in Path('/').iterdir():
        if drive.is_dir():
            for path in drive.glob('**/' + filename):
                paths.append(str(path.absolute()))
    for i in paths[::-1]:
        if i.split("\\")[1]=="$Recycle.Bin":
            paths.remove(i)
    return paths
