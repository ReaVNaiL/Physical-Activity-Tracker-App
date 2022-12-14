import os
from PyQt5.QtCore import QPoint
from PyQt5 import QtCore, QtGui, QtWidgets


class UI_SecondWindow(object):
    def setupUI(self, second_window):
        # Add a Font
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        
        self.second_window = second_window
        
        self.second_window_central_widget = QtWidgets.QWidget(self.second_window)
        self.second_window_central_widget.setObjectName("second_window_central_widget")
        
        # Create exit button
        self.exit_button = QtWidgets.QPushButton(self.second_window_central_widget)
        self.exit_button.setGeometry(QtCore.QRect(770, 10, 41, 41))
        self.exit_button.setObjectName("exit_button")
        pixmap = QtGui.QPixmap(os.path.join(os.getcwd(), "src", "gui", "assets", "exit_button.png"))
        self.exit_button.setIcon(QtGui.QIcon(pixmap))
        self.exit_button.clicked.connect(self.exit_button_clicked)
        self.exit_button.raise_()
        
        self.second_window_main_frame = QtWidgets.QFrame(self.second_window_central_widget)
        self.second_window_main_frame.setGeometry(QtCore.QRect(0, 30, 807, 421))
        self.second_window_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_window_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_window_main_frame.setObjectName("second_window_main_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.second_window_main_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.second_window_inner_frame_without_save = QtWidgets.QFrame(self.second_window_main_frame)
        self.second_window_inner_frame_without_save.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_window_inner_frame_without_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_window_inner_frame_without_save.setObjectName("second_window_inner_frame_without_save")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.second_window_inner_frame_without_save)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.second_window_left_colum_frame = QtWidgets.QFrame(self.second_window_inner_frame_without_save)
        self.second_window_left_colum_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_window_left_colum_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_window_left_colum_frame.setObjectName("second_window_left_colum_frame")

        self.horizontalLayout.addWidget(self.second_window_left_colum_frame)
        self.mid_frame_arrows = QtWidgets.QFrame(self.second_window_inner_frame_without_save)
        # self.mid_frame_arrows.setStyleSheet("")
        self.mid_frame_arrows.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mid_frame_arrows.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid_frame_arrows.setObjectName("mid_frame_arrows")
        self.layoutWidget_2 = QtWidgets.QWidget(self.mid_frame_arrows)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 100, 141, 70))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout.addWidget(self.mid_frame_arrows)
        self.second_window_right_column_frame = QtWidgets.QFrame(self.second_window_inner_frame_without_save)
        self.second_window_right_column_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.second_window_right_column_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.second_window_right_column_frame.setObjectName("second_window_right_column_frame")
        
        """
        Mid Section
        """
        self.add_arrow = QtWidgets.QPushButton(self.layoutWidget_2)
        self.add_arrow.setObjectName("middle_right_arrow")
        
        self.remove_arrow = QtWidgets.QPushButton(self.layoutWidget_2)
        self.remove_arrow.setObjectName("middle_left_arrow")
        
        self.arrow_frame = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.arrow_frame.setContentsMargins(0, 0, 0, 0)
        self.arrow_frame.setObjectName("arrow_frame")
        self.arrow_frame.addWidget(self.add_arrow)
        self.arrow_frame.addWidget(self.remove_arrow)
        
        self.submit_button = QtWidgets.QPushButton(self.mid_frame_arrows)
        self.submit_button.setGeometry(QtCore.QRect(50, 250, 139, 23))
        self.submit_button.setObjectName("submit_button")
        
        """
        Left Side Lists
        """
        self.left_list = QtWidgets.QListWidget(self.second_window_left_colum_frame)
        self.left_list.setGeometry(QtCore.QRect(10, 60, 241, 250))
        self.left_list.setObjectName("left_list")
        
        self.input_label = QtWidgets.QLabel(self.second_window_left_colum_frame)
        self.input_label.setGeometry(QtCore.QRect(100, 0, 150, 70))
        self.input_label.setObjectName("input_label")
        
        """
        Right Side Lists
        """
        self.right_list = QtWidgets.QListWidget(self.second_window_right_column_frame)
        self.right_list.setGeometry(QtCore.QRect(10, 60, 241, 250))
        self.right_list.setObjectName("right_list")

        self.display_label = QtWidgets.QLabel(self.second_window_right_column_frame)
        self.display_label.setGeometry(QtCore.QRect(100, 0, 150, 70))
        self.display_label.setObjectName("display_label")

        self.horizontalLayout.addWidget(self.second_window_right_column_frame)
        self.verticalLayout_4.addWidget(self.second_window_inner_frame_without_save)
        second_window.setCentralWidget(self.second_window_central_widget)
        self.statusbar = QtWidgets.QStatusBar(second_window)
        self.statusbar.setObjectName("statusbar")
        second_window.setStatusBar(self.statusbar)

        self.setFonts(font)
        self.retranslateUI(second_window)
        QtCore.QMetaObject.connectSlotsByName(second_window)

    def retranslateUI(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "Options"))
        self.input_label.setText(_translate("secondWindow", "Input"))
        self.add_arrow.setText(_translate("secondWindow", ">"))
        self.remove_arrow.setText(_translate("secondWindow", "<"))
        self.submit_button.setText(_translate("secondWindow", "Submit"))
        self.display_label.setText(_translate("secondWindow", "Display"))
    
    def setFonts(self, font):
        self.left_list.setFont(font)
        self.right_list.setFont(font)
        self.display_label.setFont(font)
        self.input_label.setFont(font)
        self.add_arrow.setFont(font)
        self.remove_arrow.setFont(font)
        self.submit_button.setFont(font)

    def get_filters(self) -> list[str]:
        # Get the filters from the right list
        filters = []
        for i in range(self.right_list.count()):
            filters.append(self.right_list.item(i).text())
        return filters
    
    def add_item_to_right_list(self):
        # Get the clicked item
        left_item = self.left_list.currentItem()

        # If there is item selected add it to the right list
        if left_item:
            self.right_list.addItem(left_item.text())
            self.left_list.takeItem(self.left_list.row(left_item))

    def add_item_to_left_list(self):
        # Get the clicked item
        right_item = self.right_list.currentItem()

        if right_item:
            self.left_list.addItem(right_item.text())
            self.right_list.takeItem(self.right_list.row(right_item))

    def exit_button_clicked(self):
        self.second_window.close()
        
    def mouse_press_event(self, event):
        try:
            self.old_pos = event.globalPos()
        except:
            pass
    def mouse_move_event(self, event):
        try:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.second_window.move(self.second_window.x() + delta.x(), self.second_window.y() + delta.y())
            self.old_pos = event.globalPos()
        except:
            pass
        
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    secondWindow = QtWidgets.QMainWindow()
    ui = UI_SecondWindow()
    secondWindow.setMaximumSize(821, 374)
    secondWindow.setMinimumSize(821, 374)
    ui.setupUI(secondWindow)
    secondWindow.show()
    sys.exit(app.exec_())
