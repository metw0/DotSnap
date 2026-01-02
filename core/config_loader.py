import tomllib
from pathlib import Path

def load_config():
    base_dir = Path(__file__).parent.parent
    config_path = base_dir / 'config.toml'

    with open(config_path, 'rb') as f:
        data = tomllib.load(f)

    dotfiles = data.get('dotfiles', {})
    backup_path = data.get('settings', {}).get('backup_dir')

    return dotfiles, backup_path
