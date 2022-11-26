
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
from numpy import random
from second_window import Ui_secondWindow


# class Canvas(FigureCanvas):
#     def __init__(self,parent):
#         fig, self.ax = plt.subplots(figuresize=(5,4), dpi=200)
#         super().__init__(fig)
#         self.setParent(parent)


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_secondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1755, 773)
        MainWindow.setStyleSheet("border-color: rgb(255, 255, 255);\n"
                                 "border-color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(213, 213, 213);\n"
                                 "font: 8pt \"Georgia\";\n"
                                 "background-image: url(C:\\Users\\samue\\OneDrive\\Documents\\350_Project\\911.png)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.right_column = QtWidgets.QFrame(self.centralwidget)
        self.right_column.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_column.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_column.setObjectName("right_column")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.right_column)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.right_column_top_box = QtWidgets.QFrame(
            self.right_column)  # graph location 2
        self.right_column_top_box.setObjectName("right_column_top_box")
        self.verticalLayout_2.addWidget(self.right_column_top_box)
        self.right_column_buttom_box = QtWidgets.QFrame(
            self.right_column)  # graph location 3
        self.right_column_buttom_box.setStyleSheet("")
        self.right_column_buttom_box.setObjectName("right_column_buttom_box")
        self.verticalLayout_2.addWidget(self.right_column_buttom_box)
        self.gridLayout.addWidget(self.right_column, 0, 1, 1, 1)
        self.left_column = QtWidgets.QFrame(self.centralwidget)
        self.left_column.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_column.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_column.setObjectName("left_column")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left_column)
        self.verticalLayout.setObjectName("verticalLayout")
        self.left_column_inner = QtWidgets.QFrame(self.left_column)
        self.left_column_inner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_column_inner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_column_inner.setObjectName("left_column_inner")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.left_column_inner)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.left_column_top_box = QtWidgets.QFrame(self.left_column_inner)
        self.left_column_top_box.setStyleSheet("font: 10pt \"Arial\";")
        self.left_column_top_box.setObjectName("left_column_top_box")
        self.frame = QtWidgets.QFrame(self.left_column_top_box)
        self.frame.setGeometry(QtCore.QRect(11, 11, 761, 56))
        self.frame.setObjectName("frame")
        self.left_column_top_box_button_container_1 = QtWidgets.QVBoxLayout(
            self.frame)
        self.left_column_top_box_button_container_1.setObjectName(
            "left_column_top_box_button_container_1")
        self.import_button = QtWidgets.QPushButton(self.frame)
        self.import_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.import_button.setObjectName("import_button")
        self.left_column_top_box_button_container_1.addWidget(
            self.import_button)
        self.clear_button = QtWidgets.QPushButton(self.frame)
        self.clear_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.clear_button.setObjectName("clear_button")
        self.left_column_top_box_button_container_1.addWidget(
            self.clear_button)
        self.frame1 = QtWidgets.QFrame(self.left_column_top_box)
        self.frame1.setGeometry(QtCore.QRect(14, 90, 71, 121))
        self.frame1.setObjectName("frame1")
        self.left_column_top_box_label_container = QtWidgets.QVBoxLayout(
            self.frame1)
        self.left_column_top_box_label_container.setObjectName(
            "left_column_top_box_label_container")
        self.index_label = QtWidgets.QLabel(self.frame1)
        self.index_label.setStyleSheet("font: 75 10pt \"Arial\";\n"
                                       "background-color: rgb(255, 255, 255);")
        self.index_label.setObjectName("index_label")
        self.left_column_top_box_label_container.addWidget(self.index_label)
        self.subject_label = QtWidgets.QLabel(self.frame1)
        self.subject_label.setStyleSheet("font: 75 10pt \"Arial\";\n"
                                         "background-color: rgb(255, 255, 255);")
        self.subject_label.setObjectName("subject_label")
        self.left_column_top_box_label_container.addWidget(self.subject_label)
        self.device_label = QtWidgets.QLabel(self.frame1)
        self.device_label.setStyleSheet("font: 75 10pt \"Arial\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.device_label.setObjectName("device_label")
        self.left_column_top_box_label_container.addWidget(self.device_label)
        self.date_label = QtWidgets.QLabel(self.frame1)
        self.date_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 87 10pt \"Arial\";")
        self.date_label.setObjectName("date_label")
        self.left_column_top_box_label_container.addWidget(self.date_label)
        self.frame2 = QtWidgets.QFrame(self.left_column_top_box)
        self.frame2.setGeometry(QtCore.QRect(10, 250, 761, 56))
        self.frame2.setObjectName("frame2")
        self.left_column_top_box_button_container_2 = QtWidgets.QVBoxLayout(
            self.frame2)
        self.left_column_top_box_button_container_2.setObjectName(
            "left_column_top_box_button_container_2")
        self.save_all_button = QtWidgets.QPushButton(
            self.frame2, clicked=lambda: self.openWindow())
        self.save_all_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.save_all_button.setObjectName("save_all_button")
        self.left_column_top_box_button_container_2.addWidget(
            self.save_all_button)
        self.index_list_box = QtWidgets.QListWidget(self.left_column_top_box)
        self.index_list_box.setGeometry(QtCore.QRect(91, 91, 671, 31))
        self.index_list_box.setObjectName("index_list_box")
        item = QtWidgets.QListWidgetItem()
        self.index_list_box.addItem(item)
        self.device_list_box = QtWidgets.QListWidget(self.left_column_top_box)
        self.device_list_box.setGeometry(QtCore.QRect(90, 150, 671, 31))
        self.device_list_box.setObjectName("device_list_box")
        item = QtWidgets.QListWidgetItem()
        self.device_list_box.addItem(item)
        self.subject_list_box = QtWidgets.QListWidget(self.left_column_top_box)
        self.subject_list_box.setGeometry(QtCore.QRect(91, 120, 671, 31))
        self.subject_list_box.setObjectName("subject_list_box")
        item = QtWidgets.QListWidgetItem()
        self.subject_list_box.addItem(item)
        self.frame3 = QtWidgets.QFrame(self.left_column_top_box)
        self.frame3.setGeometry(QtCore.QRect(90, 177, 671, 61))
        self.frame3.setObjectName("frame3")
        self.left_column_top_box_startDate_checkBox_container = QtWidgets.QGridLayout(
            self.frame3)
        self.left_column_top_box_startDate_checkBox_container.setObjectName(
            "left_column_top_box_startDate_checkBox_container")
        self.end_date = QtWidgets.QDateTimeEdit(self.frame3)
        self.end_date.setDateTime(QtCore.QDateTime(
            QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.end_date.setObjectName("end_date")
        self.left_column_top_box_startDate_checkBox_container.addWidget(
            self.end_date, 0, 1, 1, 1)
        self.start_date = QtWidgets.QDateTimeEdit(self.frame3)
        self.start_date.setDateTime(QtCore.QDateTime(
            QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.start_date.setObjectName("start_date")
        self.left_column_top_box_startDate_checkBox_container.addWidget(
            self.start_date, 0, 0, 1, 1)
        self.time_converter_check_box = QtWidgets.QCheckBox(self.frame3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.time_converter_check_box.setFont(font)
        self.time_converter_check_box.setObjectName("time_converter_check_box")
        self.left_column_top_box_startDate_checkBox_container.addWidget(
            self.time_converter_check_box, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.left_column_top_box)
        self.left_column_buttom_box = QtWidgets.QFrame(
            self.left_column_inner)  # Graph Location 1
        self.left_column_buttom_box.setObjectName("left_column_buttom_box")
        # Left column buttom box vancas
        # self.figure = plt.figure()
        # self.canvas = FigureCanvas(self.figure)
        # end of the canvas

        self.verticalLayout_4.addWidget(self.left_column_buttom_box)
        # self.verticalLayout_4.addWidget(self.canvas)

        self.verticalLayout.addWidget(self.left_column_inner)
        self.gridLayout.addWidget(self.left_column, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1755, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menuFile.setFont(font)
        self.menuFile.setAutoFillBackground(False)
        self.menuFile.setTearOffEnabled(False)
        self.menuFile.setSeparatorsCollapsible(True)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_button.setText(_translate("MainWindow", "Import Data"))
        self.clear_button.setText(_translate("MainWindow", "Clear Data"))
        self.index_label.setText(_translate("MainWindow", "Index"))
        self.subject_label.setText(_translate("MainWindow", "Subject"))
        self.device_label.setText(_translate("MainWindow", "Device"))
        self.date_label.setText(_translate("MainWindow", "Date range"))
        self.save_all_button.setText(_translate("MainWindow", "Select All"))
        __sortingEnabled = self.index_list_box.isSortingEnabled()
        self.index_list_box.setSortingEnabled(False)
        item = self.index_list_box.item(0)
        item.setText(_translate("MainWindow", "Metadata"))
        self.index_list_box.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.device_list_box.isSortingEnabled()
        self.device_list_box.setSortingEnabled(False)
        item = self.device_list_box.item(0)
        item.setText(_translate("MainWindow", "Options"))
        self.device_list_box.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.subject_list_box.isSortingEnabled()
        self.subject_list_box.setSortingEnabled(False)
        item = self.subject_list_box.item(0)
        item.setText(_translate("MainWindow", "All"))
        self.subject_list_box.setSortingEnabled(__sortingEnabled)
        self.time_converter_check_box.setText(
            _translate("MainWindow", "Standard Time"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
