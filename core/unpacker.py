import tarfile
from pathlib import Path

def extract_archive(archive_path: Path):
    home_dir = Path.home()

    if not archive_path.exists():
        return False

    with tarfile.open(archive_path, 'r:gz') as tar:
        tar.extractall(path=home_dir)
    return True