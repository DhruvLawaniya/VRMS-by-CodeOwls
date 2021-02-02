from tkinter import *
from PIL import ImageTk,Image

import Modules.main2 as ma
root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#24292e")
root.geometry("500x500")
ProfileMain=Label(root)
def check() :
    us=u.get()
    pas=p.get()
    us1="Admin"
    ps1="abc123"
    txt="Invalid Credentials"
    if(us==us1):
        if(pas==ps1):
            txt="Autorized"
            ma.call()
        else:
            txt="Invalid Credentials"
    elif(us==us1):
        if(pas==ps1):
            txt="Autorized"
        else:
            txt="Invalid Credentials"
    elif(us==us1):
        if(pas==ps1):
            txt="Autorized"
        else:
            txt="Invalid Credentials"
    elif(us==us1):
        if(pas==ps1):
            txt="Autorized"

        else:
            txt="Invalid Credentials"
    msg=Label(root,text=txt)
    msg.grid(row=3,column=0)
#Logo
logo=ImageTk.PhotoImage(Image.open ("images\codeowls.png"),width=10, height =50)
main = Label(root,image=logo,borderwidth="0")
main.grid(row=5,column=0)
u=Entry(root,text="Enter Username")
p=Entry(root,text="Enter Password")
l=Button(root,text="Login",command=check)
u.grid(row=0,column=0)
p.grid(row=1,column=0)
l.grid(row=2,column=0)
root.mainloop()