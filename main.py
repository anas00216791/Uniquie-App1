
from typer import Typer
from rich.console import Console
from session import SessionManager

app = Typer()
console = Console()
session_manager = SessionManager()

@app.command()
def start():
    console.print("[bold green]\nWelcome to MoodGarden 🌿 Your Emotional Journal[/bold green]")

    while True:
        console.print("\n[1] New Mood Entry\n[2] View All Entries\n[3] Exit")
        choice = input("> ")

        if choice == "1":
            session_manager.new_entry()
        elif choice == "2":
            session_manager.view_entries()
        elif choice == "3":
            console.print("Take care 🌸")
            break
        else:
            console.print("[red]Invalid choice. Try again.[/red]")

if __name__ == "__main__":
    app()
