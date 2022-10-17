from tkinter import *
from tkinter.filedialog import askopenfile
import pandas as pd
import matplotlib.pyplot as plt
'''
Color Pallet Ref: https://colorhunt.co/palette/f7f7f7eeeeee393e46929aab
'''

#SETUP
root = Tk()
root.geometry("400x500")
root.title("Physical Activity Tracker")
root.config(bg="#F7F7F7") #background
root.iconbitmap("./assets/windowIcon.ico") #icon


def loadCSV() -> bool:
	file = askopenfile(parent=root, mode='r', title = "choose file", filetypes =[('Excel Files', '*.csv')])
	if(file):
		isLoaded = True
		df = pd.read_csv(file)
		df.plot(x="Datetime (UTC)", y = ["Acc magnitude avg"])
		plt.show()
	else:
		isLoaded = False
	return isLoaded
		
#menu
menubar = Menu(root)
root.config(menu=menubar)

#Data Menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Data", menu=file_menu)
file_menu.add_command(label="Options about Data will be added here", command=loadCSV)

#analysis menu
timeSeries = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Analysis", menu=timeSeries)
timeSeries.add_command(label="Something")

button = Button(root, text="Import CSV", command = loadCSV)
button.pack()




root.mainloop()