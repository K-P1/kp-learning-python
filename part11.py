#Note to self: figure out how to link the slider to the label when stop is active

#Slider and progress bar
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

#sliders and progress bar
window= tk.Tk()
window.geometry('250x200')
window.title('sliders and progress bar')
stop_state= False
"""
#slider
scale_int=tk.IntVar(value=15)
slider = ttk.Scale(window, 
                   command= lambda value: print(scale_int.get()), 
                   from_= 0, to= 25, 
                   length= 150, 
                   orient='vertical',
                   variable=scale_int)
slider.pack()

#progress bar
progress_bar= ttk.Progressbar(window, 
                              variable= scale_int,
                              maximum=25,
                              orient='horizontal',
                              mode='determinate',
                              length=110)
progress_bar.pack()
#progress_bar.start(1000)
#progress_bar.stop()

#scrolled text
scroled_text= scrolledtext.ScrolledText(window,width=100,height=12)
scroled_text.pack()"""

def update_progress_bar():
    if stop_state== False:
        v= bar_value.get() 
        x= v+ 1
        if x==101:
            label_value.set("      100%\n Completed")
            return
        bar_value.set(x)
        label_value.set(str(x)+'%')

        window.after(1000, update_progress_bar)
    else:
        return
        

def reset():
    global stop_state
    bar_value.set(0)
    label_value.set('0%')
    update_progress_bar()

def stop():
    global stop_state
    if stop_state == False:
        stop_state= True
        btn_label.set('Start')
    else:
        stop_state= False
        btn_label.set('Stop')
        update_progress_bar()

def active(self):
    x=bar_value.get()
    label_value.set(str(x)+'%')
#    update_progress_bar()

bar_value= tk.IntVar(value=0)
label_value= tk.StringVar(value='0%')
btn_label= tk.StringVar(value='Stop')
P_bar= ttk.Progressbar(window,orient= 'vertical', variable= bar_value,maximum=100)
P_bar.pack()
label= ttk.Label(window,textvariable=label_value)
label.pack()
slider= ttk.Scale(window,orient= 'horizontal',variable= bar_value,from_= 0, to= 100, command= active)
slider.pack()
reset_btn= ttk.Button(window,text='Reset', command= reset)
reset_btn.pack()
stop_btn= ttk.Button(window,text='Stop',textvariable=btn_label, command= stop)
stop_btn.pack()
window.after(1000, update_progress_bar)


#run
window.mainloop()