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
        df.plot(x="Datetime (UTC)", y=["Temp avg"])
        plt.show()
    else:
        isLoaded = False
    return isLoaded
def window_close():
    root.quit()
    
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
        file_menu.add_command(label="Exit", command=window_close)

        # analysis menu
        timeSeries = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Analysis", menu=timeSeries)
        timeSeries.add_command(label="Something")

        # button = Button(root, text="Import CSV", command=import_csv)
        # button.pack()
        # self.add_button("Import CSV", import_csv)
        
        # Labels:
        options_label = self.add_label("Options", font=("Arial", 16))
        self.frame_in_screen(options_label,1,0,(20,20),(20,20))

        #Stat Date Label and input box
        date_start_label = self.add_label("Start Date\t")
        self.frame_in_screen(date_start_label,2,0)
        date_start_label_box = self.add_input_box(root)
        self.frame_in_screen(date_start_label_box,2,1)
        
        #spacing between two labels
        # empty_spaces = self.create_empty_space(9)
        # for elem in empty_spaces:
        #     self.frame_in_screen(elem, self.grid_x, self.grid_y)
        #     self.grid_x += 1

        #End Date Label and input box
        date_ends_label = self.add_label("End Date\t")
        self.frame_in_screen(date_ends_label,3,0,(20,20),(20,20))
        date_ends_label_box = self.add_input_box(root)
        self.frame_in_screen(date_ends_label_box,3,1)
        
        utc_date_label = self.add_label("Status")
        self.frame_in_screen(utc_date_label,4,0)

        # on = Image("/assets/on.png") 
        # off = Image("/assets/off.png")

        # status = on
        # button = Button(root, image = self.button_switch_action(on,off,status) , bd = 0)
        ''' 
        Framing:

        empty_spaces = self.create_empty_space(9)

        for elem in empty_spaces:
            self.frame_in_screen(elem, self.grid_x, self.grid_y)
            self.grid_x += 1
        '''
        
        
        # self.frame_in_screen(empty_spaces[0], 0, 0)
        # self.frame_in_screen(empty_spaces[1], 1, 0)
        
        
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

    def button_switch_action(self,imageOn, imageOff, status):
        # Create A Button
        #on_button = Button(root, image = on, bd = 0,command = switch)
        #on_button.pack(pady = 50)

        if status:
            return imageOn
        else:
            return imageOff
                