from pathlib import Path

def get_valid_path(raw_path):
    path = Path(raw_path).expanduser()

    if path.exists():
        return path
    else:
        return None
