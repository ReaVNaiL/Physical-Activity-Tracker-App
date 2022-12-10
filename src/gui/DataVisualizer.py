import os
from PyQt5 import QtWidgets
from src.DataHandler import DataHandler
from src.gui.MainWindow import UI_MainWindow
from src.gui.SecondWindow import UI_SecondWindow
from src.gui.AlertBox import AlertBox

from PyQt5.QtCore import Qt, QPoint, QDate, QTime, QDateTime, QEvent, pyqtSignal
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QGroupBox, QFormLayout, QListWidgetItem, QMessageBox, QFileDialog
from src.helpers.date_axis import DateAxisItem
from src.gui.GraphPlotHandler import GraphPlotHandler

import sys
import pyqtgraph as pg
import pandas as pd
import numpy as np
import random


class DataVisualizer:
    def __init__(self, handler: DataHandler) -> None:
        self._UI = UI_MainWindow()
        self._handler = handler

        # Create the plot handler
        self._plot_handler = GraphPlotHandler(self._UI, self._handler)

    def show(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self._UI.setupUi(self.MainWindow)
        self.MainWindow.setFixedSize(1755, 820)
        if sys.platform == "win32" or sys.platform == "win64" or sys.platform == "cygwin":
            self.MainWindow.setWindowFlags(Qt.FramelessWindowHint)
            self.MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.MainWindow.mouseMoveEvent = self._UI.mouse_move_event
        self.MainWindow.mousePressEvent = self._UI.mouse_press_event
        self.MainWindow.show()

        with open("src/gui/style/stylesheet.css", "r") as f:
            app.setStyleSheet(f.read())

        # This Adds The Second Window
        select_button = self._UI.select_button
        select_button.clicked.connect(self.open_helper_window)

        import_button = self._UI.import_button
        import_button.clicked.connect(self.import_data)
        
        clear_button = self._UI.clear_button
        clear_button.clicked.connect(self.clear_data)

        # Import Button
        self.populate_dropdowns()

        sys.exit(app.exec_())

    def open_helper_window(self):
        self.helper_window = QtWidgets.QMainWindow()
        self.helper_UI = UI_SecondWindow()
        self.helper_UI.setupUI(self.helper_window)
        self.helper_window.setWindowFlags(Qt.WindowStaysOnTopHint)
        if sys.platform == "win32" or sys.platform == "win64" or sys.platform == "cygwin":
            self.helper_window.setWindowFlags(Qt.FramelessWindowHint)
            self.helper_window.setAttribute(Qt.WA_TranslucentBackground)
            
        self.helper_window.setMaximumSize(825, 500)
        self.helper_window.setMinimumSize(825, 500)
        self.helper_window.mouseMoveEvent = self.helper_UI.mouse_move_event
        self.helper_window.mousePressEvent = self.helper_UI.mouse_press_event
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
        # self._UI.index_dropdown.addItem("metadata.csv")

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

        try:
            # Populate the right list with the list of items that are selected
            self.helper_UI.right_list.addItems(self._handler.graph_filter)
            # Remove the items from the left list
            for item in self._handler.graph_filter:
                self.helper_UI.left_list.takeItem(
                    self.helper_UI.left_list.row(self.helper_UI.left_list.findItems(item, Qt.MatchExactly)[0])
                )
        except:
            pass

        # Add Event Listeners for the arrows
        self.helper_UI.add_arrow.clicked.connect(self.helper_UI.add_item_to_right_list)
        self.helper_UI.remove_arrow.clicked.connect(self.helper_UI.add_item_to_left_list)

    def create_input_model(self, input = None, set_window = False):
        self._handler.file_index = self._UI.index_dropdown.currentText() if input == None else input.file_index
        self._handler.subject_id = self._UI.subject_dropdown.currentText() if input == None else input.subject_id
        self._handler.device_OS = self._UI.device_dropdown.currentText() if input == None else input.device_OS
        self._handler.is_standard_time = self._UI.time_converter_check_box.isChecked() if input == None else input.is_standard_time
        self._handler.start_date = self._UI.start_date.text() if input == None else input.start_date
        self._handler.end_date = self._UI.end_date.text() if input == None else input.end_date
        
        if set_window:
            self._UI.index_dropdown.setCurrentText(self._handler.file_index)
            self._UI.subject_dropdown.setCurrentText(self._handler.subject_id)
            self._UI.device_dropdown.setCurrentText(self._handler.device_OS)
            self._UI.time_converter_check_box.setChecked(self._handler.is_standard_time)
            self._UI.start_date.setDateTime(QDateTime.fromString(self._handler.start_date, "MM/dd/yyyy hh:mm A"))
            self._UI.end_date.setDateTime(QDateTime.fromString(self._handler.end_date, "MM/dd/yyyy hh:mm A"))
    
    def submit_data(self):
        """
        This function is called when the submit button is clicked in the helper window
        """
        if self.helper_UI.right_list.count() == 0:
            AlertBox("Alert!\n\nPlease select at least one column to graph.")
            return
        
        # Close the Helper Window
        self.helper_window.close()

        # Get the filtering into the DataHandler
        filters = self.helper_UI.get_filters()
        self._handler.graph_filter = filters

        if self._handler.subject_id == "All Subjects":
            subject_record_list = self._handler.process_all_subjects_data_filtering(filter_enabled=True)

            if not len(subject_record_list) == 0:
                # Populate the graph area
                self._plot_handler.populate_graph_all_subjects(len(subject_record_list[0].columns), subject_record_list)
                self._UI.graph_area.setVisible(True)
                return
        else:
            filtered_records = self._handler.process_data_filtering(filter_enabled=True)

            if not len(filtered_records) == 0:
                # Populate the graph area
                self._plot_handler.populate_graph_subjects(len(filtered_records.columns), filtered_records)
                self._UI.graph_area.setVisible(True)
                return
            
        AlertBox("Error!\n\nRecords not found for the given information...\nPlease try again with different values.")

    def import_data(self):
        """
        This function is called when the import button is clicked, it opens a file dialog and gets the file path
        Then it extracts the data from the file and populates the UI with the data.
        """
        
        # Create a QFileDialog
        file_dialog = QFileDialog()

        try:
            root_path = os.path.join(os.getcwd(), "data")

            # Get the file path ../data
            file_path = file_dialog.getOpenFileName(
                self.MainWindow, "Open File", root_path, "Summary CSV Files (summary.csv)"
            )
            print(file_path[0])

            # Get the date range from the file
            model = self._handler.extract_input_model(file_path[0])

            # set the model to the UI
            self.create_input_model(model, set_window=True)
            
            # Populate the helper window
            self.open_helper_window()
            
        except Exception as e:
            if e == AttributeError or e == IndexError:
                print("Error: ", e)
            else:
                print("Error: ", e)
            try:
                if e.errno == 2:
                    AlertBox("Error!\n\nA record was not selected. Please try again.")
            except:
                pass

    def clear_data(self):
        """
        This function is called when the clear button is clicked, it clears the UI and the data
        """
        self._plot_handler.CLEAR_PLOTS()
        self._UI.graph_area.setVisible(False)
        
if __name__ == "__main__":
    helper_UI = DataVisualizer()
    helper_UI.show()
