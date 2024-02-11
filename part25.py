#combining different layouts using class
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class app(ttk.Window):
    def __init__(self, title, geometry):
        global state2
        global state1
        global themes
        global style
        super().__init__(self)
        self.title(title)
        self.geometry(f'{geometry[0]}x{geometry[1]}')
        style= ttk.Style('darkly')
        #important vars
        state1= True
        state2= True
        themes = ['cosmo','flatly','litera','minty','lumen','sandstone','yeti','pulse','united','morph','journal','superhero','solar','cyborg','vapor','simplex','cerculean']

        self.widget_set2 = widget_set2(self)
        widget_set1(self, self.widget_set2)
        self.widget_set2.place(relx=1, rely=0, relheight=1, relwidth=0.65, anchor= 'ne')

        #run
        self.mainloop()

class commands():
    def __init__(self):
        pass
        
    def B1(widget_set1):
        #label 1 vanish and reappear
        global state1
        if state1:
            widget_set1.label1.grid_forget()
            state1= False
        else:
            widget_set1.label1= ttk.Label(widget_set1, text= 'red', background= 'red')
            widget_set1.label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
            state1= True
    
    def B2(widget_set2):
        #label 2 vanish and reappear
        global state2
        if state2:
            widget_set2.label2.grid_forget()
            state2= False
        else:
            widget_set2.label2= ttk.Label(widget_set2, text= 'blue', background= 'blue')
            widget_set2.label2.grid(row= 0, column= 1, sticky= 'nwse', padx= 15, pady= 5)
            state2= True

    def B3(widget_set2):
        #red>brown  blue>purple
        label1= widget_set2.get_label1()
        label2= widget_set2.get_label2()
        label1.grid_forget()
        label1= ttk.Label(widget_set2, text= 'brown', background= 'brown')
        label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
        label2.grid_forget()
        label2= ttk.Label(widget_set2, text= 'purple', background= 'purple')
        label2.grid(row= 0, column= 1, sticky= 'nwse', padx= 15, pady= 5)
        
    def B4(widget_set2):
        #red>pink  blue>green
        label1= widget_set2.get_label1()
        label2= widget_set2.get_label2()        
        label1.grid_forget()
        label1= ttk.Label(widget_set2, text= 'pink', background= 'pink')
        label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
        label2.grid_forget()
        label2= ttk.Label(widget_set2, text= 'green', background= 'green')
        label2.grid(row= 0, column= 1, sticky= 'nwse', padx= 15, pady= 5)

    def B5(widget_set2):
        #red>orange  blue>yellow
        label1= widget_set2.get_label1()
        label2= widget_set2.get_label2()        
        label1.grid_forget()
        label1= ttk.Label(widget_set2, text= 'orange', background= 'orange')
        label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
        label2.grid_forget()
        label2= ttk.Label(widget_set2, text= 'yellow', background= 'yellow')
        label2.grid(row= 0, column= 1, sticky= 'nwse', padx= 15, pady= 5)

    def Dark():
        global style
        style.theme_use('darkly')

    def Random():
        global style
        global themes
        theme = themes[2]
        style.theme_use(theme)
        themes.append(themes.pop(0))

class widget_set1(ttk.Frame):
    def __init__(self, parent, widget_set2):
        super().__init__(parent)
        self.place(relx= 0, rely= 0, relheight=1, relwidth=0.35)
        #creating widgets
        button3= ttk.Button(self, text= 'Brown/Purple', command= lambda: commands.B3(widget_set2))
        button4= ttk.Button(self, text= 'Pink/Green', command= lambda: commands.B4(widget_set2))
        button5= ttk.Button(self, text= 'Orange/Yellow', command= lambda: commands.B5(widget_set2))
        entry1= ttk.Entry(self, text= 'entry1')
        slider1= ttk.Scale(self,orient='vertical')
        slider2= ttk.Scale(self,orient='vertical')
        button6= ttk.Button(self, text= 'default', command= commands.Dark)
        button7= ttk.Button(self, text = 'random', command= commands.Random)
        #placing widgets
        button3.place(relx= 0, rely= 0.01, relheight=0.16, relwidth=0.58)
        button4.place(relx= 0.6, rely= 0.01, relheight=0.16, relwidth=0.4)
        button5.place(relx= 0, rely= 0.18, relheight=0.16, relwidth=1)
        slider1.place(relx= 0.15, rely= 0.355, relheight=0.5)
        slider2.place(relx= 0.8, rely= 0.355, relheight=0.5)
        button6.place(relx= 0.51, rely= 0.93, anchor= 'sw')
        button7.place(relx= 0.49, rely= 0.93, anchor= 'se')
        entry1.place(relx= 0.1, rely=0.999, relwidth= 0.8, height= 30, anchor= 'sw')

class widget_set2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=1, rely=0, relheight=1, relwidth=0.65, anchor= 'ne')
        #create widgets
        self.label1= ttk.Label(self, text= 'red', background= 'red')
        self.label2= ttk.Label(self, text= 'blue', background= 'blue')
        self.button1= ttk.Button(self, text= 'Hide/Show Red Button 1', command= lambda: commands.B1(self))
        self.button2= ttk.Button(self, text= 'Hide/Show Blue Button 2', command= lambda: commands.B2(self))
        #placing widgets
        self.rowconfigure([0,1], weight= 2)
        self.columnconfigure([0,1], weight= 2)
        self.label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
        self.label2.grid(row= 0, column= 1, sticky= 'nwse', padx= 15, pady= 5)
        self.button1.grid(row= 1, column= 0, sticky= 'nwse', padx= 15, pady= 5)
        self.button2.grid(row= 1, column= 1, sticky= 'nwse', padx= 15, pady= 5)

    def get_label1(self):
        return self.label1
    
    def get_label2(self):
        return self.label2

app('working with classes', (1000,600))