#Menus
import tkinter as tk
from tkinter import ttk

# window
window= tk.Tk()
window.title("Menu")
window.geometry('600x400')

#menu
menu= tk.Menu(window)

#submenu
file_menu= tk.Menu(menu, tearoff= False)
file_menu.add_command(label= 'New', command= lambda: print("New File"))
file_menu.add_command(label= 'New1', command= lambda: print("New File"))
file_menu.add_command(label= 'New2', command= lambda: print("New File"))
share= tk.Menu(menu, tearoff= False)
share.add_command(label='Facebook', command=lambda:print("Share on Facebook"))
share.add_command(label="Instagram", command=lambda:print("Share on Insta"))
file_menu.add_cascade(label='share', menu= share)
menu.add_cascade(label='file', menu= file_menu)
file_menu.add_cascade(label='help', menu= None)


window.configure(menu=menu)#acts like pack but for menus


#menu button
menu_button= ttk.Menubutton(window, text= 'Menu')
menu_button.pack()

button_submenu= tk.Menu(menu_button, tearoff= False)
button_submenu.add_command(label= 'New', command= lambda: print("New File"))
button_submenu.add_checkbutton(label= 'New')
#menu_button.configure(menu= button_submenu) #can be used interchangably with the below line, they do the same thing
menu_button['menu']= button_submenu

#run
window.mainloop()