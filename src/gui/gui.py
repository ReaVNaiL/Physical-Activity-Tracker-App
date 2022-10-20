from tkinter import *
from tkinter.filedialog import askopenfile
import pandas as pd
import matplotlib.pyplot as plt

'''
Color Pallet Ref: https://colorhunt.co/palette/f7f7f7eeeeee393e46929aab
'''

''' 
Global Variables Root
'''
root = Tk()


def import_csv() -> bool:
    file = askopenfile(parent=root, mode='r', title="choose file", filetypes=[
        ('Excel Files', '*.csv')])
    if (file):
        isLoaded = True
        df = pd.read_csv(file)
        df.plot(x="Datetime (UTC)", y=["Acc magnitude avg"])
        plt.show()
    else:
        isLoaded = False
    return isLoaded


class MainWindow():
    """ This will not build, it's just a placeholder """
    menu_bar = Menu(root)

    def __init__(self, height, width, name, color="#F7F7F7"):
        self.set_window(height, width, name, color)
        self.resize(800, 600)
        
        # menu
        root.config(menu=self.menu_bar)

        # Data Menu
        file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Data", menu=file_menu)
        file_menu.add_command(
            label="Options about Data will be added here", command=import_csv)

        # analysis menu
        timeSeries = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Analysis", menu=timeSeries)
        timeSeries.add_command(label="Something")

        # button = Button(root, text="Import CSV", command=import_csv)
        # button.pack()

    def set_window(self, height, width, name, color):
        '''
        Sets up the window with the given parameters
        '''
        self.resize(height, width)
        root.title(name)
        root.configure(bg=color)

        # root.title("Physical Activity Tracker")
        # root.config(bg="#F7F7F7")  # background
        # root.iconbitmap("./assets/windowIcon.ico") #icon

    def resize(self, height, width):
        '''
        Resizes the window
        '''
        root.geometry(f"{height}x{width}")
    
    def show(self):
        '''
        Shows the window
        '''
        root.mainloop()
    

        



