"""
Some few Tkinter Objects
1. Label
2. Button
3. Entry
4. Frame

How Tkinter Objects are Arranged on a window
1. Grid Manager
2. Pack Manager

"""
from tkinter import *

#=============Window Properties=============
dashboard = Tk()
dashboard.geometry("650x300")
dashboard.title("Halogen")
dashboard.resizable(width = False,height = False)
dashboard["bg"] = "orange"


#===================1. Label===============
label1 = Label(dashboard,text = "Emeka\nis\nTall",\
               font = "Calibri 24 bold italic",\
               fg = "yellow",bg = "black" )
label1.pack(side = LEFT)
"""\Packing Labels Directly
Label(dashboard,text = "Emeka\nis\nTall",\
        font = "Calibri 24 bold italic").pack()
"""
label1["text"] = "Emeka is Black"

#===================2. Button=================
btnClick = Button(dashboard,text = "Click Me",\
        font = "Times 16", fg = "purple",\
                  bg = "white", width = 17,\
                  height = 3)
btnClick.pack(side = RIGHT)

#===================3. Entry(Textbox)===================
#1. StringVar()
#2. IntVar()
#3. DoubleVar()
word = StringVar()
txtentry = Entry(dashboard, textvariable = word\
        ,font = "Arial 16", width = 10)
txtentry.pack()

#===========The grid Manager===================



#=================End of Window================
dashboard.mainloop()

"""
The Grid Manager
==========================================
       |       |       |       |       |
==========================================
       |       |       |       |       |
==========================================
       |       |       |       |       |
==========================================
"""










