import sys
import helpers.format_date as ft
from DataHandler import DataHandler
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from PyQt5 import QtGui

import sys
import pyqtgraph as pg
import pandas as pd

class PlottingHandler:
    def __init__(self):
        self._data_handler = DataHandler()
        self._data_handler.TEST_DATA_HANDLER()

    def TEST_PLOTTING_HANDLER(self):
        print("TEST_PLOTTING_HANDLER")
        
        # for each attribute of data_handler print the value
        self._data_handler.__repr__()
        
        self.data = self._data_handler.process_data_filtering(filter_enabled=False)

        x_axis = self.data["Unix Timestamp (UTC)"]
        y_axis = self.data["Eda avg"]
        
        # new_time = ft.convert_timestamp_standard(x_axis.to_list()[2])

class Window(QWidget):
    def __init__(self, input_val, data_handler: PlottingHandler):
        super().__init__()
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        self._data_handler = data_handler
        self.plot_graph(input_val)
        
    def plot_graph(self, input_val):
        formLayout = QFormLayout()
        groupBox = QGroupBox("This Is Group Box")
        plotWidget_list = []
        
        df = self._data_handler.data

        for i in range(input_val):
            y = df['Unix Timestamp (UTC)'].to_list() #x_axis is time
            y2 = df['Eda avg'].to_list() #y_axis is mng avg

            plot = pg.PlotWidget()
            plot.plot(y, y2, pen='r')

        
            plotWidget_list.append(plot)
            formLayout.addRow(plotWidget_list[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        self.show()

        
if __name__ == "__main__":
    plotting_handler = PlottingHandler()
    plotting_handler.TEST_PLOTTING_HANDLER()
    App = QApplication(sys.argv)
    window = Window(1, plotting_handler)
    sys.exit(App.exec())