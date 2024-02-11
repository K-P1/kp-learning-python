import tkinter as tk
from tkinter import ttk
#buttons, checkbox and radio buttons
#functions
def B1():
    print('clicked')

# window
window= tk.Tk()
window.title("buttons")
window.geometry('600x400')

#tkinter variables
string_var= tk.StringVar(value= 'button')
check_value= tk.IntVar()
check_value2= tk.IntVar()

radio_var= tk.StringVar()

#widgets
#normal button
button= ttk.Button(window, command= lambda: (print('clicked\n', radio_var.get()), check_value2.set(5), check_value.set(5), radio_var.set(0)), textvariable= string_var).pack()

#checkbutton
check= ttk.Checkbutton(window, text= 'checkbox1', command= lambda: print(check_value.get()), variable= check_value,onvalue=10,offvalue=5).pack()
check2= ttk.Checkbutton(window, text= 'checkbox2', command= lambda: print(check_value.get()), variable= check_value2,onvalue=10,offvalue=5).pack()

#radiobuttons
radio= ttk.Radiobutton(window,text='radio button1',value=1, variable= radio_var, command= lambda: print(radio_var.get())).pack()
radio2= ttk.Radiobutton(window,text='radio button2',value=2, variable= radio_var, command= lambda: print(radio_var.get())).pack()

#run
window.mainloop()