"""
Do the GUI(10 mins)
A Simple interest calculator
"""

from tkinter import *
from tkinter import messagebox

def cmdreset():
    #print("Won ti click me o")
    principal.set("0")
    rate.set("0")
    time.set("0")


def cmdcalculate():
    p = principal.get()
    r = rate.get()
    t = time.get()

    if (p.isdigit() or (p.count(".") <2 and p.replace(".","").isdigit())) and\
       (r.isdigit() or (r.count(".") <2 and r.replace(".","").isdigit())) and \
       (t.isdigit() or (t.count(".") <2 and t.replace(".","").isdigit())):
        p = float(p)
        r = float(r)
        t = float(t)
        si = p* r * t / 100
        si = round(si,2)

        ans["text"] = f"Simple interest = ${si}"
    else:
        messagebox.showerror("Invalid Input",\
            "One of Principal, rate or time is not correctly entered")

    
si_root = Tk()
si_root.title("SI Calculator")
si_root.geometry("310x350")
si_root["bg"] = "light green"
#===============Text Variables=================
principal = StringVar()
rate = StringVar()
time = StringVar()

#==============The Header Label======================
Label(si_root,text = "Halogen Simple Interest\nCalculator", bg = si_root["bg"]\
      ,font = "Calibri 15 bold").grid(row = 1, column = 1, columnspan = 2)

Label(si_root, text = "Principal", font = "Calibri 13", bg = si_root["bg"]).\
               grid(row = 3, column = 1, padx = 7, pady = 3)
Label(si_root, text = "Rate", font = "Calibri 13", bg = si_root["bg"]).\
               grid(row = 3, column = 2, padx = 7, pady = 3)

txtp = Entry(si_root, textvariable = principal,font = "Calibri 13", \
             width = 15).grid(row = 4, column = 1, padx = 7, pady = 3)
txtr = Entry(si_root, textvariable = rate,font = "Calibri 13", \
             width = 15).grid(row = 4, column = 2, padx = 7, pady = 3)

Label(si_root, text = "Time", font = "Calibri 13", bg = si_root["bg"]).\
               grid(row = 5, column = 1, columnspan = 2\
                    , padx = 7, pady = 3)

txtt = Entry(si_root, textvariable = time,font = "Calibri 13", \
             width = 15).grid(row = 6, column = 1, padx = 7, pady = 3\
                              ,columnspan = 2)
btnreset = Button(si_root, command = cmdreset, width = 10, text =\
                  "Reset",font = "Calibri 14").grid(row = 7, column = 1, \
                                                    padx = 7, pady = 5)
btncalc = Button(si_root, command = cmdcalculate, width = 10, text =\
                 "Calculate",font = "Calibri 14").grid(row = 7, column = 2,\
                                                       padx = 7, pady = 5)

ans =Label(si_root, text = "", font = "Calibri 15 bold", bg = si_root["bg"])
ans.grid(row = 8, column = 1, columnspan = 2, padx = 7, pady = 7)

frame1 = Frame(si_root, width = 45, borderwidth = 3)
frame1["bg"] = "red"
frame1.grid(row = 9, column = 1, columnspan = 2)

ans1 =Label(frame1, text = "jkerhiubirueg", font = "Calibri 15 bold")
#ans1["bg"] = frame1["bg"]
ans1.pack()

principal.set("0")
rate.set("0")
time.set("0")

si_root.mainloop()


def cmdcalculate():
    
    p = float(principal.get())
    r = float(rate.get())
    t = float(time.get())
    si = p* r * t / 100
    si = round(si,2)

    ans["text"] = f"Simple interest = ${si}"

