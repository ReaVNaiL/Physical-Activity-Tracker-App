# Importing the necessary modules
import sys
import os

# Path: Physical-Activity-Tracker-App\src\
from models import *
from gui import *
import load_csv as lc

class MainWindow():
    """ This will not build, it's just a placeholder """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Physical Activity Tracker App")
        self.resize(800, 600)
        
    def show(self):
        super().show()
        
    def setWindowTitle(self, title):
        super().setWindowTitle(title)
    
    def resize(self, width, height):
        super().resize(width, height)

def start_up():
    # This function will be called when the app is started
    
    """ Placeholder for main window """
    # main_window = MainWindow() 

    # Show the main window
    # main_window.show()
    
    csv_sample_path = os.path.join(os.path.dirname(__file__), "../data/20200118/310/summary.csv")
    
    csv_object = lc.load_csv(csv_sample_path)
    
    print(csv_object)
    
    
if __name__ == "__main__":
    start_up()