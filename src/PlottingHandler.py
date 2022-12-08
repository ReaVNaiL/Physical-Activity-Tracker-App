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
        print(repr(self._data_handler))
        
        self._data_handler.subject_id = "310"
        self.data = self._data_handler.process_data_filtering(filter_enabled=True)
        self._data_handler.subject_id = "311"
        self.data2 = self._data_handler.process_data_filtering(filter_enabled=True)
        self._data_handler.subject_id = "312"
        self.data3 = self._data_handler.process_data_filtering(filter_enabled=True)
        
class Window(QWidget):
    def __init__(self, input_val, data_handler: PlottingHandler):
        super().__init__()
        self.top = 200
        self.left = 500
        self.width = 1400
        self.height = 1300
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        self._data_handler = data_handler
        self.plot_graph(input_val)
        
    def plot_graph(self, input_val):
        formLayout = QFormLayout()
        groupBox = QGroupBox()
        
        df = self._data_handler.data
        df2 = self._data_handler.data2
        df3 = self._data_handler.data3

        # This returns epoch time in milliseconds
        x_axis = df['Unix Timestamp (UTC)'].to_list() #x_axis is time
        x_axis2 = df2['Unix Timestamp (UTC)'].to_list() #x_axis is time
        x_axis3 = df3['Unix Timestamp (UTC)'].to_list() #x_axis is time

        # Drop the Datetime (Standard) column
        # df = df.drop(columns=['Datetime (Standard)'])
        # df = df.drop(columns=['Datetime (UTC)'])
        # df = df.drop(columns=['Timezone (minutes)'])
        df = df.drop(columns=['Unix Timestamp (UTC)'])

        # Set the x-axis to seconds since epoch
        start_date = x_axis[0] / 1000
        end_date = x_axis[-1] / 1000
        date_range = np.linspace(start_date, end_date, len(x_axis))
        
        df2 = df2.drop(columns=['Unix Timestamp (UTC)'])

        # Set the x-axis to seconds since epoch
        start_date2 = x_axis[0] / 1000
        end_date2 = x_axis[-1] / 1000
        date_range2 = np.linspace(start_date2, end_date2, len(x_axis2))

        df3 = df3.drop(columns=['Unix Timestamp (UTC)'])
        
        # Set the x-axis to seconds since epoch
        start_date3 = x_axis[0] / 1000
        end_date3 = x_axis[-1] / 1000
        date_range3 = np.linspace(start_date3, end_date3, len(x_axis3))
        
        # for column in df.columns:
        y_axis = df['Movement intensity'].to_list() #y_axis is mng avg

        # Generating plot widget
        plot = pg.PlotWidget()
        
        # Set up the x-axis to display the time and date
        axis = DateAxisItem(orientation='bottom', is_standard=True)
        axis.attachToPlotItem(plot.getPlotItem())
        plot.setMinimumSize(300, 300)
        
        # Choose a random color for the pen between blue and purple
        pen_color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
        
        # Plot the data
        subject_310 = plot.plot(x=date_range, y=y_axis, pen=None, symbol='o', symbolPen=None, symbolSize=5, symbolBrush=(255,0,0,150))
        
        second_plot = df2['Movement intensity'].to_list()
        subject_311 = plot.plot(x=date_range2, y=second_plot, pen=None, symbol='o', symbolPen=None, symbolSize=5, symbolBrush=(0,255,0,150))
        
        third_plot = df3['Movement intensity'].to_list()
        subject_312 = plot.plot(x=date_range3, y=third_plot, pen=None, symbol='o', symbolPen=None, symbolSize=5, symbolBrush=(0,0,255,150))
        
        # Scatter plot
        plot.plot()
        
        # display grid
        plot.showGrid(x=True, y=True)
        plot.setLabel('left', self._data_handler._data_handler.graph_filter[0])
        plot.setTitle(self._data_handler._data_handler.graph_filter[0])
        
        
        # Prevent zooming past the data
        plot.setLimits(xMin=date_range[0], xMax=date_range[-1], yMin=min(third_plot), yMax=max(second_plot))
        
        # Add legend to the plot for the y-axis
        legend_y = pg.LegendItem((100, 60), offset=(70, 30))
        legend_y.setParentItem(plot.graphicsItem())
        legend_y.addItem(subject_310, "310")
        legend_y.addItem(subject_311, "311")
        legend_y.addItem(subject_312, "312")
        
        
        formLayout.addRow(plot)
                

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(1200)
        layout = QVBoxLayout(self)
        layout.addWidget(scroll)
        self.show()

        
if __name__ == "__main__":
    plotting_handler = PlottingHandler()
    plotting_handler.TEST_PLOTTING_HANDLER()
    App = QApplication(sys.argv)
    window = Window(3, plotting_handler)
    sys.exit(App.exec())