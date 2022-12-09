# Importing the necessary modules
import os
from time import sleep
import asyncio

# Path: Physical-Activity-Tracker-App\src\
from src.gui.DataVisualizer import DataVisualizer
from src.DataHandler import DataHandler


def start_up():
    # This function will be called when the app is started
    """Placeholder for main window"""

    # Instantiate the Data Handler
    handler = DataHandler()

    # # Show the main window
    program = DataVisualizer(handler)
    program.show()


if __name__ == "__main__":
    start_up()
