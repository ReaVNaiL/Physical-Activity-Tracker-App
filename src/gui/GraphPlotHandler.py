import random
import sys
from src.gui.MainWindow import UI_MainWindow
from src.helpers.date_axis import DateAxisItem
from src.DataHandler import DataHandler
from PyQt5 import QtWidgets
from src.gui.MainWindow import UI_MainWindow
from src.gui.SecondWindow import UI_SecondWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QGroupBox, QFormLayout, QListWidgetItem, QMessageBox

import sys
import pyqtgraph as pg
import pandas as pd
import numpy as np


class GraphPlotHandler():
    sync_plots: list[pg.PlotItem] = []

    nav_bar_created = False
    subject_colors = [(36, 158, 121), (179, 155, 215), (215, 239, 188)]
    brush_colors = [(36, 158, 121, 80), (179, 155, 215, 80), (215, 239, 188, 80)]
    
    def __init__(self, UI: UI_MainWindow, handler: DataHandler):
        self._UI = UI
        self._handler = handler

    def populate_graph_subjects(self, record_count: int, records_df: pd.DataFrame):
        """
        Populates the graph area with the data from the `records_df` parameter

        Args:
            `record_count` (int): The number of records to be displayed
            `records_df` (pd.DataFrame): The dataframe containing the records to be displayed

        """
        # Set the graph layout height times the record count
        self.CLEAR_PLOTS()
        
        self.graph_layout = pg.GraphicsLayoutWidget()
        self.graph_layout.setFixedHeight(350 * record_count)

        # Get the Unix Timestamp then drop it
        x_axis = records_df["Unix Timestamp (UTC)"].to_list()
        records_df = records_df.drop(columns=["Unix Timestamp (UTC)"])

        # Set the x-axis to seconds since epoch
        start_date = x_axis[0] / 1000
        end_date = x_axis[-1] / 1000
        date_range = np.linspace(start_date, end_date, len(x_axis))

        color_index = 0
        for column in records_df.columns:
            # setting y_axis
            y_axis = records_df[column].to_list()

            # Generating plot widget
            plot = self.graph_layout.addPlot(col=0)
            plot.setMinimumSize(225, 225)

            # Set up the x-axis to display the time and date
            axis = DateAxisItem(orientation="bottom", is_standard=self._handler.is_standard_time)
            axis.attachToPlotItem(plot)

            # Add margins to the plot 30px
            plot.setContentsMargins(30, 30, 30, 30)

            # Random Pen Color
            pen_color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))

            # Plot the data
            legend_plot = self.paint_plot_design(column, plot, color_index, date_range, y_axis, pen_color)

            # display grid
            plot.showGrid(x=True, y=True)
            plot.setLabel("left", column)
            plot.setTitle(column)

            # Prevent zooming past the data
            plot.setLimits(xMin=start_date, xMax=end_date, yMin=min(y_axis), yMax=max(y_axis))

            # Add legend to the plot for the y-axis
            legend_y = pg.LegendItem((140, 60), offset=(70, 30))
            legend_y.setParentItem(plot.graphicsItem())
            legend_y.addItem(legend_plot, column)

            # Increment the row
            self.graph_layout.nextRow()
            
            # Add the plot to the list of plots to sync
            self.sync_plots.append(plot)
            

        # Create the navigator graph
        self.create_nav_graph(start_date, end_date)
        # graph_layout.setBackground((14, 18, 21, 255))
        
        scroll_area = self._UI.graph_area
        scroll_area.setWidget(self.graph_layout)
        scroll_area.setWidgetResizable(True)
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)

    def populate_graph_all_subjects(self, record_count: int, subject_records: list[pd.DataFrame]):
        """_summary_

        Args:
            record_count (int): _description_
            record_list (list[pd.DataFrame]): _description_
        """
        self.CLEAR_PLOTS()

        # Set the graph layout height times the record count
        self.graph_layout = pg.GraphicsLayoutWidget()
        self.graph_layout.setFixedHeight(233 * record_count)

        # Saving the graph filter
        df_columns = self._handler.graph_filter

        for column in df_columns:
            # Generating plot widget
            plot = self.graph_layout.addPlot(col=0)
            plot.setMinimumSize(225, 225)

            # Set anti-aliasing
            pg.setConfigOptions(antialias=True)

            # Add legend to the plot for the y-axis
            legend_y = pg.LegendItem((140, 90), offset=(-120, 10), brush=(255, 255, 255, 50))
            legend_y.setParentItem(plot.graphicsItem())

            # Set up the x-axis to display the time and date
            axis = DateAxisItem(orientation="bottom", is_standard=self._handler.is_standard_time)
            axis.attachToPlotItem(plot)

            # get the y-axis data
            Y_limits = []
            color_index = 0

            # Plot each subject's data
            for record in subject_records:
                # Get the Unix Timestamp
                x_axis = record["Unix Timestamp (UTC)"].to_list()

                # Set the x-axis to seconds since epoch
                start_date = x_axis[0] / 1000
                end_date = x_axis[-1] / 1000
                date_range = np.linspace(start_date, end_date, len(x_axis))

                # setting y_axis
                y_axis = record[column].to_list()

                # Random Pen Color
                pen_color = self.subject_colors[color_index]

                # Plot the data
                legend_plot = None

                legend_plot = self.paint_plot_design(column, plot, color_index, date_range, y_axis, pen_color)

                # Add the legend
                legend_y.addItem(legend_plot, "Subject: " + record["Subject ID"].to_list()[0])

                # Add the y-axis data to the list
                Y_limits.extend(y_axis)
                color_index += 1
                self.sync_plots.append(plot)

            # # Prevent zooming past the data
            min_Y, max_Y = -0.1, 1.1
            if not column == "On Wrist":
                max_Y = np.max(Y_limits)
                min_Y = np.min(Y_limits)

            plot.setLimits(xMin=start_date, xMax=end_date, yMin=min_Y, yMax=max_Y)

            # Add margins to the plot 30px
            plot.setContentsMargins(30, 30, 30, 30)

            # display grid
            plot.showGrid(x=True, y=True)
            plot.setLabel("left", column)
            plot.setTitle(column)

            # Increment the row
            self.graph_layout.nextRow()

        self.create_nav_graph(start_date, end_date)
        
        scroll_area = self._UI.graph_area
        scroll_area.setWidget(self.graph_layout)
        scroll_area.setWidgetResizable(True)
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)

    def paint_plot_design(self, column, plot, color_index, date_range, y_axis, pen_color):
        if column == "Movement intensity" or column == "Rest":
            legend_plot = plot.plot(
                        x=date_range,
                        y=y_axis,
                        pen=None,
                        symbol=random.choice(["o", "t1", "t"]),
                        symbolPen=None,
                        symbolSize=10,
                        symbolBrush=self.brush_colors[color_index],
                    )
        elif column == "On Wrist":
                    # Bar graph
            legend_plot = plot.plot(
                        x=date_range,
                        y=y_axis,
                        fillLevel=0,
                        fillBrush=self.brush_colors[color_index],
                        symbol="s",
                        symbolPen=None,
                        symbolSize=2,
                        symbolBrush=self.brush_colors[color_index],
                    )
        else:
            legend_plot = plot.plot(
                        x=date_range + 1, y=y_axis, pen=pen_color, fillLevel=0, fillBrush=(150, 150, 150, 60)
                    )
            
        return legend_plot

    def create_nav_graph(self, start_date: int, end_date: int):
        """_summary_

        Args:
            records_df (pd.DataFrame): _description_
        """
                                
        self.bottom_graph_layout = pg.GraphicsLayoutWidget()
        self.bottom_graph_layout.setFixedHeight(153)
        
        self.navigator = pg.LinearRegionItem()
        self.navigator.setBrush(pg.mkBrush(255, 255, 255, 100))
        self.navigator.setZValue(-10)

        self._UI.bottom_left_f.layout().addWidget(self.bottom_graph_layout)
        self.nav_bar_created = True
        
        # Assign it only to the first plot
        self.navigator.sigRegionChanged.connect(self.UPDATE_SIGNAL_PLOTS)
        # self.sync_plots[0].sigXRangeChanged.connect(self.update_navigator)      
          
        self.navigator_plot = self.bottom_graph_layout.addPlot(row=0, col=0)
        
        # Set up the x-axis to display the time and date
        axis = DateAxisItem(orientation="bottom", is_standard=self._handler.is_standard_time)
        axis.attachToPlotItem(self.navigator_plot)
        
        self.navigator_plot.addItem(self.navigator)
        
        # delete the old navigator
        self.navigator_plot.clear()
        
        # Take the middle date + half a day
        navigator_region_start = (end_date - start_date) / 2 + start_date - 21600
        navigator_region_end = navigator_region_start + 43200
        
        self.navigator = pg.LinearRegionItem([navigator_region_start, navigator_region_end])
        self.navigator.sigRegionChanged.connect(self.UPDATE_SIGNAL_PLOTS)

        # Set the region with correct start and end date
        self.navigator_plot.addItem(self.navigator)
        
        # Update the plots for 
        self.navigator_plot.plot(x=self.sync_plots[0].getAxis("bottom").range, y=self.sync_plots[0].getAxis("left").range, pen="w")
        
        self.navigator_plot.setLimits(
            xMin=start_date,
            xMax=end_date,
            yMin=self.sync_plots[0].getAxis("left").range[0],
            yMax=self.sync_plots[0].getAxis("left").range[1],
        )
        
        self.navigator_plot.setTitle("Navigator")

    def UPDATE_NAVIGATOR(self):
        self.navigator.setRegion(self.sync_plots[0].getViewBox().viewRange()[0])

    def UPDATE_SIGNAL_PLOTS(self):
        for g in self.sync_plots:
            if g != self.navigator:
                g.blockSignals(True)
                g.setXRange(*self.navigator.getRegion(), padding=0)
                g.blockSignals(False)
    
    def CLEAR_PLOTS(self):
        try:
            self.bottom_graph_layout.setParent(None)
            self.graph_layout.setParent(None)
            self.navigator_plot.setParent(None)
            self.navigator.setParent(None)
        except:
            pass
        self.sync_plots = []
        
    def TEST_PLOTTING_HANDLER(self):
        print("TEST_PLOTTING_HANDLER")

        # for each attribute of data_handler print the value
        print(repr(self._handler))

        self._handler.subject_id = "310"
        self.data = self._handler.process_data_filtering(filter_enabled=True)
        self._handler.subject_id = "311"
        self.data2 = self._handler.process_data_filtering(filter_enabled=True)
        self._handler.subject_id = "312"
        self.data3 = self._handler.process_data_filtering(filter_enabled=True)


if __name__ == "__main__":
    plotting_handler = GraphPlotHandler()
