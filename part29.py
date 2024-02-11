"""
note to self...
this is a personal project to see my currnt skill level, i basically want to make an app that mimics those old dvd player screens, with a shape in the middle that bounces off the walls in a loop. i currently have no idea how this will work but thats the fun of coding we get to figure it out!
Edit
finally completed it, i'm super impressed with myself, actually cant belive i pulled it off, it looks so simple at the end but it definately wasnt easy lol
"""
import tkinter as tk
import random
from tkinter import ttk

class Screen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bouncy widget lol')
        self.geometry('900x600')
        self.attributes('-topmost',True)
        #security event
        self.bind('<Escape>', lambda event: self.quit())#quits the window once esc is pressed
        self.bind('<space>', self.toggle_fullscreen) #Toggle fullscreen on space press
        #x and y position for the oval shape
        self.x = 0
        self.y = 0
        self.multiplier_X= 0.01
        self.multiplier_Y= 0.02
        self.create_widget()
        self.colors= ['white','black','red','green','blue','cyan','yellow','magenta','grey','orange','purple','pink','brown','lightgrey','darkgrey']
        self.color= self.oval_color()

    def toggle_fullscreen(self, event=None):
        # Toggle between fullscreen and normal mode
        self.attributes('-fullscreen', not self.attributes('-fullscreen'))

    def create_widget(self):
        self.frame= ttk.Frame(self)
        self.frame.pack(expand='True', fill= 'both')
        self.canvas= tk.Canvas(self.frame, bg='blue', highlightthickness=0)
        self.canvas.pack(expand='True', fill= 'both')

        self.after(100, self.update_widget)

    def update_widget(self):
        self.canvas.delete("all")   # Delete all items from the canvas
        #x and y positions where the oval will be drawn on the canvas
        xx= self.x * self.canvas.winfo_width()
        yy= self.y * self.canvas.winfo_height()
        oval_width= xx+300
        oval_height= yy+150
        #controlling borders
        if yy < 0:                                                          #oval is at border A
            if self.multiplier_Y < 0:                                       #height multiplier is negative
                self.multiplier_Y = -self.multiplier_Y                      #makes multiplier positive
            else:
                self.multiplier_Y = self.multiplier_Y                       #makes multiplier y positive
            self.multiplier_Y= random.choice([0.01, 0.013, 0.017, 0.02])    #randomize multiplier y
            self.canvas.configure(bg= self.canvas_color())                  #changes the canvas colour
            self.color= self.oval_color()

        elif oval_height >= self.canvas.winfo_height():                     #oval is at border C
            if self.multiplier_Y > 0:                                       #height multiplier is positive
                self.multiplier_Y = -self.multiplier_Y                      #makes multiplier negative
            else:
                self.multiplier_Y = self.multiplier_Y                       #makes multiplier y negative
            self.multiplier_Y= random.choice([-0.01,-0.014, -0.02])         #resets multiplier y
            self.canvas.configure(bg= self.canvas_color())                  #changes the canvas colour
            self.color= self.oval_color()

        elif xx < 0:                                                        #oval is at border D
            if self.multiplier_X < 0:                                       #width multiplier is negative
                self.multiplier_X = -self.multiplier_X                      #makes multiplier positive
            else:
                self.multiplier_X = self.multiplier_X                       #makes multiplier x positive
            self.multiplier_X= random.choice([0.01, 0.013, 0.016, 0.02])    #randomize multiplier x
            self.canvas.configure(bg= self.canvas_color())                  #changes the canvas colour
            self.color= self.oval_color()

        elif oval_width >= self.canvas.winfo_width():                       #oval is at border B
            if self.multiplier_X > 0:                                       #width multiplier is positive
                self.multiplier_X = -self.multiplier_X                      #makes multiplier negative
            else:
                self.multiplier_X = self.multiplier_X                       #makes multiplier x negative
            self.multiplier_X= random.choice([-0.02, -0.016, -0.01])        #resets multiplier x
            self.canvas.configure(bg= self.canvas_color())                  #changes the canvas colour
            self.color= self.oval_color()

        #draw oval
        self.canvas.create_oval(xx, yy, oval_width, oval_height, fill= self.color)
        #increment multiplier
        self.x += self.multiplier_X
        self.y += self.multiplier_Y
        self.after(100, self.update_widget)

    def canvas_color(self):
        self.cc= random.choice(self.colors)
        return self.cc
        
    def oval_color(self):
        self.oc= random.choice(self.colors)
        return self.oc

run= Screen()
run.mainloop()