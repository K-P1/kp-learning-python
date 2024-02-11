#Toggling widgets
#widget.pack_forget() or place_forget() or grid_forget() does the same thing they all hide the widget
#in case of pack forget you will run into the problem of disarranged layout because pack stacks widgets
#this can be fixed by replaceing the widget you want to hide with a blank widget like a frame or an empty label
#then using the 'before' aregument you can properly pack the empty widget to replace the one you wanna  hide.
import tkinter as tk
from tkinter import ttk

# window
window= tk.Tk()
window.title("hide widget")
window.geometry('800x500')

#function
state1= True
state2= True
state3= True
def toggle1():
    global state1
    if state1:
        label1.place_forget()
        state1= False
    else:
        label1.place(relx= 0.1, rely= 0.3, relheight= 0.2, relwidth=0.2)
        state1= True
def toggle2():
    global state2
    if state2:
        label2.place_forget()
        state2= False
    else:
        label2.place(relx= 0.4, rely= 0.3, relheight= 0.2, relwidth=0.2)
        state2= True
def toggle3():
    global state3
    if state3:
        label3.place_forget()
        state3= False
    else:
        label3.place(relx= 0.7, rely= 0.3, relheight= 0.2, relwidth=0.2)
        state3= True

    

#widgets
label1= ttk.Label(window, text= 'red', background= 'red')
label2= ttk.Label(window, text= 'blue', background= 'blue')
label3= ttk.Label(window, text= 'green', background= 'green')
button1= ttk.Button(window, text= 'toggle red', command = toggle1)
button2= ttk.Button(window, text= 'toggle blue', command = toggle2)
button3= ttk.Button(window, text= 'toggle green', command = toggle3)

#layout
label1.place(relx= 0.1, rely= 0.3, relheight= 0.2, relwidth=0.2)
label2.place(relx= 0.4, rely= 0.3, relheight= 0.2, relwidth=0.2)
label3.place(relx= 0.7, rely= 0.3, relheight= 0.2, relwidth=0.2)
button1.place(relx= 0.15, rely= 0.55, relheight= 0.05)
button2.place(relx= 0.45, rely= 0.55, relheight= 0.05)
button3.place(relx= 0.75, rely= 0.55, relheight= 0.05)

#run
window.mainloop()