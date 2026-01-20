import os
import sys
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.prompt import Prompt
from transformer import PayrollTransformer

console = Console()

def select_directory():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directory = filedialog.askdirectory(title="Vyberte složku s Excel soubory")
    root.destroy()
    return directory

def run_app():
    transformer = PayrollTransformer()
    
    while True:
        console.clear()
        console.print(Panel.fit(
            "[bold cyan]Payroll Data Transformer[/bold cyan]\n"
            "[white]Nástroj pro transformaci XLSX -> CSV pro mzdové systémy[/white]",
            border_style="bright_blue"
        ))

        selected_path = select_directory()
        if not selected_path:
            console.print("[yellow]Nebyla vybrána žádná složka.[/yellow]")
            choice = Prompt.ask("Chcete to zkusit znovu?", choices=["n", "k"], default="n")
            if choice == "k":
                break
            continue

        root_dir = Path(selected_path)
        files = transformer.find_files(root_dir)

        if not files:
            console.print(f"[yellow]Ve složce {root_dir} nebyly nalezeny žádné .xlsx soubory.[/yellow]")
        else:
            console.print(f"[green]Nalezeno {len(files)} souborů ke zpracování.[/green]")
            
            results = []
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                console=console
            ) as progress:
                task = progress.add_task("[cyan]Zpracování...", total=len(files))
                
                for file_path in files:
                    progress.update(task, description=f"Zpracovávám: {file_path.name}")
                    success, message = transformer.process_file(file_path)
                    results.append((file_path.name, success, message))
                    progress.advance(task)

            # Show Summary Table
            table = Table(title="Shrnutí zpracování")
            table.add_column("Soubor", style="cyan")
            table.add_column("Stav", style="bold")
            table.add_column("Zpráva", style="white")

            for name, success, message in results:
                status = "[green]OK[/green]" if success else "[red]CHYBA[/red]"
                table.add_row(name, status, message)

            console.print(table)

        choice = Prompt.ask("\n[bold]K[/bold]onec nebo [bold]N[/bold]ový výběr?", choices=["k", "n"], default="n")
        if choice.lower() == "k":
            console.print("[bold blue]Nashledanou![/bold blue]")
            break

if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        console.print("\n[yellow]Aplikace ukončena uživatelem.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]Kritická chyba: {str(e)}[/bold red]")
        input("Stiskněte Enter pro ukončení...")
        sys.exit(1)
