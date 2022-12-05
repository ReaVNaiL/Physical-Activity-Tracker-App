import sys
import pyqtgraph as pg
from PyQt5 import QtWidgets
from gui.MainWindow import UI_MainWindow
from gui.SecondWindow import UI_SecondWindow
from DataHandler import DataHandler
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFormLayout,
    QVBoxLayout,
    QGroupBox,
    QFormLayout,
    QListWidgetItem,
)
from gui.models.InputModel import InputModel


class DataVisualizer:
    def __init__(self, handler: DataHandler) -> None:
        self._UI = UI_MainWindow()
        self._handler = handler

    def show(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self._UI.setupUi(MainWindow)
        MainWindow.show()

        # with open("src/gui/style/stylesheet.css", "r") as f:
        #     app.setStyleSheet(f.read())

        # This Adds The Second Window
        select_button = self._UI.select_button
        select_button.clicked.connect(self.open_helper_window)

        # Import Button
        self.populate_dropdowns()

        sys.exit(app.exec_())

    def open_helper_window(self):
        self.window = QtWidgets.QMainWindow()
        self.helper_UI = UI_SecondWindow()
        self.helper_UI.setupUi(self.window)
        self.window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        self.window.setMaximumSize(821, 374)
        self.window.setMinimumSize(821, 374)
        self.window.show()

        
        # Create the Input Model
        self.create_input_model()

        # Populate the helper window
        self.populate_helper_window()

    def populate_dropdowns(self):
        # Populate index box:
        self._UI.index_dropdown.addItem("summary.csv")
        self._UI.index_dropdown.addItem("metadata.csv")

        # Populate Subject box:
        self._UI.subject_dropdown.addItem("310")
        self._UI.subject_dropdown.addItem("311")
        self._UI.subject_dropdown.addItem("312")

        # Populate device dropdown
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
            self.helper_UI.second_window_header_list.addItem(item)

        # Add Event Listeners for the arrows
        self.helper_UI.middle_right_arrow.clicked.connect(self.helper_UI.add_item_to_right_list)
        self.helper_UI.middle_left_arrow.clicked.connect(self.helper_UI.add_item_to_left_list)

    def create_input_model(self):
        self._handler.file_index = self._UI.index_dropdown.currentText()
        self._handler.subject_id = self._UI.subject_dropdown.currentText()
        self._handler.device_OS = self._UI.device_dropdown.currentText()
        self._handler.is_standard_time = self._UI.time_converter_check_box.isChecked()
        self._handler.start_date = self._UI.start_date.text()
        self._handler.end_date = self._UI.end_date.text()

    # TEST METHODS
    def populate_graph_test(self, count: int):
        """
        goal: generate graph location equal to the row count

        """
        formLayout = QFormLayout()
        groupBox = QGroupBox()
        plotWidget_list = []
        for i in range(count):
            y = [1, 2, 3]
            y2 = [2, 3, 4]

            plot = pg.PlotWidget()
            plot.setMinimumSize(225, 225)
            plot.plot(y, y2, pen="r")
            plotWidget_list.append(plot)
            formLayout.addRow(plotWidget_list[i])

        groupBox.setLayout(formLayout)

        scroll_area = self._UI.graph_area
        scroll_area.setWidget(groupBox)
        scroll_area.setWidgetResizable(True)
        layout = QVBoxLayout()
        layout.addWidget(scroll_area)


if __name__ == "__main__":
    helper_UI = DataVisualizer()
    helper_UI.show()
