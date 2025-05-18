import gui
from tkinter import *
import tkinter.messagebox as tmsg

# Note : Downlaod Xampp from google and start Apache and MySQL under this Application

# If you are running this code first time, you have to comment out the following lines of code
# Note : You can comment out and comment in the lines of code by selecting them and pressing Ctrl + /
# To create database run this command

# import pymysql as ms
# myobj = ms.connect(host = "localhost", user = "root", password="")
# cursorobj = myobj.cursor()
# try:
#     db="create database Project"
#     cursorobj.execute(db)
#     print("Database created")
# except:
#     print("Database error...")

# Don't run this command again if database has been created once, please comment in the above code

# Now, run the below command to create a table

# import pymysql as ms
# myobj = ms.connect(host = "localhost", user = "root", password="",database="Project")
# mysqlc = myobj.cursor()
# ct = "create table Data(user varchar(255) primary key, password varchar(255))"
# mysqlc.execute(ct)  # Here, user and password are fields names

# Please comment in the above code and never run it twice

# Please comment out the below code forever whenever you are running this code

import pymysql as ms
myobj = ms.connect(host = "localhost", user = "root", password="",database="Project")
mysqlc = myobj.cursor()

def on_entry_click(event):
    # Clear the placeholder text when the entry is clicked
    if entry.get() == "Enter username here...":
        entry.delete(0,END)
        entry.config(fg='black')

def on_focusout(event):
    # Restore the placeholder text if the entry is empty
    if entry.get() == "":
        entry.insert(0, "Enter username here...")
        entry.config(fg='grey')

def on_pentry_click(event):
    # Clear the placeholder text when the entry is clicked
    if pentry.get() == "Enter password here...":
        pentry.delete(0,END)
        pentry.config(fg='black')

def on_pfocusout(event):
    # Restore the placeholder text if the entry is empty
    if pentry.get() == "":
        pentry.insert(0, "Enter password here...")
        pentry.config(fg='grey')    

def signup():
    def on_entry_click(event):
    # Clear the placeholder text when the entry is clicked
        if entry1.get() == "Enter username here...":
            entry1.delete(0,END)
            entry1.config(fg='black')

    def on_focusout(event):
    # Restore the placeholder text if the entry is empty
        if entry1.get() == "":
            entry1.insert(0, "Enter username here...")
            entry1.config(fg='grey')

    def on_pentry_click(event):
        # Clear the placeholder text when the entry is clicked
        if pentry1.get() == "Enter password here...":
            pentry1.delete(0,END)
            pentry1.config(fg='black')

    def on_pfocusout(event):
        # Restore the placeholder text if the entry is empty
        if pentry1.get() == "":
            pentry1.insert(0, "Enter password here...")
            pentry1.config(fg='grey')

    def on_cpentry_click(event):
        # Clear the placeholder text when the entry is clicked
        if cpentry1.get() == "Enter password again...":
            cpentry1.delete(0,END)
            cpentry1.config(fg='black')

    def on_cpfocusout(event):
        # Restore the placeholder text if the entry is empty
        if cpentry1.get() == "":
            cpentry1.insert(0, "Enter password again...")
            cpentry1.config(fg='grey')

    screen = Toplevel(root)
    screen.title("DESKTOP AI ASSISTANT")
    screen.geometry("1536x864")
    screen.minsize(1536,864)
    screen.configure(background = "black")
    aa = Label(screen,text = "DESKTOP AI ASSISTANT", bg="green",fg="white",font="comicsansms 30 bold",padx = 50,pady = 30,borderwidth = 20,relief=RIDGE)
    aa.pack(anchor="center",pady=20)

    user1 = Label(screen, text = "USERNAME",bg="red",fg="cyan",font="comicsansms 20 bold",padx = 5,pady = 5)
    user1.pack(padx=30,pady=30)
    uservalue1 = StringVar()

    # Create the Entry widget
    entry1= Entry(screen,textvariable= uservalue1,width=70,bg="pink",fg="black",borderwidth=10,relief=SUNKEN,font=("Times new roman",20,"bold"))
    entry1.insert(0,"Enter username here...")
    entry1.bind("<FocusIn>", on_entry_click)
    entry1.bind("<FocusOut>", on_focusout)
    entry1.pack()

    password1 = Label(screen,text = "PASSWORD",bg="red",fg="cyan",font="comicsansms 20 bold",padx = 5,pady = 5)
    password1.pack(padx=30,pady=30)
    passvalue1 = StringVar()

    # Create the Entry widget
    pentry1 = Entry(screen,textvariable= passvalue1,width=70,bg="pink",fg="black",borderwidth=10,relief=SUNKEN,font=("Times new roman",20,"bold"))
    pentry1.insert(0, "Enter password here...")
    pentry1.bind("<FocusIn>", on_pentry_click)
    pentry1.bind("<FocusOut>", on_pfocusout)
    pentry1.pack()
    warn = Label(screen, text = "Please enter digits only in password",bg = "black",fg = "white",font=("Times new roman",15))
    warn.pack()

    cpassword1 = Label(screen,text = "CONFIRM PASSWORD",bg="red",fg="cyan",font="comicsansms 20 bold",padx = 5,pady = 5)
    cpassword1.pack(padx=30,pady=30)
    cpassvalue1 = StringVar()

    # Create the Entry widget
    cpentry1 = Entry(screen,textvariable= cpassvalue1,width=70,bg="pink",fg="black",borderwidth=10,relief=SUNKEN,font=("Times new roman",20,"bold"))
    cpentry1.insert(0, "Enter password again...")
    cpentry1.bind("<FocusIn>", on_cpentry_click)
    cpentry1.bind("<FocusOut>", on_cpfocusout)
    cpentry1.pack()

    def submit1():
        if passvalue1.get() == cpassvalue1.get() :
            if passvalue1.get().isdigit() :
                try:
                    ins="insert into data(user,password) values(%s,%s)"
                    # TO input single data at a time
                    tu=(uservalue1.get(),passvalue1.get())
                    mysqlc.execute(ins,tu)

                    # # To input multiple data at a time
                    # tu=[("Ansh","3242"),("immortal","3242")]
                    # mysqlc.executemany(ins,tu)

                    myobj.commit();
                    print("Data inserted")
                    tmsg.showinfo("SUBMIT","yOUR DETAILS HAVE BEEN SUBMITTED")
                except:
                    print("Data error...")
            else:
                tmsg.showerror("Error","Please enter numbers only")
        elif uservalue1.get() == "Enter username here...":
            tmsg.showerror("Error","Please enter username")

        elif passvalue1.get() == "Enter password here..." and  cpassvalue1.get() == "Enter password again...":
            tmsg.showerror("Error","Please enter password")
        else:
            tmsg.showerror("Error","Please enter same password in both fields")
    Button(screen,text="Submit",font=("Times new roman",20,"bold"),command=submit1).place(x=690,y=700)



root = Tk()
root.title("DESKTOP AI ASSISTANT")
root.geometry("1536x864")
root.minsize(1536,864)
root.configure(background = "black")
a = Label(text = "DESKTOP AI ASSISTANT", bg="green",fg="white",font="comicsansms 30 bold",padx = 50,pady = 30,borderwidth = 20,relief=RIDGE)
a.pack(anchor="center",pady=20)

user = Label(root, text = "USERNAME",bg="red",fg="cyan",font="comicsansms 20 bold",padx = 5,pady = 5)
user.pack(padx=30,pady=30)
uservalue = StringVar()

# Create the Entry widget
entry= Entry(root,textvariable= uservalue,width=70,bg="pink",fg="black",borderwidth=10,relief=SUNKEN,font=("Times new roman",20,"bold"))
entry.insert(0,"Enter username here...")
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)
entry.pack()

password = Label(root,text = "PASSWORD",bg="red",fg="cyan",font="comicsansms 20 bold",padx = 5,pady = 5)
password.pack(padx=30,pady=30)
passvalue = StringVar()

# Create the Entry widget
pentry = Entry(root,textvariable= passvalue,width=70,bg="pink",fg="black",borderwidth=10,relief=SUNKEN,font=("Times new roman",20,"bold"))
pentry.insert(0, "Enter password here...")
pentry.bind("<FocusIn>", on_pentry_click)
pentry.bind("<FocusOut>", on_pfocusout)
pentry.pack()

def getvalue():
    print("Username:",uservalue.get())
    print("Passsword:",passvalue.get())
    if uservalue.get() == "Enter username here..." and passvalue.get() == "Enter password here...":
        tmsg.showerror("Error","Please enter username and password")
    elif uservalue.get() == "Enter username here..." or uservalue.get() == "":
        tmsg.showerror("Error","Please enter username")
    elif passvalue.get() == "Enter password here..." or passvalue.get() == "":
        tmsg.showerror("Error","Please enter password")
    elif passvalue.get().isdigit() == False :
        tmsg.showerror("Error","Please enter numbers only")
    else:
        q = "select password from data where user = %s"
        mysqlc.execute(q,(uservalue.get(),))
        e = mysqlc.fetchone()
        if e != None:
            r = ("{:<20}".format(e[0]))
            print("type of r : ",type(r),r)
            print("type of password : ",type(passvalue.get()),passvalue.get())
            if int(r) == int(passvalue.get()):
                tmsg.showinfo("Enter","You have logged in successfully")
                gui.GUI()
                
            else:
                tmsg.showerror("Error","Password is incorrect")
        else:
            tmsg.showerror("Error","Username does not exist")
            
W = Label(text = "Didn't have an account?",font = ("Times new roman",40,"bold"),bg="black",fg="cyan").place(x=400,y=550)

Button(text = "Sign up",font = ("Times new roman",30,"bold"),command = signup).place(x=1000,y = 550)

Button(text="Submit",font=("Times new roman",30,"bold"),command=getvalue).place(x=690,y=670)

root.mainloop()