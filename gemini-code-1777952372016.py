import os
import time
import webbrowser
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text

console = Console()

class InterZSpotify:
    def __init__(self):
        self.library = {
            "XXXTENTACION": [
                {"title": "Jocelyn Flores", "album": "17", "duration": "1:59"},
                {"title": "SAD!", "album": "?", "duration": "2:46"},
                {"title": "Moonlight", "album": "?", "duration": "2:15"},
                {"title": "Look At Me!", "album": "Revenge", "duration": "2:06"},
                {"title": "Hope", "album": "?", "duration": "1:50"}
            ],
            "LIL PEEP": [
                {"title": "Star Shopping", "album": "Single", "duration": "2:22"},
                {"title": "Save That Shit", "album": "Come Over When You're Sober", "duration": "3:51"},
                {"title": "Falling Down", "album": "Single", "duration": "3:10"},
                {"title": "Beamer Boy", "album": "California Girls", "duration": "3:23"}
            ],
            "LIL UZI VERT": [
                {"title": "XO Tour Llif3", "album": "Luv Is Rage 2", "duration": "3:02"},
                {"title": "20 Min", "album": "Luv Is Rage 2", "duration": "3:40"},
                {"title": "The Way Life Goes", "album": "Luv Is Rage 2", "duration": "3:41"},
                {"title": "Money Longer", "album": "Lil Uzi Vert vs. The World", "duration": "3:18"}
            ]
        }
        self.current_playing = "None"

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def header(self):
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="right")
        grid.add_row(
            Text(" 👁️ INTERZ PREMIUM", style="bold green"),
            Text("Welcome, OwnerZ ", style="bold white")
        )
        return Panel(grid, style="green")

    def show_main_menu(self):
        self.clear()
        console.print(self.header())
        table = Table(title="Your Artists", show_header=True, header_style="bold green", expand=True)
        table.add_column("ID", style="dim", width=6)
        table.add_column("Artist Name")
        table.add_column("Status", justify="right")

        for idx, artist in enumerate(self.library.keys(), 1):
            table.add_row(str(idx), artist, "[green]Verified")

        console.print(table)
        console.print("\n[bold green][0][/bold green] Exit")

    def show_songs(self, artist):
        self.clear()
        console.print(self.header())
        songs = self.library[artist]
        table = Table(title=f"Songs by {artist}", show_header=True, header_style="bold green", expand=True)
        table.add_column("#", style="dim")
        table.add_column("Title")
        table.add_column("Album")
        table.add_column("Duration", justify="right")

        for idx, song in enumerate(songs, 1):
            table.add_row(str(idx), song['title'], song['album'], song['duration'])

        console.print(table)
        console.print("\n[bold green][B][/bold green] Back to Artists")

    def play(self, artist, song_index):
        song = self.library[artist][song_index]
        search_query = f"{artist} {song['title']}".replace(" ", "+")
        
        # UI Playing Effect
        self.clear()
        with Live(self.generate_playing_ui(song['title'], artist), refresh_per_second=4):
            time.sleep(2)
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            time.sleep(1)

    def generate_playing_ui(self, title, artist):
        content = f"\n  [bold white]Now Playing:[/bold white]\n  [bold green]♫ {title}[/bold green]\n  [dim]{artist}[/dim]\n\n  [green]━━━━━━●───────────[/green] 0:01 / 3:00\n  [white]  ◀   II   ▶  [/white]"
        return Panel(content, title="InterZ Player", border_style="green", padding=(1, 2))

    def run(self):
        while True:
            self.show_main_menu()
            choice = input("\nSelect Artist ID: ")
            
            if choice == "0":
                break
            
            try:
                artist_key = list(self.library.keys())[int(choice)-1]
                while True:
                    self.show_songs(artist_key)
                    song_choice = input("\nSelect Song # to Play (or 'B'): ")
                    
                    if song_choice.lower() == 'b':
                        break
                    
                    self.play(artist_key, int(song_choice)-1)
            except Exception:
                continue

if __name__ == "__main__":
    app = InterZSpotify()
    app.run()