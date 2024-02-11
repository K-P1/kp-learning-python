# using a function with an argument with buttons
import tkinter as tk
from tkinter import ttk

#functions
"""
def button_func(based):
    print(based)
        
def button_call():
    button_func('it worked button was pressed')
"""
def button_call(vvv):
    print('a button was pressed')
    print(entry_var.get())   
def outer_func(param):
    def inner_func():
        print(param.get())
        print("pressy press")
    return inner_func
# window
window= tk.Tk()
window.title("button")
window.geometry('800x500')

#tkinter variables
entry_var= tk.StringVar(value='yametekuresai')

#widgets
Entry= ttk.Entry(window, textvariable= entry_var).pack()
button1= ttk.Button(window, text= 'button 1', command= lambda: print(entry_var.get())).pack()
button2= ttk.Button(window, text= 'button 2', command= lambda: button_call('vvvx')).pack()
button3= ttk.Button(window, text= 'button 3', command= outer_func(entry_var)).pack()


#run
window.mainloop()