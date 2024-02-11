#Pack layout
import tkinter as tk
from tkinter import ttk
from tkinter import *

# window
window= tk.Tk()
window.title("Pack parenting")
window.geometry('800x500')

#widgets
label1= ttk.Label(window, text= 'red', background= 'red')
label2= ttk.Label(window, text= 'blue', background= 'blue')
label3= ttk.Label(window, text= 'green', background= 'green')
label4= ttk.Label(window, text= 'black', background= 'black')
label5= ttk.Label(window, text= 'white')
label6= ttk.Label(window, text= 'yellow', background= 'yellow')
button= Button(window, text= 'button',bg= 'red')

#layout
label1.pack(side= 'top', expand= True, fill= 'both', pady= 10, padx=10)
#label2.pack(side= 'top', expand= True)
#label3.pack(side= 'top', expand= True, fill= 'both')
label4.pack(side= 'left', expand= True, fill= 'both')
label5.pack(side= 'top', expand= True, fill= 'both')
label6.pack(side= 'top', expand= True, fill= 'both')
#button.pack(side= 'top', fill= 'both', padx= 200,pady= 20)

#run
window.mainloop()