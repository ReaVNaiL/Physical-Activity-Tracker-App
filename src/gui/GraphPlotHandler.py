import random
import sys
from gui.MainWindow import UI_MainWindow
from helpers.date_axis import DateAxisItem
from DataHandler import DataHandler
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from PyQt5 import QtGui
from datetime import datetime

import sys
import pyqtgraph as pg
import pandas as pd
import numpy as np


class GraphPlotHandler():
    def __init__(self, UI: UI_MainWindow, handler: DataHandler):
        self._UI = UI
        self._handler = handler

    # All The Graphing Functions Need To Be Moved To A New Class
    def populate_graph_subjects(self, record_count: int, records_df: pd.DataFrame):
        """
        Populates the graph area with the data from the `records_df` parameter

        Args:
            `record_count` (int): The number of records to be displayed
            `records_df` (pd.DataFrame): The dataframe containing the records to be displayed

        """
        # Set the graph layout height times the record count
        graph_layout = pg.GraphicsLayoutWidget()
        graph_layout.setFixedHeight(350 * record_count)

        # Get the Unix Timestamp then drop it
        x_axis = records_df["Unix Timestamp (UTC)"].to_list()
        records_df = records_df.drop(columns=["Unix Timestamp (UTC)"])

        # Set the x-axis to seconds since epoch
        start_date = x_axis[0] / 1000
        end_date = x_axis[-1] / 1000
        date_range = np.linspace(start_date, end_date, len(x_axis))

        for column in records_df.columns:
            # setting y_axis
            y_axis = records_df[column].to_list()

            # Generating plot widget
            plot = graph_layout.addPlot(col=0)
            plot.setMinimumSize(225, 225)

            # Set up the x-axis to display the time and date
            axis = DateAxisItem(orientation="bottom", is_standard=self._handler.is_standard_time)
            axis.attachToPlotItem(plot)

            # Add margins to the plot 30px
            plot.setContentsMargins(30, 30, 30, 30)

            # Random Pen Color
            pen_color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))

            # Plot the data
            plot.plot(x=date_range, y=y_axis, pen=pen_color, fillLevel=0, fillBrush=(150, 150, 150, 60))

            # display grid
            plot.showGrid(x=True, y=True)
            plot.setLabel("left", column)
            plot.setTitle(column)

            # Prevent zooming past the data
            plot.setLimits(xMin=start_date, xMax=end_date, yMin=min(y_axis), yMax=max(y_axis))

            # Add legend to the plot for the y-axis
            legend_y = pg.LegendItem((140, 60), offset=(70, 30))
            legend_y.setParentItem(plot.graphicsItem())
            legend_y.addItem(pg.PlotDataItem(pen=pen_color), column)

            # Increment the row
            graph_layout.nextRow()

        scroll_area = self._UI.graph_area
        scroll_area.setWidget(graph_layout)
        scroll_area.setWidgetResizable(True)
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)

    def populate_graph_all_subjects(self, record_count: int, subject_records: list[pd.DataFrame]):
        """_summary_

        Args:
            record_count (int): _description_
            record_list (list[pd.DataFrame]): _description_
        """

        # Set the graph layout height times the record count
        graph_layout = pg.GraphicsLayoutWidget()
        graph_layout.setFixedHeight(233 * record_count)

        # Saving the graph filter
        df_columns = self._handler.graph_filter

        # Subject colors:
        subject_colors = [(36, 158, 121), (179, 155, 215), (215, 239, 188)]
        brush_colors = [(36, 158, 121, 80), (179, 155, 215, 80), (215, 239, 188, 80)]
        self.sync_plots: list[pg.PlotItem] = []

        for column in df_columns:
            # Generating plot widget
            plot = graph_layout.addPlot(col=0)
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
                pen_color = subject_colors[color_index]

                # Plot the data
                legend_plot = None

                if column == "Movement intensity" or column == "Rest":
                    legend_plot = plot.plot(
                        x=date_range,
                        y=y_axis,
                        pen=None,
                        symbol=random.choice(["o", "t1", "t"]),
                        symbolPen=None,
                        symbolSize=10,
                        symbolBrush=brush_colors[color_index],
                    )
                elif column == "On Wrist":
                    # Bar graph
                    legend_plot = plot.plot(
                        x=date_range,
                        y=y_axis,
                        fillLevel=0,
                        fillBrush=brush_colors[color_index],
                        symbol="s",
                        symbolPen=None,
                        symbolSize=2,
                        symbolBrush=brush_colors[color_index],
                    )
                else:
                    legend_plot = plot.plot(
                        x=date_range + 1, y=y_axis, pen=pen_color, fillLevel=0, fillBrush=(150, 150, 150, 60)
                    )

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
            graph_layout.nextRow()

        # for plot in self.sync_plots:
        #     plot.sigRangeChanged.connect(self.onSigRangeChanged)

        # Take the middle date + half a day
        navigator_region_start = (end_date - start_date) / 2 + start_date - 21600
        navigator_region_end = navigator_region_start + 43200

        # Add a region to the first plot
        self.navigator = pg.LinearRegionItem([navigator_region_start, navigator_region_end])
        self.navigator.setBrush(pg.mkBrush(255, 255, 255, 100))
        self.navigator.setZValue(-10)
        self.sync_plots[0].addItem(self.navigator)

        # Assign it only to the first plot
        self.navigator.sigRegionChanged.connect(self.update_plots)
        # self.sync_plots[0].sigXRangeChanged.connect(self.update_navigator)

        # Add the graph_layout to the bottom_left_f
        bottom_graph_layout = pg.GraphicsLayoutWidget()
        bottom_graph_layout.setFixedHeight(153)

        navigator_plot = bottom_graph_layout.addPlot(row=0, col=0)
        navigator_plot.plot(
            x=self.sync_plots[0].getAxis("bottom").range, y=self.sync_plots[0].getAxis("left").range, pen="w"
        )
        # Set up the x-axis to display the time and date
        axis = DateAxisItem(orientation="bottom", is_standard=self._handler.is_standard_time)
        axis.attachToPlotItem(navigator_plot)
        navigator_plot.addItem(self.navigator)
        navigator_plot.setLimits(
            xMin=start_date,
            xMax=end_date,
            yMin=self.sync_plots[0].getAxis("left").range[0],
            yMax=self.sync_plots[0].getAxis("left").range[1],
        )
        navigator_plot.setTitle("Navigator")

        self._UI.bottom_left_f.layout().addWidget(bottom_graph_layout)

        scroll_area = self._UI.graph_area
        scroll_area.setWidget(graph_layout)
        scroll_area.setWidgetResizable(True)
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)

    def create_navigator_graph(self, date_range: list):
        """_summary_

        Args:
            records_df (pd.DataFrame): _description_
        """

        # Set the graph layout height times the record count
        graph_layout = pg.GraphicsLayoutWidget()
        graph_layout.setFixedHeight(self._UI.bottom_left_f.height())

        # Add graph_layout to the bottom_left_f
        self._UI.bottom_left_f.layout().addWidget(graph_layout)

    def update_plots(self):
        for g in self.sync_plots:
            if g != self.navigator:
                g.blockSignals(True)
                g.setXRange(*self.navigator.getRegion(), padding=0)
                g.blockSignals(False)

    def update_navigator(self):
        self.navigator.setRegion(self.sync_plots[0].getViewBox().viewRange()[0])

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


if __name__ == "__main__":
    plotting_handler = GraphPlotHandler()
