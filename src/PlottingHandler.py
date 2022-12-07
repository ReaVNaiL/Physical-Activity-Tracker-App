import sys
import helpers.format_date as ft
from helpers.date_axis import DateAxisItem
from DataHandler import DataHandler
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from PyQt5 import QtGui
from datetime import datetime

import sys
import pyqtgraph as pg
import pandas as pd
import numpy as np

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
        groupBox = QGroupBox()
        plotWidget_list = []
        
        df = self._data_handler.data

        # This returns epoch time in milliseconds
        x_axis = df['Unix Timestamp (UTC)'].to_list() #x_axis is time
        y_axis = df['Eda avg'].to_list() #y_axis is mng avg

        # Set the x-axis to seconds since epoch
        start_date = x_axis[0] / 1000
        end_date = x_axis[-1] / 1000
        date_range = np.linspace(start_date, end_date, len(x_axis))
        
        for i in range(input_val):
            # Generating plot widget
            plot = pg.PlotWidget()
            
            # Set up the x-axis to display the time and date
            axis = DateAxisItem(orientation='bottom')
            axis.attachToPlotItem(plot.getPlotItem())
            
            plot.plot(x=date_range, y=y_axis, pen="r")
            
            # display grid
            plot.showGrid(x=True, y=True)
            plot.setLabel('left', "EDA Avg")
            plot.setTitle("EDA Avg")
            

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