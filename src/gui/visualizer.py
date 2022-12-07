from PyQt5 import QtWidgets
from DataHandler import DataHandler
from gui.MainWindow import UI_MainWindow
from gui.SecondWindow import UI_SecondWindow
from gui.models.InputModel import InputModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QGroupBox, QFormLayout, QListWidgetItem, QMessageBox
from helpers.date_axis import DateAxisItem

import sys
import pyqtgraph as pg
import pandas as pd
import matplotlib as plt
import numpy as np

class DataVisualizer:
    def __init__(self, handler: DataHandler) -> None:
        self._UI = UI_MainWindow()
        self._handler = handler

    def show(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self._UI.setupUi(self.MainWindow)
        self.MainWindow.show()
        pg.PlotWidget()

        # with open("src/gui/style/stylesheet.css", "r") as f:
        #     app.setStyleSheet(f.read())

        # This Adds The Second Window
        select_button = self._UI.select_button
        select_button.clicked.connect(self.open_helper_window)

        # Import Button
        self.populate_dropdowns()

        sys.exit(app.exec_())

    def open_helper_window(self):
        self.helper_window = QtWidgets.QMainWindow()
        self.helper_UI = UI_SecondWindow()
        self.helper_UI.setupUI(self.helper_window)
        self.helper_window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        self.helper_window.setMaximumSize(821, 374)
        self.helper_window.setMinimumSize(821, 374)
        self.helper_window.show()

        # Create the Input Model
        self.create_input_model()

        # Populate the helper window
        self.populate_helper_window()

        # Add the event listener for the import button
        self.helper_UI.submit_button.clicked.connect(self.submit_data)

    def populate_dropdowns(self):
        # Populate index box:
        self._UI.index_dropdown.addItem("summary.csv")
        self._UI.index_dropdown.addItem("metadata.csv")

        # Populate Subject box:
        self._UI.subject_dropdown.addItem("All Subjects")
        self._UI.subject_dropdown.addItem("310")
        self._UI.subject_dropdown.addItem("311")
        self._UI.subject_dropdown.addItem("312")

        # Populate device dropdown
        self._UI.device_dropdown.addItem("All Devices")
        self._UI.device_dropdown.addItem("Android")
        self._UI.device_dropdown.addItem("iOS")

    def populate_helper_window(self):
        """
        Populates the helper window with the data from the `InputModel` into the input fields
        """
        index = self._UI.index_dropdown.currentText()

        header_list = self._handler.get_headers(index)

        # Populate the list widget
        for header in header_list:
            item = QListWidgetItem(header)
            self.helper_UI.left_list.addItem(item)

        # Add Event Listeners for the arrows
        self.helper_UI.add_arrow.clicked.connect(self.helper_UI.add_item_to_right_list)
        self.helper_UI.remove_arrow.clicked.connect(self.helper_UI.add_item_to_left_list)

    def create_input_model(self):
        self._handler.file_index = self._UI.index_dropdown.currentText()
        self._handler.subject_id = self._UI.subject_dropdown.currentText()
        self._handler.device_OS = self._UI.device_dropdown.currentText()
        self._handler.is_standard_time = self._UI.time_converter_check_box.isChecked()
        self._handler.start_date = self._UI.start_date.text()
        self._handler.end_date = self._UI.end_date.text()

    def submit_data(self):
        """
        TBD
        """
        # Close the Helper Window
        self.helper_window.close()

        # Get the filtering into the DataHandler
        filters = self.helper_UI.get_filters()
        self._handler.graph_filter = filters

        # Get the data from the handler
        filtered_records = self._handler.process_data_filtering(filter_enabled=True)

        if len(filtered_records) == 0:
            QMessageBox.about(self.MainWindow, "Alert", "No Records Found!")
        else:
            # Populate the graph area
            # BUG: This is not working
            self.populate_graph_test(len(filtered_records.columns), filtered_records)

    # TEST METHODS
    def populate_graph_test(self, count: int, records_df: pd.DataFrame):
        """
        goal: generate graph location equal to the row count

        """
        formLayout = QFormLayout()
        groupBox = QGroupBox()
        plotWidget_list = []

        # Get the Unix Timestamp then drop it
        x_axis = records_df['Unix Timestamp (UTC)'].to_list()
        records_df = records_df.drop(columns=['Unix Timestamp (UTC)'])
        
        # Set the x-axis to seconds since epoch
        start_date = x_axis[0] / 1000
        end_date = x_axis[-1] / 1000
        date_range = np.linspace(start_date, end_date, len(x_axis))
        
        count = 0
        for column in records_df.columns:
            # setting y_axis
            y_axis = records_df[column].to_list()
            
            # Generating plot widget
            plot = pg.PlotWidget()
            plot.setMinimumSize(225, 225)
            
            # Set up the x-axis to display the time and date
            axis = DateAxisItem(orientation='bottom', is_standard=self._handler.is_standard_time)
            axis.attachToPlotItem(plot.getPlotItem())
            
            # Plot the data
            plot.plot(x=date_range, y=y_axis, randomPen=(count, count+1))
            
            # display grid
            plot.showGrid(x=True, y=True)
            plot.setLabel('left', column)
            plot.setTitle(column)
            
            plotWidget_list.append(plot)
            formLayout.addRow(plotWidget_list[count])
            count += 1
            
        groupBox.setLayout(formLayout)

        scroll_area = self._UI.graph_area
        scroll_area.setWidget(groupBox)
        scroll_area.setWidgetResizable(True)
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)


if __name__ == "__main__":
    helper_UI = DataVisualizer()
    helper_UI.show()
