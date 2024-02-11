#layouts
#gird,place,pack
import tkinter as tk
from tkinter import ttk

# window
window= tk.Tk()
window.title("Layouts")
window.geometry('800x400')

#widgets
label1= ttk.Label(window, text= 'red', background= 'red')
label2= ttk.Label(window, text= 'blue', background= 'blue')
label3= ttk.Label(window, text= 'green', background= 'green')
label4= ttk.Label(window, text= 'black', background= 'black')
label5= ttk.Label(window, text= 'white')

##pack
#label3.pack(side= 'top', expand= True, fill= 'both')
#label2.pack(side= 'top', expand= True, fill= 'both')
#label5.pack(side= 'bottom', expand= True, fill= 'both')
#label1.pack(side= 'right', expand= True, fill= 'both')
#label4.pack(side= 'left',expand= True, fill= 'both')

#grid
#window.columnconfigure(0, weight= 1)
#window.columnconfigure(1, weight= 1)
#window.columnconfigure(2, weight= 2)
#window.rowconfigure(0, weight= 1)
#window.rowconfigure(1, weight= 1)
#label1.grid(row=0, column=2, sticky='nsew')
#label2.grid(row=1, column=1, columnspan=2, sticky='nsew')
#label3.grid(row=0, column=0, columnspan=2, sticky='nsew')

#place
#label1.place(x= 400, y= 0, width= 400, height= 200)
#label2.place(x= 200, y= 200, width= 600, height= 200)
#label3.place(x= 0, y= 0, width= 400, height= 200)
#label5.place(x= 0, y= 200, width= 200, height= 200)

label1.place(relx= 0.5, rely= 0, relwidth= 0.5, relheight=0.5, anchor='nw')
label2.place(relx= 0.25, rely= 0.5, relwidth= 0.75, relheight=0.5, anchor='nw')
label3.place(relx= 0, rely= 0, relwidth= 0.5, relheight=0.5, anchor='nw')
label5.place(relx= 0, rely= 0.5, relwidth= 0.25, relheight=0.5, anchor='nw')



#run
window.mainloop()