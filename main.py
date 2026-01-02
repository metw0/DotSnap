import time
from pathlib import Path
from datetime import datetime

from core.config_loader import load_config
from core.scanner import get_valid_path
from core.archiver import create_archive
from core.display import show_status_table, show_menu, console
from core.unpacker import extract_archive
from rich.progress import track


def main():
    files, _ = load_config()
    project_root = Path(__file__).parent

    valid_files = {}
    display_data = {}

    for _ in track(range(5), description='[green]Checking files...'):
        time.sleep(0.1)

    for name, raw_path in files.items():
        path_obj = get_valid_path(raw_path)
        full_path = Path(raw_path).expanduser()
        display_data[name] = full_path
        if path_obj:
            valid_files[name] = path_obj

    show_status_table(display_data)
    choice = show_menu()

    if choice == '1':
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        archive_path = project_root / 'backups' / f'backup_{timestamp}.tar.gz'

        console.print(f'[yellow]Archiving to {archive_path.name}...')
        create_archive(archive_path, valid_files)
        console.print('[bold green]Success ! Backup created inside /backups[/]')


    elif choice == '2':
        backup_dir = project_root / 'backups'
        archives = list(backup_dir.glob('*.tar.gz'))

        if not archives:
            console.print('[bold red]No backups found in /backups folder ![/]')

        else:
            latest_backup = max(archives, key=lambda p: p.stat().st_mtime)
            console.print(f'[yellow]Restoring from:[/] {latest_backup.name}...')

            if extract_archive(latest_backup):
                console.print(f'[bold green]Files have been restored to {Path.home()}[/]')

            else:
                console.print('[bold red]Restore failed ![/]')


if __name__ == '__main__':
    main()