import tkinter as tk
from tkinter import ttk
#getting and setting widgets data
#functions
def button_func():
    # get the content of the entry
    Entry_text= Entry.get()
    
    # update the label
    #Label.configure(text= "new next")
    Label['text']= Entry_text
    Entry['state']= 'disabled'
    #print(Entry.configure())
    
def reset():
    Label['text']= "some text"
    Entry['state']= 'normal'

# window
window= tk.Tk()
window.title("")

#widgets
Label= ttk.Label(master= window, text= "sometext")
Entry= ttk.Entry(master= window)
Button= ttk.Button(master= window, text= "button", command= button_func)
Button2= ttk.Button(master= window, text= "reset", command= reset)

#pack
Label.pack()
Entry.pack()
Button.pack()
Button2.pack()

#run
window.mainloop()