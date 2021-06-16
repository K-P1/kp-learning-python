from tkinter import *
from tkinter import messagebox

user_registered_name = ""
user_registered_username = ""
user_registered_password = ""

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
    global nameVar
    global usernameVar
    global passwordVar
    global win2
    
    win2 = Tk()
    win2.title("Registration Window")
    win2.geometry("525x350")
    Label(win2,text = "Kindly fill the form\nBelow",font = \
        "Verdanas 24").pack(pady = 7)

    nameVar = StringVar(win2)
    usernameVar = StringVar(win2)
    passwordVar = StringVar(win2)

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

    btnReg = Button(win2,command = cmdRegister,text = \
        "Register",font = "Verdanas 15")
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
    global userentry
    global passwordentry

    win3 = Tk()
    win3.title("Login Window")
    win3.geometry("525x300")
    Label(win3,text = "Kindly fill the form\nBelow to Login",font = \
        "Verdanas 24").pack(pady = 7)

    userentry = StringVar(win3)
    passwordentry = StringVar(win3)

    loginform = Frame(win3)
    loginform.pack()

    Label(loginform,text = "Username:",font = \
        "Verdanas 15").grid(row = 1, column = 1)
    Label(loginform,text = "Password:",font = \
        "Verdanas 15").grid(row = 2, column = 1)

    ent11 = Entry(loginform,textvariable = userentry,\
        font = "Verdanas 15")
    ent11.grid(row = 1, column = 2, padx = 7, pady = 10)
    ent22 = Entry(loginform,textvariable = passwordentry,\
        font = "Verdanas 15")
    ent22.grid(row = 2, column = 2, padx = 7, pady = 10)

    btnLogin = Button(win3,command = cmdLogin,text = \
        "Login",font = "Verdanas 15")
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

def cmdRegister():
    global win2
    global nameVar
    global usernameVar
    global passwordVar

    global user_registered_name
    global user_registered_username
    global user_registered_password

    user_registered_name = nameVar.get()
    user_registered_username = usernameVar.get()
    user_registered_password = passwordVar.get()
    #print("Data Extracted")
    nameVar.set("")
    usernameVar.set("")
    passwordVar.set("")
    #print("Registration Successful")
    messagebox.showinfo("Information",\
         "Registration Successful")

    win2.destroy()

    loginWindow()

def cmdLogin():
    
    global user_registered_username
    global user_registered_password
    global user_registered_name

    global userentry
    global passwordentry

    if userentry.get() == user_registered_username and\
        passwordentry.get()== user_registered_password:
        messagebox.showinfo("Information",\
            f"Hey {user_registered_name},You can proceed to Dashboard")

    else:
        messagebox.showerror("Information",\
            "Wrong Username/Password")


mainwindow()