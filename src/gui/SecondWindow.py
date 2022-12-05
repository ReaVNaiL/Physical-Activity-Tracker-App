from PyQt5 import QtCore, QtGui, QtWidgets


class UI_SecondWindow(object):
    def setupUi(self, secondWindow):
        secondWindow.setObjectName("secondWindow")
        secondWindow.resize(821, 374)
        secondWindow.setMaximumSize(QtCore.QSize(821, 374))
        self.second_window_central_widget = QtWidgets.QWidget(secondWindow)
        self.second_window_central_widget.setObjectName("second_window_central_widget")
        self.second_window_main_frame = QtWidgets.QFrame(
            self.second_window_central_widget
        )
        self.second_window_main_frame.setGeometry(QtCore.QRect(0, 10, 811, 421))
        self.second_window_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_window_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_window_main_frame.setObjectName("second_window_main_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.second_window_main_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.second_window_inner_frame_without_save = QtWidgets.QFrame(
            self.second_window_main_frame
        )
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.second_window_inner_frame_without_save.setFont(font)
        self.second_window_inner_frame_without_save.setFrameShape(
            QtWidgets.QFrame.StyledPanel
        )
        self.second_window_inner_frame_without_save.setFrameShadow(
            QtWidgets.QFrame.Raised
        )
        self.second_window_inner_frame_without_save.setObjectName(
            "second_window_inner_frame_without_save"
        )
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.second_window_inner_frame_without_save
        )
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.second_window_left_colum_frame = QtWidgets.QFrame(
            self.second_window_inner_frame_without_save
        )
        self.second_window_left_colum_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_window_left_colum_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_window_left_colum_frame.setObjectName(
            "second_window_left_colum_frame"
        )
        self.second_window_header_list = QtWidgets.QListWidget(
            self.second_window_left_colum_frame
        )
        self.second_window_header_list.setGeometry(QtCore.QRect(10, 20, 241, 281))
        self.second_window_header_list.setStyleSheet("background-color: rgb(255, 255, 255);\n" 'font: 12pt "Arial";')
        self.second_window_header_list.setObjectName("second_window_header_list")
        self.label_2 = QtWidgets.QLabel(self.second_window_left_colum_frame)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 47, 13))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.second_window_left_colum_frame)
        self.second_window_arrow_button_frame = QtWidgets.QFrame(
            self.second_window_inner_frame_without_save
        )
        self.second_window_arrow_button_frame.setStyleSheet("")
        self.second_window_arrow_button_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel
        )
        self.second_window_arrow_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_window_arrow_button_frame.setObjectName(
            "second_window_arrow_button_frame"
        )
        self.layoutWidget_2 = QtWidgets.QWidget(self.second_window_arrow_button_frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 110, 141, 83))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.middle_arrows_frame = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.middle_arrows_frame.setContentsMargins(0, 0, 0, 0)
        self.middle_arrows_frame.setObjectName("middle_arrows_frame")
        self.middle_right_arrow = QtWidgets.QPushButton(self.layoutWidget_2)
        self.middle_right_arrow.setObjectName("middle_right_arrow")
        self.middle_arrows_frame.addWidget(self.middle_right_arrow)
        self.middle_left_arrow = QtWidgets.QPushButton(self.layoutWidget_2)
        self.middle_left_arrow.setObjectName("middle_left_arrow")
        self.middle_arrows_frame.addWidget(self.middle_left_arrow)
        self.pushButton = QtWidgets.QPushButton(self.second_window_arrow_button_frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 270, 139, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.second_window_arrow_button_frame)
        self.second_window_right_column_frame = QtWidgets.QFrame(
            self.second_window_inner_frame_without_save
        )
        self.second_window_right_column_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel
        )
        self.second_window_right_column_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_window_right_column_frame.setObjectName(
            "second_window_right_column_frame"
        )
        self.second_window_middle_list = QtWidgets.QListWidget(
            self.second_window_right_column_frame
        )
        self.second_window_middle_list.setGeometry(QtCore.QRect(10, 20, 241, 281))
        self.second_window_middle_list.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" 'font: 12pt "Arial";'
        )
        self.second_window_middle_list.setObjectName("second_window_middle_list")
        self.label = QtWidgets.QLabel(self.second_window_right_column_frame)
        self.label.setGeometry(QtCore.QRect(100, 0, 47, 20))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.second_window_right_column_frame)
        self.verticalLayout_4.addWidget(self.second_window_inner_frame_without_save)
        secondWindow.setCentralWidget(self.second_window_central_widget)
        self.statusbar = QtWidgets.QStatusBar(secondWindow)
        self.statusbar.setObjectName("statusbar")
        secondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(secondWindow)
        QtCore.QMetaObject.connectSlotsByName(secondWindow)

    def retranslateUi(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "Options"))
        self.label_2.setText(_translate("secondWindow", "Input"))
        self.middle_right_arrow.setText(_translate("secondWindow", ">"))
        self.middle_left_arrow.setText(_translate("secondWindow", "<"))
        self.pushButton.setText(_translate("secondWindow", "Save"))
        self.label.setText(_translate("secondWindow", "Output"))

    def add_item_to_right_list(self):
        # Get the clicked item
        left_item = self.second_window_header_list.currentItem()

        if left_item:
            # Add the item to the middle list
            self.second_window_middle_list.addItem(left_item.text())
            
            # Remove the item from the header list
            self.second_window_header_list.takeItem(self.second_window_header_list.row(left_item))
            
    def add_item_to_left_list(self):
        # Get the clicked item
        right_item = self.second_window_middle_list.currentItem()

        if right_item:
            # Add the item to the header list
            self.second_window_header_list.addItem(right_item.text())
            # Remove the item from the middle list
            self.second_window_middle_list.takeItem(self.second_window_middle_list.row(right_item))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondWindow = QtWidgets.QMainWindow()
    ui = UI_SecondWindow()
    ui.setupUi(secondWindow)
    secondWindow.show()
    sys.exit(app.exec_())
