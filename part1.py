import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
# introduction to tkinter and ttkinter
"""
theme types:
cosmo
flatly
litera
minty
lumen
sandstone
yeti
pulse
united
morph
journal
darkly
superhero
solar
cyborg
vapor
simplex
cerculean
"""
#functions
def convert():
    # Get the input in miles
    mile_input = entry_int.get()

    # Convert miles to kilometers
    km_output = mile_input * 1.61

    # Set the output to the converted value
    output_string.set(km_output)
    
# window
window = ttk.Window(themename= 'darkly')
window.title('demo')
window.geometry('300x150')

# title
title_label = ttk.Label(master = window, text = "Miles to kilometer", font = "calibri 24 bold").pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int= tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable= entry_int).pack(side='left')
button = ttk.Button(master=input_frame, text= "convert", command= convert).pack()
input_frame.pack()

#output
output_string= tk.StringVar()
output_label = ttk.Label(master= window, text= 'output', font= 'calibri 24', textvariable= output_string).pack()

# run
window.mainloop()