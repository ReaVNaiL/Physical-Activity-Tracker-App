from tkinter import *
import tkinter
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
    grid_x = 0
    grid_y = 0

    def __init__(self, height, width, name, color="#F7F7F7"):
        self.set_window(height, width, name, color)
        self.resize(800, 600)
        
        # menu
        root.config(menu=self.menu_bar)

        # Data Menu
        file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(
            label="Open", command=import_csv)

        # analysis menu
        timeSeries = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Analysis", menu=timeSeries)
        timeSeries.add_command(label="Something")

        # button = Button(root, text="Import CSV", command=import_csv)
        # button.pack()
        # self.add_button("Import CSV", import_csv)
        # Labels:
        testing = self.add_label("Date Start")
        testing2 = self.add_label("Date Ends")
        testing_box = self.add_input_box(root, 0, 1)
        sam = self.add_label("\tSam")
        sam_box = self.add_input_box(root)
        options_label = self.add_label("Date Ends")
        
        # # Framing:
        # empty_spaces = self.create_empty_space(9)

        # for elem in empty_spaces:
        #     self.frame_in_screen(elem, self.grid_x, self.grid_y)
        #     self.grid_x += 1
        
        # self.frame_in_screen(empty_spaces[0], 0, 0)
        # self.frame_in_screen(empty_spaces[1], 1, 0)
        self.grid_y += 1
        self.frame_in_screen(testing, self.grid_x, 0, padx=(150, 150), pady=(150, 150))
        # testing.grid(padx=(150, 150), pady=(150, 150)) 
        self.grid_y += 1
        self.frame_in_screen(testing_box, self.grid_x, 1)
        self.grid_y += 1
        self.frame_in_screen(testing2, self.grid_x, self.grid_y)
        self.grid_y += 1
        self.frame_in_screen(sam, self.grid_x+1, 0)
        self.frame_in_screen(sam_box, self.grid_x+1, 1)
        

        
        # testing.pack()

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
    
    def add_button(self, text, command, color="#F7F7F7", font=("Arial", 12), width=15, height=2):
        '''
        Adds a button to the window
        @param text: The text to be displayed on the button
        @param command: The command to be executed when the button is clicked
        @param color: The color of the button
        @param font: The font of the text
        @param width: The width of the button
        @param height: The height of the button
        '''
        button = Button(root, text=text, command=command, bg=color, font=font, width=width, height=height)
        return button
        
    def add_label(self, text, color="#F7F7F7", font=("Arial", 12)):
        '''
        Adds a label to the window
        @param text: The text to be displayed on the label
        @param color: The color of the text
        @param font: The font of the text
        '''
        label = Label(root, text=text, bg=color, font=font)
        return label
        
    def add_menu(self, menu, options):
        '''
        Adds a menu to the window
        @param menu: The menu to be added
        '''
        return self.menu_bar.add_cascade(label=menu, menu=options)
        
    def add_input_box(self, parent, pos_x = 0, pos_y = 0):
        '''
        Adds a text input
        '''
        new_entry = Entry(parent)
        self.frame_in_screen(new_entry, pos_x, pos_y)
        return new_entry

    def frame_in_screen(self, element, pos_x = 0, pos_y = 0, padx=(0,0), pady=(0,0)):
        '''
        Call
        @param element: parent element
        @param pos_x: The pos_x
        @param pos_y: The pos_y
        @param padx: Padding for the left and right of X
        @param pady: Padding for the top and right of Y
        '''
        element.grid(row=pos_x, column=pos_y, padx=padx, pady=pady)
        
    def create_empty_space(self, amount: int) -> list[Label]:
        empty = []
        
        for i in range(amount):
            empty.append(self.add_label("", font=("Arial", 16)))
        
        return empty