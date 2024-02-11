
#contact app
from datetime import datetime
from math import ceil
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from PIL import Image, ImageTk
import ttkbootstrap as tttk
from faker import Faker
import random

class App(tttk.Window):
    def __init__(self):
        super().__init__()
        self.geometry('450x700')
        style= tttk.Style()
        style.theme_use('darkly')
        style.configure('TNotebook', tabposition='s') #repositions the notebook header
        self.notebook= ttk.Notebook(self)
        self.notebook.pack(fill= 'both', expand= 'True')
        self.day= int(datetime.now().strftime("%d"))
        self.tab_1()

        #run
        self.mainloop()

    def tab_1(self):  # Define a method to create the first tab (call logs)
        # Create a frame for the first tab
        self.frame_tab_1 = ttk.Frame(self.notebook)
        self.frame_tab_1.pack(fill='both', expand=True)

        # Add the frame to the notebook with the text 'call log'
        self.notebook.add(self.frame_tab_1, text='call log')

        # Configure rows for the call log frame
        for i in range(8):
            self.frame_tab_1.rowconfigure(i, weight=1, uniform='a')

        # Configure the first column to expand
        self.frame_tab_1.columnconfigure(0, weight=1, uniform='a')

        # Create multiple log entries and add them to the grid
        logs = [self.tab_1_logs() for i in range(8)]
        for i, log in enumerate(logs):
            # Use grid to place each log entry in a row and column
            log.grid(row=i, column=0, sticky='nsew',pady= 3)

    def tab_1_logs(self):
        self.frame_log= ttk.Frame(self.frame_tab_1)
        self.frame_log.columnconfigure((0,4), weight= 1, uniform= 'a')
        self.frame_log.columnconfigure((1,2,3), weight= 2, uniform= 'a')
        self.frame_log.rowconfigure((0,1), weight= 1, uniform= 'a')

        # Create separate image and resized_image variables for each log entry
        image_path = r"C:\Users\hamed\Python\GUI_Tutorial\icons\contact_icon.png"
        image_path2 = r"C:\Users\hamed\Python\GUI_Tutorial\icons\call_icon2.png"
        image = Image.open(image_path)
        image2 = Image.open(image_path2)

        self.sub_frame1(image).grid(row=0, column=0, rowspan= 2, sticky= 'nsew')
        self.sub_frame2().grid(row=0, column=1, columnspan= 3, sticky= 'nsew', padx= (5,0))
        self.sub_frame3().grid(row=1, column=1, sticky= 'nsew', padx= (5,0))
        self.sub_frame4().grid(row=1, column=2, sticky= 'nsew')
        self.sub_frame5().grid(row=1, column=3, sticky= 'nsew')
        self.sub_frame6(image2).grid(row=0, column=4, rowspan= 2, sticky= 'nsew')
        return self.frame_log
    
    def sub_frame1(self,image):  # Create a subframe with a canvas and display an image
        subframe_1 = ttk.Frame(self.frame_log)
        subframe_1.bind("<Configure>", lambda event, i=image: self.on_window_resize(subframe_1, event, i, 1))

        return subframe_1
    
    def sub_frame2(self):       #name\number
        self.subframe_2= ttk.Frame(self.frame_log)      
        ttk.Label(self.subframe_2, text= self.fake_name()).place(relx=0, rely=0,relheight=1,relwidth=1)
        return self.subframe_2
    
    def sub_frame3(self):       #incoming\outgoing
        self.subframe_3= ttk.Frame(self.frame_log)      
        ttk.Label(self.subframe_3, text= self.in_out()).place(relx=0, rely=0,relheight=1,relwidth=1)
        return self.subframe_3
    
    def sub_frame4(self):       #country
        self.subframe_4= ttk.Frame(self.frame_log)      
        ttk.Label(self.subframe_4, text= self.country()).place(relx=0, rely=0,relheight=1,relwidth=1)
        return self.subframe_4
        
    def sub_frame5(self):       #date
        self.subframe_5= ttk.Frame(self.frame_log)      
        ttk.Label(self.subframe_5, text= self.date()).place(relx=0, rely=0,relheight=1,relwidth=1)
        return self.subframe_5
    
    def sub_frame6(self, image):       #call icon
        subframe_6= ttk.Frame(self.frame_log)      
        subframe_6.bind("<Configure>", lambda event, i=image: self.on_window_resize(subframe_6, event, i, 6))

        return subframe_6
    
    def on_window_resize(self, parent, event, image, frame):
        # This method will be called after the window has been rendered
        if frame == 1:
            # Get the actual width and height of the widget
            width = event.width 
            height = event.height 

            # Resize the image to fit the widget
            image = image.resize((width, height), resample=Image.LANCZOS)
            tk_image = ImageTk.PhotoImage(image)
            label = ttk.Label(parent, image=tk_image)
            label.image = tk_image  # To prevent garbage collection
            label.place(relx=0, rely=0, relheight=1, relwidth=1)

        elif frame == 6:
            # Get the actual width and height of the widget
            width = event.width - 20
            height = event.height - 25

            # Resize the image to fit the widget
            image = image.resize((width, height), resample=Image.LANCZOS)
            tk_image = ImageTk.PhotoImage(image)
            label = ttk.Label(parent, image=tk_image)
            label.image = tk_image  # To prevent garbage collection
            label.place(relx=0.15, rely=0.05, relheight=1, relwidth=1)
        else:
            print("frame was not specified")

    @staticmethod
    def fake_name():
        fake= Faker()
        name = fake.name()
        return name
    @staticmethod
    def in_out():
        x= ['incoming','outgoing']
        y= random.choice(x)
        return y
    @staticmethod
    def country():
        fake= Faker()
        country= fake.country()
        return country
    def date(self):
        if self.day>1:
            print(self.day)
            self.day-=1
            print(self.day)
            today = datetime.now().strftime(f"{self.day}/%m/%Y")
            return today
        else:
            if self.day == 1:
                day= '30'
                month= int(datetime.now().strftime("%m")) -1
                today = datetime.now().strftime(f"{day}/{month}/%Y")
                self.day-=1
                print('0')
                return today
            elif self.day == 0:
                day= '29'
                month= int(datetime.now().strftime("%m")) -1
                today = datetime.now().strftime(f"{day}/{month}/%Y")
                self.day-=1
                print('0')
                return today
            else:
                day= 29+ self.day
                month= int(datetime.now().strftime("%m")) -1
                today = datetime.now().strftime(f"{day}/{month}/%Y")
                self.day-=1
                print('else')
                return today

App()