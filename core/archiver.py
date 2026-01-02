import tarfile
from pathlib import Path

def create_archive(destination: Path, files_to_backup: dict):
    destination.parent.mkdir(parents=True, exist_ok=True)

    with tarfile.open(destination, 'w:gz') as tar:
        for name, path in files_to_backup.items():
            if path.exists():
                try:
                    rel_path = path.relative_to(Path.home())
                    tar.add(path, arcname=rel_path)
                except ValueError:
                    tar.add(path, arcname=path.name)