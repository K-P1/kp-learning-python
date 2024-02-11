#Responsive layouts with tkinter
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, width):
        super().__init__()
        self.title("App")
        self.geometry(f'{width}x400')
        self.frame= ttk.Frame(self)
        self.frame.pack(expand= 'True', fill= 'both')
        resize(self,{300: self.size_1, 600: self.size_2, 900: self.size_3})

        #run
        self.mainloop()

    def size_1(self):
        self.frame.pack_forget()
        self.frame= ttk.Frame(self)
        self.frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.red = ttk.Label(self.frame, text='red', background='red')
        self.green = ttk.Label(self.frame, text='green', background='green')
        self.blue = ttk.Label(self.frame, text='blue', background='blue')
        self.yellow = ttk.Label(self.frame, text='yellow', background='yellow')
        self.red.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(5))
        self.green.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=(5))
        self.blue.grid(row=2, column=0, columnspan=4, sticky="nsew", pady=(5))
        self.yellow.grid(row=3, column=0, columnspan=4, sticky="nsew", pady=(5))
        self.frame.pack(expand= 'True', fill= 'both')

    def size_2(self):
        self.frame.pack_forget()
        self.frame= ttk.Frame(self)
        self.frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.red = ttk.Label(self.frame, text='red', background='red')
        self.green = ttk.Label(self.frame, text='green', background='green')
        self.blue = ttk.Label(self.frame, text='blue', background='blue')
        self.yellow = ttk.Label(self.frame, text='yellow', background='yellow')
        self.red.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew", pady=(5), padx=(5))
        self.green.grid(row=0, column=2, columnspan=2, rowspan=2, sticky="nsew", pady=(5), padx=(5))
        self.blue.grid(row=2, column=0, columnspan=2, rowspan=2, sticky="nsew", pady=(5), padx=(5))
        self.yellow.grid(row=2, column=2, columnspan=2, rowspan=2, sticky="nsew", pady=(5), padx=(5))
        self.frame.pack(expand= 'True', fill= 'both')
    
    def size_3(self):
        self.frame.pack_forget()
        self.frame= ttk.Frame(self)
        self.frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.red = ttk.Label(self.frame, text='red', background='red')
        self.green = ttk.Label(self.frame, text='green', background='green')
        self.blue = ttk.Label(self.frame, text='blue', background='blue')
        self.yellow = ttk.Label(self.frame, text='yellow', background='yellow')
        self.red.grid(row=0, column=0, rowspan=4, sticky="nsew", padx=(5))
        self.green.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=(5))
        self.blue.grid(row=0, column=2, rowspan=4, sticky="nsew", padx=(5))
        self.yellow.grid(row=0, column=3, rowspan=4, sticky="nsew", padx=(5))
        self.frame.pack(expand= 'True', fill= 'both')

class resize:
    def __init__(self, parent, size_dict):
        self.window= parent
        self.size_dict= size_dict
        self.min_width= list(self.size_dict)[0]
        self.window.bind("<Configure>", self.check_size)
        self.current_min_size= None

    def check_size(self, event):
        #this if statement stops the event from identifying the grid as a configure event. if you ever want to know the use remove it and run the app you'll see
        if event.widget == self.window:
            checked_width= None
            live_width= event.width
            for min_width in self.size_dict:
                temp_checked_width= live_width - min_width
                if temp_checked_width >= 0:
                    checked_width = min_width
            if checked_width != self.current_min_size:
                self.current_min_size= checked_width
                self.size_dict[self.current_min_size]()

run= App(400)
