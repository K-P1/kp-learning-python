#TreeView
import tkinter as tk
from tkinter import ttk
from faker import Faker

#window
window = tk.Tk()
window.geometry('900x400')
window.title('TreeView')

#data
fake= Faker()
first_names=[]
last_names=[]
for x in range(1000):
    first_names.append(fake.first_name())

for x in range(1000):
    last_names.append(fake.last_name())
    

tree = ttk.Treeview(window, 
                    columns=('First Name', 'Last Name', 'Email', 'Address'), 
                    show='headings')
tree.heading('First Name', text='First Name') 
tree.heading('Last Name', text='Last Name') 
tree.heading('Email', text='Email') 
tree.heading('Address', text='Address') 
tree.pack(fill='both', expand=True)

#insert values to table
#index number reps the row inwhich the data will be inserted    index=tk.END will place the data at the last row
for (x,y) in zip(first_names,last_names):
    tree.insert(parent='',
                index=0,
                values= (x,y,f'{x[0]+'_'+y}@gmmail.com',fake.address()))
    
#events
def item_select(_):
    print(tree.selection())
    for i in tree.selection():
        print(tree.item(i)['values'])

def delt(self):
    for i in tree.selection():
        tree.delete(i)

tree.bind('<Delete>',delt)
tree.bind('<<TreeviewSelect>>',item_select)

#items


#run
window.mainloop()