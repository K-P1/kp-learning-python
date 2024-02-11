#pack layout plus frames
import tkinter as tk
from tkinter import ttk
from tkinter import *

# window
window= tk.Tk()
window.title("Pack parenting")
window.geometry('500x700')

#frames
frame1 = Frame(window)
frame2 = Frame(window)
frame2a = Frame(frame2)
frame2b = Frame(frame2)

#widgets
label1= ttk.Label(frame1, text= 'red', background= 'red')
label2= ttk.Label(frame1, text= 'blue', background= 'blue')
label3= ttk.Label(window, text= 'another label', background= 'green')
label4= ttk.Label(frame2a, text= 'list of the labels', background= 'orange')
button1= ttk.Button(frame2a, text= 'A Button')
button2= ttk.Button(frame2a, text= 'Another Button')
button3= ttk.Button(frame2b, text= 'button3')
button4= ttk.Button(frame2b, text= 'button4')
button5= ttk.Button(frame2b, text= 'button5')

#top layout
label1.pack(side='top', expand= True, fill='both')
label2.pack(side='top', expand= True, fill='both')
frame1.pack(side='top', expand= True, fill='both')

#middle layout
label3.pack(side= 'top', expand= True)

#bottom layout
frame2.pack(side= 'top', expand= True, fill='both')
frame2a.pack(side= 'left', expand= True, fill='both')
frame2b.pack(side= 'left', expand= True, fill='both')

button1.pack(side='left', expand= True, fill='both')
label4.pack(side='left', expand= True, fill='both')
button2.pack(side='left', expand= True, fill='both')

button3.pack(side='top', expand= True, fill='both')
button4.pack(side='top', expand= True, fill='both')
button5.pack(side='top', expand= True, fill='both')


#run
window.mainloop()