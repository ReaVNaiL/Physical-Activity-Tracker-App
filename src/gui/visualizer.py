import sys
from PyQt5 import QtWidgets
from gui.MainWindow import UI_MainWindow
from gui.SecondWindow import UI_SecondWindow


class DataVisualizer:
    def __init__(self) -> None:
        self.UI = UI_MainWindow()
            
    def show(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.UI.setupUi(MainWindow)
        MainWindow.show()
        
        # with open("src/gui/style/stylesheet.css", "r") as f:
        #     app.setStyleSheet(f.read())
            
        # This Adds The Second Window  
        select_button = self.UI.select_button
        select_button.clicked.connect(self.open_helper_window)
        
        # Import Button
        self.populate_dropdown()
        
        sys.exit(app.exec_())

    def open_helper_window(self):
        self.print_message()
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def print_message(self):
        print("The start date is: ", self.UI.start_date.text())
        print("The end date is: ", self.UI.end_date.text())
        print("The index is: ", self.UI.index_dropdown.currentText())
        print("The subject is: ", self.UI.subject_dropdown.currentText())
        print("Checkbox is set to: ", self.UI.time_converter_check_box.isChecked())
        
    def populate_dropdown(self):
        # Populate index box:
        self.UI.index_dropdown.addItem("Summary.csv")
        self.UI.index_dropdown.addItem("Metadata.csv")
        
        # Populate device dropdown
        self.UI.subject_dropdown.addItem("Apple Watch")
        self.UI.subject_dropdown.addItem("Fitbit")
    
if __name__ == "__main__":
    ui = DataVisualizer()
    ui.show()