#Frames and parenting
import tkinter as tk
from tkinter import ttk

# window
window= tk.Tk()
window.title("")
window.geometry('600x400')

TEXT= tk.Label(window, text= 'FRAMES AND PARENTING',font = "calibri 34 bold").pack()

frame1= ttk.Frame(window, width= 200, height= 250, borderwidth=10, relief= tk.GROOVE)#RIDGE,SUNKEN,FLAT,RAISED,GROOVE
frame1.pack_propagate(False)
frame1.pack(side= 'left',padx=10)

text= tk.Label(frame1, text= "testing").pack()
entry= ttk.Entry(frame1).pack()
button= ttk.Button(frame1, text='a button').pack()
text= tk.Label(window, text= "TESTING").pack(side= 'left', padx= (55,0))

frame2= ttk.Frame(window, width= 200, height= 250, borderwidth=10, relief= tk.GROOVE)#RIDGE,SUNKEN,FLAT,RAISED,GROOVE
frame2.pack_propagate(False)
frame2.pack(side= 'right', padx= 10)

text= tk.Label(frame2, text= "testing").pack()
entry= ttk.Entry(frame2).pack()
button= ttk.Button(frame2, text='a button').pack()


#run
window.mainloop()