from tkinter import *

def mainwindow():
    global win1


    win1 = Tk()
    win1.title("Welcome Window")
    win1.geometry("525x300")
    Label(win1,text = "Welcome to our Homepage",font = \
        "Verdanas 24").pack(pady = 7)

    frame = Frame(win1)
    frame.pack(pady = 30)

    btnRegister = Button(frame, command = cmdReg,text =\
        "Register", font = "Verdanas 16", width = 15,\
            bg = "cyan4")
    btnRegister.grid(row = 1, column = 1, padx = 15)

    btnLogin = Button(frame,command = cmdLogin,text =\
         "Login", font = "Verdanas 16", width = 15,\
             bg = "cyan4")
    btnLogin.grid(row = 1, column = 2, padx = 15)

    win1.mainloop()

def regWindow():
    global name
    global username
    global password
    global win2
    
    nameVar = StringVar()
    usernameVar = StringVar()
    passwordVar = StringVar()
    
    win2 = Tk()
    win2.title("Registration Window")
    win2.geometry("525x350")
    Label(win2,text = "Kindly fill the form\nBelow",font = \
        "Verdanas 24").pack(pady = 7)

    form = Frame(win2)
    form.pack()

    Label(form,text = "Full Name:",font = \
        "Verdanas 15").grid(row = 1, column = 1)
    Label(form,text = "Username:",font = \
        "Verdanas 15").grid(row = 2, column = 1)
    Label(form,text = "Password:",font = \
        "Verdanas 15").grid(row = 3, column = 1)

    ent1 = Entry(form,textvariable = nameVar,font = \
        "Verdanas 15")
    ent1.grid(row = 1, column = 2, padx = 7, pady = 10)
    ent2 = Entry(form,textvariable = usernameVar,font = \
        "Verdanas 15")
    ent2.grid(row = 2, column = 2, padx = 7, pady = 10)
    ent3 = Entry(form,textvariable = passwordVar,font = \
        "Verdanas 15")
    ent3.grid(row = 3, column = 2, padx = 7, pady = 10)

    btnReg = Button(win2,text = "Register",font = "Verdanas 15")
    btnReg["bg"] = "cyan4"
    btnReg["width"] = 15
    btnReg.pack(pady = 10)
    btnBack = Button(win2, command = cmdBack,text = "Go Back",font =\
         "Verdanas 15")
    btnBack["bg"] = "cyan4"
    btnBack["width"] = 15
    btnBack.pack(pady = 10)



    win2.mainloop()


def loginWindow():

    win3 = Tk()
    win3.title("Login Window")
    win3.geometry("525x300")
    Label(win3,text = "Kindly fill the form\nBelow to Login",font = \
        "Verdanas 24").pack(pady = 7)

    loginform = Frame(win3)
    loginform.pack()

    Label(loginform,text = "Username:",font = \
        "Verdanas 15").grid(row = 1, column = 1)
    Label(loginform,text = "Password:",font = \
        "Verdanas 15").grid(row = 2, column = 1)

    ent11 = Entry(loginform,font = \
        "Verdanas 15")
    ent11.grid(row = 1, column = 2, padx = 7, pady = 10)
    ent22 = Entry(loginform,font = \
        "Verdanas 15")
    ent22.grid(row = 2, column = 2, padx = 7, pady = 10)

    btnLogin = Button(win3,text = "Login",font = "Verdanas 15")
    btnLogin["bg"] = "cyan4"
    btnLogin["width"] = 15
    btnLogin.pack(pady = 10)


    win3.mainloop()


def cmdReg():
    global win

    win1.destroy()
    regWindow()

def cmdBack():
    global win2
    win2.destroy()
    mainwindow()

def cmdLogin():
    global win1
    win1.destroy()
    loginWindow()

mainwindow()