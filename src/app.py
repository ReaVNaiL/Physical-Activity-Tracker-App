# Importing the necessary modules
import os
from time import sleep
import asyncio

# Path: Physical-Activity-Tracker-App\src\
from gui.visualizer import DataVisualizer
# from load_csv import DataHandler

def start_up():
    # This function will be called when the app is started
    """ Placeholder for main window """
    # # Show the main window
    program = DataVisualizer()
    program.show()
    # program.open_helper_window()
    
if __name__ == "__main__":
    start_up()
