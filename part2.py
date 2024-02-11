import tkinter as tk
from tkinter import ttk
#more on widgets
#functions
def button_func():
    print("a button was pressed")
def button_func2():
    print("hello")

# creat a window
window= tk.Tk()
window.title("wondow and wigets")
window.geometry('800x500')

# widgets
# tk text
text= tk.Text(master = window)

# ttk label
label= ttk.Label(master= window, text= "This is a test")
label2= ttk.Label(master= window, text= "my label")

# ttk entry
entry= ttk.Entry(master= window)

# ttk button
button= ttk.Button(master= window, text= "A button", command= button_func)
button2= ttk.Button(master= window, text= "hello", command= lambda: print("hello"))
#button2= ttk.Button(master= window, text= "hello", command= button_func2)

#pack
label.pack()
text.pack()
entry.pack()
label2.pack()
button.pack()
button2.pack()

# run
window.mainloop()