import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMessageBox

class AlertBox:
    def __init__(self, message: str) -> None:
        self.box = QMessageBox()
        self.box.setText(message)
        self.box.setStandardButtons(QMessageBox.Ok)
        
        # if os is Windows set the FramelessWindowHint
        if sys.platform == "win32" or sys.platform == "win64" or sys.platform == "cygwin":    
            self.box.setWindowFlags(Qt.FramelessWindowHint)
        
        # Make the window moveable
        self.box.mousePressEvent = self.mouse_press_event
        self.box.mouseMoveEvent = self.mouse_move_event
        
        self.box.exec_()
        
        
    def mouse_press_event(self, event):
        try:
            self.old_pos = event.globalPos()
        except:
            pass
    def mouse_move_event(self, event):
        try:
            delta = QPoint (event.globalPos() - self.old_pos)
            self.box.move(self.box.x() + delta.x(), self.box.y() + delta.y())
            self.old_pos = event.globalPos()
        except:
            pass
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    alert = AlertBox("No File Selected!")
    sys.exit(app.exec_())
