#understanding widget sizes
#note the layout size always overides the widget size and the specified widget size always overides the default widget size

import tkinter as tk
from tkinter import ttk

# window
window= tk.Tk()
window.title("widget sizes")
window.geometry('800x500')

#widgets
label1= ttk.Label(window, text= 'red', background= 'red')
label2= ttk.Label(window, text= 'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop', background= 'blue')
label3= ttk.Label(window, text= 'green', background= 'green', width= 50)

#layout
#label1.pack()
#label2.pack()
#label3.pack(fill='x')

window.columnconfigure((0,1), weight= 1, uniform='a')
window.rowconfigure((0,1), weight= 1, uniform='a')

label1.grid(row=0, column= 0)
label2.grid(row=1, column= 0, sticky= 'nswe')

#run
window.mainloop()