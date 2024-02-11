# canvas widget basically paint on tkinter
import tkinter as tk
from tkinter import ttk

#functions

# window
window= tk.Tk()
window.title("Canvas")
window.geometry('800x500')
#window.configure(bg= 'white')

#tkinter variables

#widgets
canvas= tk.Canvas(window, bg= 'blue')
canvas.pack()

#canvas.create_rectangle((20,20,100,200), fill= 'black', width= 2, dash= (1,2,3,255), outline= 'green')
canvas.create_oval((30,30,200,220), fill= 'gold')
#canvas.create_arc((30,30,200,220), fill= 'green', start= 185, extent= 180, style= tk.ARC, outline= 'red', width= 10)
#canvas.create_polygon((40,40,120,150, 200,200), fill= 'red')
#canvas.create_line((0,0,225,225), fill= 'white')
#canvas.create_text((100,200), text= 'this is a text stuff on canva', fill= 'white', width= 220)
#canvas.create_window((150,100), window= ttk.Label(window, text= "this is some long ass text"))
"""
#Exersise making a paint app
def get_pos(event):
    print(f"x: {event.x} y:{event.y}")
    
def paint(event):
    x= event.x
    y= event.y
    size=4
    canvas.create_oval((x- size/2, y- size/2, x+ size/2, y+ size/2), fill= 'black')
#    canvas.create_line((x,y,x+1,y), fill= 'black')
    
def erase(event):
    x= event.x
    y= event.y
    size=16
    canvas.create_oval((x- size/2, y- size/2, x+ size/2, y+ size/2), fill= 'white', outline= 'white')
#    canvas.create_line((x,y,x+1,y), fill= 'white')
canvas= tk.Canvas(window, bg= 'white',width= 800, height= 500)
canvas.pack()
#canvas.create_line(10,20,300,400, fill= 'black')
#canvas.bind('<Motion>', get_pos)
canvas.bind('<Button1-Motion>',paint)
canvas.bind('<Button3-Motion>',erase)
"""
#run
window.mainloop()