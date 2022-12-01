from PyQt5 import QtCore, QtGui, QtWidgets
from SecondWindow import Ui_secondWindow


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_secondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1755, 773)
        MainWindow.setStyleSheet("")

        """"
        # Main Container
        """
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setStyleSheet("")
        self.main_widget.setObjectName("main_widget")


        """
        # Main Frames (Containers)
        """
        self.bottom_left_f = QtWidgets.QFrame(self.main_widget)
        self.bottom_left_f.setGeometry(QtCore.QRect(50, 360, 381, 371))
        self.bottom_left_f.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bottom_left_f.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_left_f.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_left_f.setObjectName("bottom_left_f")

        self.right_f = QtWidgets.QFrame(self.main_widget)
        self.right_f.setGeometry(QtCore.QRect(480, 10, 1251, 721))
        self.right_f.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        self.graph_area.setWidgetResizable(True)
        self.graph_area.setObjectName("graph_area")


        """
        Widget Contents
        """
        self.graph_area_widget_contents = QtWidgets.QWidget()
        self.graph_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 1229, 699))
        self.graph_area_widget_contents.setObjectName("graph_area_widget_contents")
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
        self.layout_dropdown_widget.setObjectName("layoutWidget_2")
        
        
        """
        # Dropdown Menus
        """
        self.dropdown_menu = QtWidgets.QVBoxLayout(self.layout_dropdown_widget)
        self.dropdown_menu.setContentsMargins(0, 0, 0, 0)
        self.dropdown_menu.setObjectName("dropdown_menu")
        
        
        """
        # Dropdown Menu Items
        """
        self.device_dropdown = QtWidgets.QComboBox(self.layout_dropdown_widget)
        self.device_dropdown.setObjectName("device_dropdown")
        self.dropdown_menu.addWidget(self.device_dropdown)
        
        self.index_dropdown = QtWidgets.QComboBox(self.layout_dropdown_widget)
        self.index_dropdown.setObjectName("index_dropdown")
        self.dropdown_menu.addWidget(self.index_dropdown)
        
        self.subject_dropdown = QtWidgets.QComboBox(self.layout_dropdown_widget)
        self.subject_dropdown.setObjectName("subject_dropdown")
        self.dropdown_menu.addWidget(self.subject_dropdown)
        
        
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
        self.start_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.start_date.setObjectName("start_date")
        
        # End Date
        self.end_date = QtWidgets.QDateTimeEdit(self.time_dates_container)
        self.end_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.end_date.setObjectName("end_date")
        
        # Time Range
        self.time_converter_check_box = QtWidgets.QCheckBox(self.frame_2)
        self.time_converter_check_box.setGeometry(QtCore.QRect(0, 130, 121, 16))
        self.time_converter_check_box.setObjectName("time_converter_check_box")


        """
        # UI Buttons Container
        """
        # Frame 1
        self.select_button = QtWidgets.QPushButton(self.frame_1)
        self.select_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.select_button.setObjectName("save_all_button_3")
        
        self.select_button_container = QtWidgets.QVBoxLayout( self.frame_1)
        self.select_button_container.setObjectName("select_button_container")
        self.select_button_container.addWidget(self.select_button)

        # Frame 2
        self.import_button = QtWidgets.QPushButton(self.frame_3)
        self.import_button.setGeometry(QtCore.QRect(9, 9, 381, 16))
        self.import_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.import_button.setObjectName("import_button")
        
        # Frame 3
        self.clear_button = QtWidgets.QPushButton(self.frame_3)
        self.clear_button.setGeometry(QtCore.QRect(9, 31, 381, 16))
        self.clear_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clear_button.setObjectName("clear_button")


        """
        # Menu Bar
        """
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1755, 21))
        self.menu_bar.setObjectName("menubar")

        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("statusbar")
        
        self.action_import = QtWidgets.QAction(MainWindow)
        self.action_import.setObjectName("actionImport")
        
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("actionExit")
        
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.menuFile = QtWidgets.QMenu(self.menu_bar)
        self.menuFile.setAutoFillBackground(False)
        self.menuFile.setTearOffEnabled(False)
        self.menuFile.setSeparatorsCollapsible(True)
        self.menuFile.setObjectName("menuFile")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.action_exit)
        self.menuFile.addSeparator()
        self.menu_bar.addAction(self.menuFile.menuAction())
        
        MainWindow.setCentralWidget(self.main_widget)
        MainWindow.setMenuBar(self.menu_bar)
        MainWindow.setStatusBar(self.status_bar)
        
        self.set_ui_naming(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_ui_naming(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        # Text Generation
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_button.setText(_translate("MainWindow", "Save"))
        self.time_converter_check_box.setText(_translate("MainWindow", "Standard Time"))
        self.device_label.setText(_translate("MainWindow", "Device"))
        self.subject_label.setText(_translate("MainWindow", "Subject  "))
        self.import_button.setText(_translate("MainWindow", "Import Data"))
        self.clear_button.setText(_translate("MainWindow", "Clear Data"))
        self.index_label.setText(_translate("MainWindow", "Index  "))
        self.date_range_label.setText(_translate("MainWindow", "Date Range"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_import.setText(_translate("MainWindow", "Import"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
