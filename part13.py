#TABS
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

#functions

# window
window= tk.Tk()
window.title("notebook")
window.geometry('800x500')


#widgets
Style().configure('TNotebook', tabposition='s')
notebook= ttk.Notebook(window)
#tab 1
tab1=ttk.Frame(notebook)
label1= ttk.Label(tab1, text= "Text in tab 1").pack()
entry1= ttk.Entry(tab1).pack()
buttton1= ttk.Button(tab1,text= 'Button').pack()
#tab2
tab2=ttk.Frame(notebook)
label2= ttk.Label(tab2, text= "Text in tab 2").pack()
entry2= ttk.Entry(tab2).pack()
buttton2= ttk.Button(tab2,text= 'Button').pack()

notebook.add(tab1, text= 'Tab 1')
notebook.add(tab2, text= 'Tab 2')
notebook.pack(fill='both', expand='True')





#run
window.mainloop()