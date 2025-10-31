from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt

#list of rich colors for random function
COLORS = ["red", "green", "blue", "yellow", "magenta", "cyan", "white", "bright_red", 
         "bright_green", "bright_blue", "bright_yellow", "bright_magenta", "bright_cyan"]

console = Console()

def get_random_colored_text(text: str) -> Text:
    """returning the text with a random color to make things more interesting"""
    color = random.choice(COLORS)
    return Text(text, style=color)

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        # return a plain string so callers (and tests) can treat the result as text
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    # return a plain string; coloring is applied only when printing to console
    return f"You walk left. {event}"

def right_path(event):
    # return a plain string; coloring is applied only when printing to console
    return f"You walk right. {event}"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("You wake up in a dark forest. You can go left or right.", style="bold magenta underline")
    while True:
        choice = Prompt.ask("[cyan]Which direction do you choose? (left/right/exit): [/cyan]")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        # color each printed output randomly while keeping step() return values as strings
        console.print(get_random_colored_text(step(choice, events)))
