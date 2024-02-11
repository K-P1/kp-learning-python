#failed... part 28 works this is kept for future refrence
#note to self change your whole approach probably try using a class or something else just chage it up what you have now is not working unless you find a way to update the live width outside the function### Check how you did live update before maybe try somthing with a timer that refresh every second ### maybe the layout should be called inside the event function
#responsive layout
import tkinter as tk
from tkinter import ttk
live_width = w
def on_resize(event):
    global live_width
    width_list= []
    live_width= event.width
    if live_width >= w:
        width_list.append(f"{live_width}")
        print(width_list)


def app(width,height):
    global w
    w=width
    h=height
    window= tk.Tk()
    window.title("Responsive Layout")
    window.geometry(f"{w}x{h}")
    window.minsize(w,h)
    window.resizable(True,False)
    #control event
    window.bind("<Configure>", on_resize)
    #widgets
    red= ttk.Label(window, text='red', background= 'red')
    green= ttk.Label(window, text='green', background= 'green')
    blue= ttk.Label(window, text='blue', background= 'blue')
    yellow= ttk.Label(window, text='yellow', background= 'yellow')
    
    #call the custom layout function
    layout(window,live_width,red,green,blue,yellow)
    
    #run
    window.mainloop()

def layout(parent,width,w1,w2,w3,w4):
    #layout
    parent.grid_columnconfigure((0, 1,2,3), weight=1)
    parent.grid_rowconfigure((0, 1,2,3), weight=1)
    if width <600:
        w1.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(5))
        w2.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=(5))
        w3.grid(row=2, column=0, columnspan=4, sticky="nsew", pady=(5))
        w4.grid(row=3, column=0, columnspan=4, sticky="nsew", pady=(5))
    if width >=600 and width<800:
        w1.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew", pady=(5),padx=(5))
        w2.grid(row=0, column=2, columnspan=2, rowspan=2, sticky="nsew", pady=(5),padx=(5))
        w3.grid(row=2, column=0, columnspan=2, rowspan=2, sticky="nsew", pady=(5),padx=(5))
        w4.grid(row=2, column=2, columnspan=2, rowspan=2, sticky="nsew", pady=(5),padx=(5))
    if width >=800:
        w1.grid(row=0, column=0, rowspan=4, sticky="nsew", padx=(5))
        w2.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=(5))
        w3.grid(row=0, column=2, rowspan=4, sticky="nsew", padx=(5))
        w4.grid(row=0, column=3, rowspan=4, sticky="nsew", padx=(5))
    


#app(width,height)
app(300,400)