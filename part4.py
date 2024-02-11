import tkinter as tk
from tkinter import ttk
#linking widgets and tkinter variables
#functions
def button_func():
    print(string_var.get())
    string_var.set("")


# window
window= tk.Tk()
window.title("Tkinter variables")
window.geometry('800x500')

#tkinter variables
string_var= tk.StringVar()

#widgets
label= ttk.Label(master = window, text= 'label', textvariable= string_var, background= 'black',foreground= 'red', width= 100).pack(pady=15,padx=20)
entry= ttk.Entry(master = window, textvariable= string_var, width= 70).pack()
button= ttk.Button(master= window, text= 'button', command= button_func).pack(pady= 20)
#pack

#run
window.mainloop()