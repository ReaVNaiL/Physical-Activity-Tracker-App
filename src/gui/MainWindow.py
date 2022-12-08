from PyQt5 import QtCore, QtGui, QtWidgets


class UI_MainWindow(object):
    """Sets Up the `Main Window` with all the main properties.

    `Attributes`:

        `main_widget`: 
            The main widget that will be used to hold all the other widgets.

        `bottom_left_f`: 
            The bottom left frame will hold a histogram of the data.

        `right_f`: 
            The bottom right frame will hold a graph of the data and the data tables

        `top_left_f`: 
            The top frame will hold the dropdown menus and the time/date range.

        `frame_1`: 
            The first frame that will be used to hold the dropdown menu.

        `frame_2`: 
            The second frame that will be used to hold the time and date widgets.

        `frame_3`: 
            The third frame that will be used to hold the import and clear buttons.

        `layout_dropdown_widget`: 
            The layout that will be used to hold the dropdown menu widgets.

        `dropdown_menu`: 
            The dropdown menu that will be used to select the index, subject, and device.

        `time_dates_container`: 
            The container that will be used to hold the start and end date widgets.

        `start_date`: 
            The start date widget that will be used to select the start date.

        `end_date`: 
            The end date widget that will be used to select the end date.

        `time_converter_check_box`: 
            The check box that will be used to convert the time to a different time zone.

        `select_button`: 
            The select button that will be used to select the data.

        `select_button_container`: 
            The container that will be used to hold the select button.

        `import_button`: 
            The import button that will be used to import the data.

        `clear_button`: 
            The clear button that will be used to clear the data.

        `menu_bar`: 
            The menu bar that will be used to hold the menu items.

        `status_bar`: 
            The status bar that will be used to display the status of the program.

        `action_import`: 
            The import action that will be used to import the data.

        `action_exit`: 
            The exit action that will be used to exit the program.

        `action_save`: 
            The save action that will be used to save the data.

        `menu_file`:
            The file menu that will be used to hold the import, save, and exit actions.

    `Returns`:
        none
    """

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow

        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1755, 773)
        # self.MainWindow.setStyleSheet("")

        """"
        # Main Container
        """
        self.main_widget = QtWidgets.QWidget(self.MainWindow)
        # self.main_widget.setStyleSheet("")
        self.main_widget.setObjectName("main_widget")

        """
        # Main Frames (Containers)
        """
        self.bottom_left_f = QtWidgets.QFrame(self.main_widget)
        self.bottom_left_f.setGeometry(QtCore.QRect(50, 360, 381, 371))
        # self.bottom_left_f.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bottom_left_f.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_left_f.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_left_f.setObjectName("bottom_left_f")

        self.right_f = QtWidgets.QFrame(self.main_widget)
        self.right_f.setGeometry(QtCore.QRect(480, 10, 1251, 721))
        self.right_f.setStyleSheet("background-color: rgb(21,26,30);")
        self.right_f.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_f.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_f.setObjectName("right_f")

        self.top_left_f = QtWidgets.QFrame(self.main_widget)
        self.top_left_f.setGeometry(QtCore.QRect(9, 9, 471, 351))
        self.top_left_f.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_left_f.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_left_f.setObjectName("top_left_f")

        """
        # Graph Area
        """
        self.graph_area = QtWidgets.QScrollArea(self.right_f)
        self.graph_area.setGeometry(QtCore.QRect(10, 10, 1231, 701))
        self.graph_area.setStyleSheet("background-color: rgb(21,26,30);")
        self.graph_area.setWidgetResizable(True)
        self.graph_area.setObjectName("graph_area")

        """
        Widget Contents
        """
        self.graph_area_widget_contents = QtWidgets.QWidget()
        self.graph_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 1229, 699))
        self.graph_area_widget_contents.setObjectName("graph_area_widget_contents")
        self.graph_area_widget_contents.setStyleSheet("background-color: rgb(21,26,30);")
        self.graph_area.setWidget(self.graph_area_widget_contents)

        self.left_column_inner = QtWidgets.QFrame(self.top_left_f)
        self.left_column_inner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_column_inner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_column_inner.setObjectName("left_column_inner")

        """
        # Inner Frames
        """
        self.frame_1 = QtWidgets.QFrame(self.left_column_inner)
        self.frame_1.setGeometry(QtCore.QRect(0, 240, 401, 56))
        self.frame_1.setObjectName("frame_1")

        self.frame_2 = QtWidgets.QFrame(self.left_column_inner)
        self.frame_2.setGeometry(QtCore.QRect(90, 60, 341, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.frame_3 = QtWidgets.QFrame(self.left_column_inner)
        self.frame_3.setGeometry(QtCore.QRect(1, 1, 391, 56))
        self.frame_3.setObjectName("frame_3")

        """
        # Labels Frames
        """
        self.index_label = QtWidgets.QLabel(self.left_column_inner)
        self.index_label.setGeometry(QtCore.QRect(10, 70, 39, 16))
        self.index_label.setObjectName("index_label")

        self.date_range_label = QtWidgets.QLabel(self.left_column_inner)
        self.date_range_label.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.date_range_label.setObjectName("date_range_label")

        self.subject_label = QtWidgets.QLabel(self.left_column_inner)
        self.subject_label.setGeometry(QtCore.QRect(10, 100, 52, 16))
        self.subject_label.setObjectName("subject_label")

        self.device_label = QtWidgets.QLabel(self.left_column_inner)
        self.device_label.setGeometry(QtCore.QRect(10, 130, 41, 16))
        self.device_label.setObjectName("device_label")

        """
        # Layout Widget For Dropdown Menus
        """
        self.layout_dropdown_widget = QtWidgets.QWidget(self.frame_2)
        self.layout_dropdown_widget.setGeometry(QtCore.QRect(0, 10, 281, 80))
        self.layout_dropdown_widget.setObjectName("layout_dropdown_widget")

        """
        # Dropdown Menus
        """
        self.dropdown_menu = QtWidgets.QVBoxLayout(self.layout_dropdown_widget)
        self.dropdown_menu.setContentsMargins(0, 0, 0, 0)
        self.dropdown_menu.setObjectName("dropdown_menu")

        """
        # Dropdown Menu Items
        """
        self.index_dropdown = QtWidgets.QComboBox(self.layout_dropdown_widget)
        self.index_dropdown.setObjectName("index_dropdown")
        self.dropdown_menu.addWidget(self.index_dropdown)

        self.subject_dropdown = QtWidgets.QComboBox(self.layout_dropdown_widget)
        self.subject_dropdown.setObjectName("subject_dropdown")
        self.dropdown_menu.addWidget(self.subject_dropdown)

        self.device_dropdown = QtWidgets.QComboBox(self.layout_dropdown_widget)
        self.device_dropdown.setObjectName("device_dropdown")
        self.dropdown_menu.addWidget(self.device_dropdown)

        """
        # Time Dates Container
        """
        # Container
        self.time_dates_container = QtWidgets.QSplitter(self.frame_2)
        self.time_dates_container.setGeometry(QtCore.QRect(0, 100, 294, 20))
        self.time_dates_container.setOrientation(QtCore.Qt.Horizontal)
        self.time_dates_container.setObjectName("time_dates_container")

        # Start Date
        self.start_date = QtWidgets.QDateTimeEdit(self.time_dates_container)
        self.start_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 18), QtCore.QTime(0, 0, 0)))
        self.start_date.setObjectName("start_date")
        self.start_date.setDisplayFormat("MM/dd/yyyy hh:mm A")

        # End Date
        self.end_date = QtWidgets.QDateTimeEdit(self.time_dates_container)
        self.end_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 21), QtCore.QTime(0, 0, 0)))
        self.end_date.setObjectName("end_date")
        self.end_date.setDisplayFormat("MM/dd/yyyy hh:mm A")


        # Time Range
        self.time_converter_check_box = QtWidgets.QCheckBox(self.frame_2)
        self.time_converter_check_box.setGeometry(QtCore.QRect(0, 130, 121, 16))
        self.time_converter_check_box.setObjectName("time_converter_check_box")
        self.time_converter_check_box.setChecked(True)
        
        """
        # UI Buttons Container
        """
        # Frame 1
        self.select_button = QtWidgets.QPushButton(self.frame_1)
        # self.select_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.select_button.setObjectName("select_button")

        self.select_button_container = QtWidgets.QVBoxLayout(self.frame_1)
        self.select_button_container.setObjectName("select_button_container")
        self.select_button_container.addWidget(self.select_button)

        # Frame 2
        self.import_button = QtWidgets.QPushButton(self.frame_3)
        self.import_button.setGeometry(QtCore.QRect(9, 9, 381, 19))
        # self.import_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.import_button.setObjectName("import_button")

        # Frame 3
        self.clear_button = QtWidgets.QPushButton(self.frame_3)
        self.clear_button.setGeometry(QtCore.QRect(9, 31, 381, 19))
        # self.clear_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clear_button.setObjectName("clear_button")

        """
        # Menu Bar
        """
        self.menu_bar = QtWidgets.QMenuBar(self.MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1755, 21))
        self.menu_bar.setObjectName("menu_bar")

        self.status_bar = QtWidgets.QStatusBar(self.MainWindow)
        self.status_bar.setObjectName("status_bar")

        self.action_import = QtWidgets.QAction(self.MainWindow)
        self.action_import.setObjectName("action_import")

        self.action_exit = QtWidgets.QAction(self.MainWindow)
        self.action_exit.setObjectName("action_exit")

        self.action_save = QtWidgets.QAction(self.MainWindow)
        self.action_save.setObjectName("action_exit")

        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setAutoFillBackground(False)
        self.menu_file.setTearOffEnabled(False)
        self.menu_file.setSeparatorsCollapsible(True)
        self.menu_file.setObjectName("menu_file")
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_exit)
        self.menu_file.addSeparator()
        self.menu_bar.addAction(self.menu_file.menuAction())

        self.MainWindow.setCentralWidget(self.main_widget)
        self.MainWindow.setMenuBar(self.menu_bar)
        self.MainWindow.setStatusBar(self.status_bar)

        self.set_ui_naming(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def set_ui_naming(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        # Text Generation
        MainWindow.setWindowTitle(_translate("MainWindow", "Physical Activity Tracker"))
        self.select_button.setText(_translate("MainWindow", "Save"))
        self.time_converter_check_box.setText(_translate("MainWindow", "Standard Time"))
        self.device_label.setText(_translate("MainWindow", "Device"))
        self.subject_label.setText(_translate("MainWindow", "Subject  "))
        self.import_button.setText(_translate("MainWindow", "Import Data"))
        self.clear_button.setText(_translate("MainWindow", "Clear Data"))
        self.index_label.setText(_translate("MainWindow", "Index  "))
        self.date_range_label.setText(_translate("MainWindow", "Date Range"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.action_import.setText(_translate("MainWindow", "Import"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_save.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
