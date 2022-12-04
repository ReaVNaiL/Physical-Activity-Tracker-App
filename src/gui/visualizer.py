import sys
from PyQt5 import QtWidgets
from gui.MainWindow import UI_MainWindow
from gui.SecondWindow import UI_SecondWindow
import pyqtgraph as pg
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout


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
        # popular graphs
        self.populate_graph_test(10)

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

    def populate_graph_test(self, count: int):
        '''
        goal: generate graph location equal to the row count

        '''
        formLayout = QFormLayout()
        groupBox = QGroupBox()
        plotWidget_list = []
        for i in range(count):
            y = [1, 2, 3]
            y2 = [2, 3, 4]

            plot = pg.PlotWidget()
            plot.setMinimumSize(225, 225)
            plot.plot(y, y2, pen='r')
            plotWidget_list.append(plot)
            formLayout.addRow(plotWidget_list[i])

        groupBox.setLayout(formLayout)

        scroll_area = self.UI.graph_area
        scroll_area.setWidget(groupBox)
        scroll_area.setWidgetResizable(True)
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)


if __name__ == "__main__":
    ui = DataVisualizer()
    ui.show()
