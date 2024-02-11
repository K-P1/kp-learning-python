#grid layout
import tkinter as tk
from tkinter import ttk

# window
window= tk.Tk()
window.title("grid")
window.geometry('800x500')

#widgets
label1= ttk.Label(window, text= 'red', background= 'red')
label2= ttk.Label(window, text= 'blue', background= 'blue')
label3= ttk.Label(window, text= 'green', background= 'green')
label4= ttk.Label(window, text= 'orange', background= 'orange')
label5= ttk.Label(window, text= 'yellow', background= 'yellow')
label6= ttk.Label(window, text= 'black', background= 'black')
label7= ttk.Label(window, text= 'white')
label8= ttk.Label(window, text= 'brown', background= 'brown')
button1= ttk.Button(window, text= 'button1')
button2= ttk.Button(window, text= 'button2')
button3= ttk.Button(window, text= 'button3')
button4= ttk.Button(window, text= 'button4')
button5= ttk.Button(window, text= 'button5')
button6= ttk.Button(window, text= 'button6')
entry1= ttk.Entry(window, text= 'entry1')
entry2= ttk.Entry(window, text= 'entry2')

#define grid
window.columnconfigure([0,1,2,3,4,5],weight=1, uniform= 'a')
"""window.columnconfigure(1,weight=1, uniform= 'a')
window.columnconfigure(2,weight=1, uniform= 'a')
window.columnconfigure(3,weight=1, uniform= 'a')
window.columnconfigure(4,weight=1, uniform= 'a')
window.columnconfigure(5,weight=1, uniform= 'a')"""
window.rowconfigure([0,1,2,3,4,5],weight=1, uniform= 'a')
"""window.rowconfigure(1,weight=1, uniform= 'a')
window.rowconfigure(2,weight=1, uniform= 'a')
window.rowconfigure(3,weight=1, uniform= 'a')
window.rowconfigure(4,weight=1, uniform= 'a')
window.rowconfigure(5,weight=1, uniform= 'a')"""

#placing a widget
label1.grid(row=0,column=0, sticky= 'nsew')
label2.grid(row=1,column=1, sticky= 'nsew')
label3.grid(row=2,column=2, sticky= 'nsew')
label4.grid(row=3,column=3, sticky= 'nsew')
label5.grid(row=4,column=4, sticky= 'nsew')
label6.grid(row=5,column=5, sticky= 'nsew')


#run
window.mainloop()