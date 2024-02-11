#new widgets combobox and spinbox
import tkinter as tk
from tkinter import ttk

#list
items=['banana','bread','peanut','butter']
# window
window= tk.Tk()
window.title("Combo and spin")
window.geometry('800x500')

#tkinter variables
foods= tk.StringVar(value=items[0])
#food= tk.StringVar(value= f"selected food = {foods.get()}")

#Combobox
combo= ttk.Combobox(window, textvariable= foods)
combo['values']=items
#combo.configure(values=items)
combo.pack()
combo_label= ttk.Label(window,text='NO food selsected')
#combo_label= ttk.Label(window,textvariable=food)
combo_label.pack()
#events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config (text=f"selected food = {foods.get()}"))
#combo.bind('<<ComboboxSelected>>', lambda event: food.set(f"selected food = {foods.get()}"))

#Spinbox
spin_int= tk.IntVar(value=12)
spin=ttk.Spinbox(window, from_ = 3, to= 20, increment= 3, textvariable= spin_int, command= lambda: print(spin_int.get()))
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()

spin_list=['a','b','c','d','e','f']
spin_var= tk.StringVar(value= spin_list[0])
spin2= ttk.Spinbox(window, values= spin_list, textvariable= spin_var)
spin2.bind('<<Decrement>>', lambda event: print(spin_var.get()))
spin2.pack()

#run
window.mainloop()