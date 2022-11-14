# Importing the necessary modules
import os

# Path: Physical-Activity-Tracker-App\src\
from gui.gui import MainWindow
import load_csv as lc


def start_up():
    # This function will be called when the app is started
    
    """ Placeholder for main window """
    # # Show the main window
    program = MainWindow(800, 600, "Physical Activity Tracker")
    program.show()
    
    # Need to parse CSV Data into window gui
    csv_sample_path = os.path.join(os.path.dirname(__file__), "../data/20200118/310/summary.csv")
    
    csv_object = lc.load_csv(csv_sample_path)
    # lc.parse_csv(csv_object, "summary")
    
    print(csv_object[:5])
    
    
if __name__ == "__main__":
    start_up()