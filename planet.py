# planet.py
from enum import Enum, auto
import sys


class SolarBodies(Enum):
    MERCURY = auto()
    VENUS = auto()
    EARTH = auto()
    MARS = auto()
    JUPITER = auto()
    SATURN = auto()
    URANUS = auto()
    NEPTUNE = auto()
    PLUTO = auto()  # Though not a planet, it's a notable solar body


def get_planet_input():
    options = {body.name: body for body in SolarBodies}
    prompt = "What planet will you be? Here's a list of options: " + ", ".join(options.keys()) + "\n> "
    while True:
        choice = input(prompt).upper()
        if choice in options:
            return options[choice]
        else:
            print("Invalid option, please choose from the list.")


class Planet:
    def __init__(self):
        self.selection = get_planet_input()

    def handle(self):
        # Simulate a switch statement using a dictionary
        # This is a simple placeholder. Extend this dictionary with actual functionality as needed.
        action = {
            SolarBodies.MERCURY: lambda: print("Handling Mercury."),
            SolarBodies.VENUS: lambda: print("Handling Venus."),
            SolarBodies.EARTH: lambda: print("Handling Earth."),
            SolarBodies.MARS: lambda: print("Handling Mars."),
            SolarBodies.JUPITER: lambda: print("Handling Jupiter."),
            SolarBodies.SATURN: lambda: print("Handling Saturn."),
            SolarBodies.URANUS: lambda: print("Handling Uranus."),
            SolarBodies.NEPTUNE: lambda: print("Handling Neptune."),
            SolarBodies.PLUTO: lambda: print("Handling Pluto (yes, we included Pluto!)."),
        }

        handler = action.get(self.selection, lambda: print("This body is not handled yet."))
        handler()
