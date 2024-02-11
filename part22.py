#stacking order
#th1s determines which widget will be untop of the other, widget stack untop of eeach other when they are created not when they are placed
#widget.lift()
#widget.lower()
#widget.tkraise(aboveThis = widget)
import tkinter as tk
from tkinter import ttk

# window
window= tk.Tk()
window.title("widget sizes")
window.geometry('400x400')



#functions
def green():
    label1= ttk.Label(window, text= 'green', background= 'green')
    label1.place(relx=0.1,rely=0.2, relheight= 0.4, relwidth=0.55)
def red():
    label2= ttk.Label(window, text= 'red', background= 'red')
    label2.place(relx=0.4,rely=0.1, relheight= 0.25, relwidth=0.4)
def raise_green():
    red()
    green()
def raise_red():
    green()
    red()

#widgets
#green()
label1= ttk.Label(window, text= 'green', background= 'green')
#red()
label2= ttk.Label(window, text= 'red', background= 'red')
label3= ttk.Label(window, text= 'blue', background= 'blue')
#button1= ttk.Button(window, text= 'raise green', command= raise_green)
button1= ttk.Button(window, text= 'raise green', command= lambda: label1.lift())
#button2= ttk.Button(window, text= 'raise red', command= raise_red)
button2= ttk.Button(window, text= 'raise red', command=  lambda: label2.tkraise())
button3= ttk.Button(window, text= 'raise blue', command=  lambda: label3.tkraise(aboveThis= label1))

#layout
label1.place(relx=0.1,rely=0.2, relheight= 0.4, relwidth=0.55)
label2.place(relx=0.4,rely=0.1, relheight= 0.25, relwidth=0.4)
label3.place(relx=0.2,rely=0.3, relheight= 0.3, relwidth=0.45)

button1.place(relx=0.8, rely=1, height= 30, relwidth=0.2, anchor= 'se')
button2.place(relx=1, rely=1, height= 30, relwidth=0.2, anchor= 'se')
button3.place(relx=0.6, rely=1, height= 30, relwidth=0.2, anchor= 'se')

#run
window.mainloop()