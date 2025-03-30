import time
import threading
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live

console = Console()

neon_shades = ["#00FFFF", "#00DDFF", "#00BBFF", "#0099FF", "#0077FF", "#0055FF"]
num_shades = len(neon_shades)

running = False  # Variable pour contrôler l'animation

def generate_title(text, shift):
    """ Génère le texte ASCII avec effet néon fluide """
    ascii_text = pyfiglet.figlet_format(text, font="slant").split("\n")
    styled_text = Text()
    
    for line in ascii_text:
        for i, char in enumerate(line):
            if char != " ":
                color = neon_shades[(i + shift) % num_shades]
                styled_text.append(char, style=f"bold {color}")
            else:
                styled_text.append(" ")
        styled_text.append("\n")
    
    border_color = neon_shades[shift % num_shades]
    return Panel(styled_text, border_style=border_color)

def neon_text(text, duration=5):
    """ Affiche du texte avec effet néon fluide en arrière-plan """
    global running
    running = True

    def neon_effect():
        shift = 0
        with Live(auto_refresh=False) as live:
            start_time = time.time()
            while running and (time.time() - start_time < duration):
                live.update(generate_title(text, shift), refresh=True)
                shift += 1
                time.sleep(0.1)

    animation_thread = threading.Thread(target=neon_effect, daemon=True)
    animation_thread.start()

    time.sleep(duration)  # Attend la fin de l'animation
    running = False  # Arrête l'animation proprement
    console.clear()  # Nettoie l'écran après l'animation
