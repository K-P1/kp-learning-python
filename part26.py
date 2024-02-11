#custom frame in tkinter class and function based approach
import tkinter as tk
from tkinter import ttk

class CustomFrame(ttk.Frame):
    def __init__(self, parent, text_1, text_2, text_3):
        super().__init__(parent)
        #define grid
        self.rowconfigure([0,1], weight= 1)
        self.columnconfigure([0, 1, 2], weight = 1,uniform='a')

        # create widgets
        self.label = ttk.Label(self, text=text_1)
        self.button = ttk.Button(self, text=text_2)
        self.button2 = ttk.Button(self, text=text_3)
        self.entry = ttk.Entry(self)

        # place widgets using grid
        self.label.grid(row=0,column=0,rowspan=2,sticky='nsew')
        self.button.grid(row=0, column= 1, rowspan=2, sticky= 'nsew')
        self.button2.grid(row=1,column=2,sticky='nsew')
        self.entry.grid(row=0, column=2,sticky='nsew')
        
        self.pack(side= 'top', expand= 'True', fill= 'both',padx= 10,pady= 10)

def Custom_frame(parent,text_1,text_2,text_3):
    #define grid
    frame= ttk.Frame(parent)
    frame.rowconfigure([0,1], weight= 1)
    frame.columnconfigure([0, 1, 2], weight = 1,uniform='a')

    # create widgets
    label = ttk.Label(frame, text=text_1)
    button = ttk.Button(frame, text=text_2)
    button2 = ttk.Button(frame, text=text_3)
    entry = ttk.Entry(frame)
    
    # place widgets using grid
    label.grid(row=0,column=0,rowspan=2,sticky='nsew')
    button.grid(row=0, column= 1, rowspan=2, sticky= 'nsew')
    button2.grid(row=1,column=2,sticky='nsew')
    entry.grid(row=0, column=2,sticky='nsew')
    return frame

window= tk.Tk()
window.geometry('600x800')
window.title('widgets and return')
Custom_frame(window,'button','click','test').pack(side= 'top', expand= 'True', fill= 'both',padx= 10,pady= 10)
Custom_frame(window,'button','click','test').pack(side= 'top', expand= 'True', fill= 'both',padx= 10,pady= 10)
Custom_frame(window,'button','click','test').pack(side= 'top', expand= 'True', fill= 'both',padx= 10,pady= 10)
Custom_frame(window,'button','click','test').pack(side= 'top', expand= 'True', fill= 'both',padx= 10,pady= 10)


#run
window.mainloop()

"""class App(tk.Tk):
    def __init__(self, text_1, text_2, text_3, frame):
        super().__init__()
        self.title('Custom widgets with class')
        self.geometry('800x600')
        
        # Create and pack the first instance of CustomFrame
        if frame == int(frame):
            if frame >10:
                print("number of frames are too much")
                return
            else:
                for x in range(frame):
                    frame = CustomFrame(self,text_1+str(x+1),text_2+str(x+1),text_3+str(x+1))
                    frame.pack(fill='both', expand=True, side='top')
        else:
            frame = 1
            print("frame was changed to 1")

        # run
        self.mainloop()

class CustomFrame(ttk.Frame):
    def __init__(self, parent, text_1, text_2, text_3):
        super().__init__(parent)

        # create widgets
        self.label = ttk.Label(self, text=text_1)
        self.button = ttk.Button(self, text=text_2)
        self.button2 = ttk.Button(self, text=text_3)
        self.entry = ttk.Entry(self)

        # place widgets using place
        self.label.place(relx=0, rely=0, relheight=1, relwidth=0.29)
        self.button.place(relx=0.3, rely=0, relheight=1, relwidth=0.34)
        self.button2.place(relx=0.65, rely=0.5, relheight=0.5, relwidth=0.35)
        self.entry.place(relx=0.65, rely=0, relheight=0.5, relwidth=0.35)

App('label', 'button', 'exercise',3)"""
