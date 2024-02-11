#contact app
import math
from math import ceil
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x800')
        Style().configure('TNotebook', tabposition='s')  # Repositions the notebook header
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand='True')

        self.tab_1()

        # Run
        self.mainloop()

    def tab_1(self):  # Define a method to create the first tab (call logs)
        # Create a frame for the first tab
        self.frame_tab_1 = ttk.Frame(self.notebook)
        self.frame_tab_1.pack(fill='both', expand=True)

        # Add the frame to the notebook with the text 'call log'
        self.notebook.add(self.frame_tab_1, text='call log')

        # Configure rows for the call log frame
        for i in range(4):
            self.frame_tab_1.rowconfigure(i, weight=1, uniform='a')

        # Configure the first column to expand
        self.frame_tab_1.columnconfigure(0, weight=1, uniform='a')

        # Create multiple log entries and add them to the grid
        logs = [self.tab_1_logs() for i in range(4)]
        for i, log in enumerate(logs):
            # Use grid to place each log entry in a row and column
            log.grid(row=i, column=0, sticky='nsew')

    def tab_2(self):
        self.frame_tab_2 = ttk.Frame(self.notebook)
        self.frame_tab_2.pack(fill='both', expand='True')

    def tab_3(self):
        self.frame_tab_3 = ttk.Frame(self.notebook)
        self.frame_tab_3.pack(fill='both', expand='True')

    def tab_1_logs(self):
        self.frame_log = ttk.Frame(self.frame_tab_1)
        self.update()
        self.frame_log.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        self.frame_log.rowconfigure((0, 1), weight=1, uniform='a')
        self.sub_frame1(self.frame_log).grid(row=0, column=0, rowspan=2, sticky='nsew')
        self.sub_frame2(self.frame_log).grid(row=0, column=1, columnspan=3, sticky='nsew')
        self.sub_frame3(self.frame_log).grid(row=1, column=1, sticky='nsew')
        self.sub_frame4(self.frame_log).grid(row=1, column=2, sticky='nsew')
        self.sub_frame5(self.frame_log).grid(row=1, column=3, sticky='nsew')
        self.sub_frame6(self.frame_log).grid(row=0, column=4, rowspan=2, sticky='nsew')
        return self.frame_log

    def sub_frame1(self, parent):  # Create a subframe with a canvas and display an image
        subframe_1 = ttk.Frame(parent)

        # Create a canvas within the subframe
        canvas = tk.Canvas(subframe_1)
        canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Load the image and store a reference to it
        self.image = tk.PhotoImage(file=r"C:\Python\GUI_Tutorial\icons\contact_icon.png")

        # Bind an event to call a method after the window has been rendered
        canvas.bind("<Configure>", lambda event, c=canvas, i=self.image: self.on_window_resize(event, c, i))

        return subframe_1

    def on_window_resize(self, event, canvas, image):
        # This method will be called after the window has been rendered

        # Get the actual width and height of the canvas
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        # Resize the image to fit the canvas
        resized_image = image.subsample(
            ceil(image.width() / canvas_width),
            ceil(image.height() / canvas_height)
        )

        # Coordinates for placing the image at the center of the canvas
        x, y = canvas_width / 2, canvas_height / 2

        # Create an oval (optional)
        # radius = 10
        # canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='', outline='')

        # Clear existing items on the canvas
        canvas.delete("all")

        # Create image on the canvas
        canvas.create_image(x, y, image=resized_image)

        # Debug information about window, frame, and canvas sizes
        print(f"Canvas width: {canvas_width}, Canvas height: {canvas_height}")
        print(f"Resized image width: {resized_image.width()}, Resized image height: {resized_image.height()}")
    
    def sub_frame2(self, parent):       #name\number
        self.subframe_2= ttk.Frame(parent)      
        ttk.Label(self.subframe_2,background='blue').place(relx=0, rely=0,relheight=1,relwidth=1)
        return self.subframe_2
    
    def sub_frame3(self, parent):       #incoming\outgoing
        self.subframe_3= ttk.Frame(parent)      
        ttk.Label(self.subframe_3,background='grey').place(relx=0, rely=0,relheight=1,relwidth=1)
        return self.subframe_3
    
    def sub_frame4(self, parent):       #country
        self.subframe_4= ttk.Frame(parent)      
        ttk.Label(self.subframe_4,background='yellow').place(relx=0, rely=0,relheight=1,relwidth=1)
        return self.subframe_4
        
    def sub_frame5(self, parent):       #date
        self.subframe_5= ttk.Frame(parent)      
        ttk.Label(self.subframe_5,background='green').place(relx=0, rely=0,relheight=1,relwidth=1)
        return self.subframe_5
    
    def sub_frame6(self, parent):       #call icon
        self.subframe_6= ttk.Frame(parent)      
        ttk.Label(self.subframe_6,background='brown').place(relx=0, rely=0,relheight=1,relwidth=1)
        return self.subframe_6        

App()
