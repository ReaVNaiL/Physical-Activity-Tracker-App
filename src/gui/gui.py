from tkinter import *
from tkinter.filedialog import askopenfile
'''
Color Pallet Ref: https://colorhunt.co/palette/f7f7f7eeeeee393e46929aab
'''

#SETUP
window = Tk()
window.geometry("1920x1080")
window.title("Physical Activity Tracker")
window.config(bg="#F7F7F7") #background
window.iconbitmap("./assets/windowIcon.ico") #icon

def dataImport():
	file = askopenfile(parent=window, mode='r', title = "choose file", filetypes =[('Excel Files', '*.xlsm')])

#menu
menubar = Menu(window)
window.config(menu=menubar)

#Data Menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Data", menu=file_menu)
file_menu.add_command(label="Import", command=dataImport)

#analysis menu
timeSeries = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Analysis", menu=timeSeries)
timeSeries.add_command(label="Something")



window.mainloop()