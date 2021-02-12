from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

import Modules.main2 as ma
import Modules.register as regi
import Modules.forget as fg
root = Tk()
root.title("VRMS")
root.iconbitmap("images\mainlogo.ico")
root.configure(bg="#24292e")
root.geometry("800x500")
ProfileMain=Label(root)


def registerfn():
    username = regi_user.get()
    password = regi_pass.get()
    pass2 = regi_passcheck.get()
    mail = regi_email.get()

    if len(username) < 4 or len(username)>12:
        messagebox.showerror("Input Error","Username should be of length 4 - 12")
        return
    
    if len(password) < 4 or len(password)>12:
        messagebox.showerror("Input Error","Password should be of length 4 - 12")
        return

    i = regi.call(username,password,mail)
    if i == -1:
        messagebox.showinfo("Registration Error","Username already exsists")
        return

    if password != pass2:
        messagebox.showerror("Input Error","Passwords don't match !")
        return

    if i == 0:
        messagebox.showinfo("Registration","Registration Complete")


def check() :
    us = loginuser.get()
    pas = loginpass.get()

    I = regi.check(us,pas)
    if I == 0:
        root.destroy()
        ma.call()
    else:
        msg = Label(root,text="Invalid Credentials")
        msg.grid(row=4,column=0)

def rn():
    regi.call()
def fp ():
    fg.call()
#Logo
logo=ImageTk.PhotoImage(Image.open ("images\codeowls.png"),width=10, height =50)
main = Label(root,image=logo,borderwidth="0")

#Login labels, Buttons and griding
looogin= Label(root,text="login here")
loginuser=Entry(root,text="Enter Username")
loginpass=Entry(root,text="Enter Password",show="*")
login=Button(root,text="Login",command=check)
fp= Button(root,text="Forgot Password ?", command=fp)

loginuser.grid(row=1,column=0)
loginpass.grid(row=2,column=0)
login.grid(row=3,column=0)
looogin.grid(row=0,column=0)
fp.grid(row=5,column=0)


#Registration Labels, Buttons and  grid
registration= Label(root,text="Register Now")
regi_user = Entry(root,text="Enter Username")
regi_pass = Entry(root,text = "Enter  password")
regi_passcheck = Entry(root,text = "Re-nter password")
regi_email = Entry(root,text = "Enter Mail")
register = Button(root,text="Register Now",command=registerfn)

registration.grid(row=0,column=6)
regi_user.grid(row=2,column=6)
regi_pass.grid(row=3,column=6)
regi_passcheck.grid(row=4,column=6)
regi_email.grid(row=5,column=6)
register.grid(row=6,column=6)

root.mainloop()