#combining different layouts
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tttk

# window
window= tttk.Window(themename= 'darkly')
window.title("")
window.geometry('1000x600')
style= tttk.Style()

#functions
state1= True
state2= True
themes = ['cosmo','flatly','litera','minty','lumen','sandstone','yeti','pulse','united','morph','journal','superhero','solar','cyborg','vapor','simplex','cerculean']

def B1():
    #label 1 vanish and reappear
    global state1
    global label1
    if state1:
        label1.grid_forget()
        state1= False
    else:
        label1= ttk.Label(frame2, text= 'red', background= 'red')
        label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
        state1= True
def B2():
    #label 2 vanish and reappear
    global state2
    global label2
    if state2:
        label2.grid_forget()
        state2= False
    else:
        label2= ttk.Label(frame2, text= 'blue', background= 'blue')
        label2.grid(row= 0, column= 1, sticky= 'nwse', padx= 15, pady= 5)
        state2= True
def B3():
    #red>brown  blue>purple
    global label1
    global label2
    
    label1.grid_forget()
    label1= ttk.Label(frame2, text= 'brown', background= 'brown')
    label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
    label2.grid_forget()
    label2= ttk.Label(frame2, text= 'purple', background= 'purple')
    label2.grid(row= 0, column= 1, sticky= 'nwse', padx= 15, pady= 5)
def B4():
    #red>pink  blue>green
    global label1
    global label2
    
    label1.grid_forget()
    label1= ttk.Label(frame2, text= 'pink', background= 'pink')
    label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
    label2.grid_forget()
    label2= ttk.Label(frame2, text= 'green', background= 'green')
    label2.grid(row= 0, column= 1, sticky= 'nwse', padx= 15, pady= 5)
def B5():
    #red>orange  blue>yellow
    global label1
    global label2
    
    label1.grid_forget()
    label1= ttk.Label(frame2, text= 'orange', background= 'orange')
    label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
    label2.grid_forget()
    label2= ttk.Label(frame2, text= 'yellow', background= 'yellow')
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

#tkinter variables
theme= tk.BooleanVar()

#widgets
frame1= ttk.Frame(window)
frame2= ttk.Frame(window)
label1= ttk.Label(frame2, text= 'red', background= 'red')
label2= ttk.Label(frame2, text= 'blue', background= 'blue')
button1= ttk.Button(frame2, text= 'Hide/Show Red Button 1', command= B1)
button2= ttk.Button(frame2, text= 'Hide/Show Blue Button 2', command= B2)
button3= ttk.Button(frame1, text= 'Brown/Purple', command= B3)
button4= ttk.Button(frame1, text= 'Pink/Green', command= B4)
button5= ttk.Button(frame1, text= 'Orange/Yellow', command= B5)
entry1= ttk.Entry(frame1, text= 'entry1')
slider1= ttk.Scale(frame1,orient='vertical')
slider2= ttk.Scale(frame1,orient='vertical')
button6= ttk.Button(frame1, text= 'default', command= Dark)
button7= ttk.Button(frame1, text = 'random', command= Random)

#layout
frame1.place(relx= 0, rely= 0, relheight=1, relwidth=0.35)

button3.place(relx= 0, rely= 0.01, relheight=0.16, relwidth=0.58)
button4.place(relx= 0.6, rely= 0.01, relheight=0.16, relwidth=0.4)
button5.place(relx= 0, rely= 0.18, relheight=0.16, relwidth=1)
slider1.place(relx= 0.15, rely= 0.355, relheight=0.5)
slider2.place(relx= 0.8, rely= 0.355, relheight=0.5)
button6.place(relx= 0.51, rely= 0.93, anchor= 'sw')
button7.place(relx= 0.49, rely= 0.93, anchor= 'se')
entry1.place(relx= 0.1, rely=0.999, relwidth= 0.8, height= 30, anchor= 'sw')

frame2.place(relx=1, rely=0, relheight=1, relwidth=0.65, anchor= 'ne')
frame2.rowconfigure([0,1], weight= 2)
frame2.columnconfigure([0,1], weight= 2)
label1.grid(row= 0, column= 0, sticky= 'nwse', padx= 15, pady= 5)
label2.grid(row= 0, column= 1, sticky= 'nwse', padx= 15, pady= 5)
button1.grid(row= 1, column= 0, sticky= 'nwse', padx= 15, pady= 5)
button2.grid(row= 1, column= 1, sticky= 'nwse', padx= 15, pady= 5)


#run
window.mainloop()