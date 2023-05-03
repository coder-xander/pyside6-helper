from pathlib import Path

def find_file_by_filename(filename):
    paths = []
    for drive in Path('/').iterdir():
        if drive.is_dir():
            for path in drive.glob('**/' + filename):
                paths.append(str(path))
    return paths
