#Changing the window
import tkinter as tk
from tkinter import ttk


# window
window= tk.Tk()
window.title("Changing the window")
#window.geometry('1707x960')
#window.geometry('600x400+LEFT+TOP')#left and top can be changed with numbers, they represent the location of the window on the screen with 0+0 putting the window on the top left coner of the screen
#window.iconbitmap('python.ico')

#exercise set the window to the middle of your screen
window_width = 850
window_height = 350
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()
positionTop = int((display_height / 2) - (window_height / 2))
positionLeft = int((display_width / 2) - (window_width / 2))

window.geometry(f'{window_width}x{window_height}+{positionLeft}+{positionTop}')
print(f'{window_width}x{window_height}+{positionLeft}+{positionTop}')

#windows sizes
#window.minsize(200, 100)
#window.maxsize(8000, 8000)
#window.resizable(False,True)

#screen attributes
print(window.winfo_geometry())
#gets screen details
#print(window.winfo_screenheight())
#print(window.winfo_screenwidth())

#window attributes
#window.attributes('-alpha',0.1)#the higher the number the more visible it is with 1 being the default and 0 being invisible
#window.attributes('-topmost',False)#true always puts this window above others, while false is the default
#window.attributes('-disable',True)#true makes this window uncloseable only way to close it is with task manager or security event
#window.attributes('-fullscreen', True)#starts the app in full screen, doesnt show menu options so you cant close it easily

#title bar
#window.overrideredirect(True)#false shows titlebar and all, true hides it but still allows interaction with the program
#grip= ttk.Sizegrip(window)#creates a resize icon
#grip.place(relx=1.0, rely= 1.0, anchor= 'se')#places the resize icon on bottom right corner of the screen

#security event
window.bind('<Escape>', lambda event: window.quit())#quits the window once esc is pressed

#run
window.mainloop()