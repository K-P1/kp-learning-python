import tkinter as tk
from tkinter import ttk
#event binding in tkinter
#functions
def get_pos(event):
    print(f"x: {event.x} y:{event.y}")

# window
window= tk.Tk()
window.title("Event binding")
window.geometry('600x500')

#tkinter variables

#widgets
text= tk.Text(window)
text.pack()

entry= ttk.Entry(window)
entry.pack()

button= ttk.Button(window, text='a button')
button.pack()

#events
window.bind('<Alt-KeyPress-a>', lambda event: print(f'an {event}'))
window.bind('<KeyPress>', lambda event: print(f'an {event.char}'))
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))
text.bind('<Shift-MouseWheel>', lambda event: print('scrollin thru smthin'))

#text.bind('<Motion>', get_pos)
#run
window.mainloop()