# Importing the necessary modules
from importlib.resources import path
import sys
import os

# Path: Physical-Activity-Tracker-App\src\
import gui.gui as gui
import load_csv as lc


def start_up():
    # This function will be called when the app is started
    
    """ Placeholder for main window """
    # Show the main window
    program = gui.MainWindow(800, 600, "Physical Activity Tracker")
    program.show()
    
    csv_sample_path = os.path.join(os.path.dirname(__file__), "../data/20200118/310/summary.csv")
    
    csv_object = lc.load_csv(csv_sample_path)
    
    print(csv_object)
    
    
if __name__ == "__main__":
    start_up()