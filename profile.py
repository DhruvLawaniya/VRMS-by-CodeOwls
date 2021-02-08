from tkinter import *
from PIL import ImageTk,Image

import Modules.main2 as ma
import Modules.register as regi
import Modules.forget as fg
root = Tk()
root.title("VRMS")
root.iconbitmap("images\mainlogo.ico")
root.configure(bg="#24292e")
root.geometry("800x500")
ProfileMain=Label(root)
def check() :
    us=u.get()
    pas=p.get()
    us1="Admin"
    ps1="Admin"
    us2="Dhruv"
    ps2="Dhruv"
    us3="Rahul"
    ps3="Rahul"
    us4="Alan"
    ps4="Alan"
    us5="Adwit"
    ps5="Adwit"
    txt="Invalid Credentials"
    if(us==us1):
        if(pas==ps1):
            txt="Autorized"
            msg=Label(root,text=txt)
            msg.grid(row=4,column=0)
            ma.call(us1)
    elif(us==us2):
        if(pas==ps2):
            txt="Autorized"
            msg=Label(root,text=txt)
            msg.grid(row=4,column=0)
            ma.call(us2)
        else:
            txt="Invalid Credentials"
    elif(us==us3):
        if(pas==ps3):
            txt="Autorized"
            msg=Label(root,text=txt)
            msg.grid(row=4,column=0)
            ma.call(us3)
        
    elif(us==us4):
        if(pas==ps4):
            txt="Autorized"
            msg=Label(root,text=txt)
            msg.grid(row=4,column=0)
            ma.call(us4)

        
    elif(us==us5):
        if(pas==ps5):
            txt="Autorized"
            msg=Label(root,text=txt)
            msg.grid(row=4,column=0)
            ma.call(us5)
            

        
    msg=Label(root,text=txt)
    msg.grid(row=4,column=0)

def rn():
    regi.call()
def fp ():
    fg.call()
#Logo
logo=ImageTk.PhotoImage(Image.open ("images\codeowls.png"),width=10, height =50)
main = Label(root,image=logo,borderwidth="0")
#main.grid(row=5,column=0)
#us=Label(root,text=)
looogin= Label(root,text="login here")
u=Entry(root,text="Enter Username")
p=Entry(root,text="Enter Password",show="*")
l=Button(root,text="Login",command=check)

fp= Button(root,text="Forgot Password ?", command=fp)


u.grid(row=1,column=0)
p.grid(row=2,column=0)
l.grid(row=3,column=0)
looogin.grid(row=0,column=0)

fp.grid(row=5,column=0)





rn= Label(root,text="Register Now")
rn.grid(row=0,column=6)

root.mainloop()