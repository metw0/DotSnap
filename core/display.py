from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table


console = Console()

def show_menu():
    main_panel = """1. Create backup\n2. Restore backup"""
    console.print(Panel(main_panel))

    return Prompt.ask()

def show_status_table(files_to_backup):
    table = Table(title='DotSnap v0.1.0')
    table.add_column('Component')
    table.add_column('Path')
    table.add_column('Status')

    # Теперь внутри функции мы можем использовать files_to_backup
    for name, path in files_to_backup.items():
        status = '[bold green]READY[/]' if path.exists() else '[bold red]MISSING[/]'
        table.add_row(name, str(path), status)

    console.print(table)
