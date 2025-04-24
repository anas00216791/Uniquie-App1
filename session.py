
import os
import json
from datetime import datetime
from mood_entry import MoodEntry
from rich.console import Console
from rich.table import Table

class SessionManager:
    def __init__(self):
        self.console = Console()
        self.file = "entries.json"
        self.entries = self.load_entries()

    def load_entries(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                return json.load(f)
        return []

    def save_entries(self):
        with open(self.file, 'w') as f:
            json.dump(self.entries, f, indent=4)

    def new_entry(self):
        mood = input("How are you feeling today (happy, sad, angry, calm, etc)? ")
        journal = input("Write a short journal entry: ")
        entry = MoodEntry(mood, journal)
        analysis = entry.analyze()
        suggestion = entry.suggest()
        self.console.print(f"\n[cyan]Mood Analysis:[/cyan] {analysis}")
        self.console.print(f"[green]Suggestion:[/green] {suggestion}")

        self.entries.append(entry.to_dict())
        self.save_entries()
        self.console.print("[bold green]Entry saved![/bold green]")

    def view_entries(self):
        if not self.entries:
            self.console.print("[yellow]No entries yet.[/yellow]")
            return

        table = Table(title="Mood Entries")
        table.add_column("Date")
        table.add_column("Mood")
        table.add_column("Snippet")

        for entry in self.entries:
            table.add_row(entry["date"], entry["mood"], entry["journal"][:30] + "...")

        self.console.print(table)

