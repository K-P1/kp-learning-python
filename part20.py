#Place layout
import tkinter as tk
from tkinter import ttk

# window
window= tk.Tk()
window.title("place")
window.geometry('800x400')

#widgets
label1= ttk.Label(window, text= 'red', background= 'red')
label2= ttk.Label(window, text= 'blue', background= 'blue')
label3= ttk.Label(window, text= 'green', background= 'green')
label4= ttk.Label(window, text= 'brown', background= 'brown')
button= ttk.Button(window, text= 'green')
frame= ttk.Frame(window)
frame_label= ttk.Label(frame, text= 'just a label', background= 'yellow')
frame_button= ttk.Button(frame, text= 'A button')


#layout
label1.place(x=600,y=350, width= 200, height=50)
label2.place(relx=0,rely=0.5, relwidth= 0.2, relheight=0.1)
label3.place(x=0,y=240, width= 160, height= 40)
button.place(relx=1, rely=1, anchor='se')
frame.place(relx=1,rely=0,relwidth=0.2,relheight=0.5,anchor='ne')
frame_label.place(relx=0,rely=0,relwidth=1,relheight=0.2)
frame_button.place(relx=0,rely=0.22,relwidth=0.5,relheight=0.12)

label4.place(relx=0.5,rely=0.5,height=200 ,relwidth=0.5, anchor= 'center')


#run
window.mainloop()