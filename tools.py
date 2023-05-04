import os
from pathlib import Path
import threading

#单例模式注解
def singleton(cls):
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]

    return get_instance

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
