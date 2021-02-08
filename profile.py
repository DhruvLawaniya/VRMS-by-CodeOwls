from tkinter import *
from PIL import ImageTk,Image

import Modules.main2 as ma
import Modules.register as regi
root = Tk()
root.title("VRMS")
root.configure(bg="#24292e")
root.geometry("180x300")
ProfileMain=Label(root)
def check() :
    us=u.get()
    pas=p.get()
    us1=""
    ps1=""
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
            msg.grid(row=3,column=0)
            ma.call(us1)
    elif(us==us2):
        if(pas==ps2):
            txt="Autorized"
            msg=Label(root,text=txt)
            msg.grid(row=3,column=0)
            ma.call(us2)
        else:
            txt="Invalid Credentials"
    elif(us==us3):
        if(pas==ps3):
            txt="Autorized"
            msg=Label(root,text=txt)
            msg.grid(row=3,column=0)
            ma.call(us3)
        
    elif(us==us4):
        if(pas==ps4):
            txt="Autorized"
            msg=Label(root,text=txt)
            msg.grid(row=3,column=0)
            ma.call(us4)

        
    elif(us==us5):
        if(pas==ps5):
            txt="Autorized"
            msg=Label(root,text=txt)
            msg.grid(row=3,column=0)
            ma.call(us5)
            

        
    msg=Label(root,text=txt)
    msg.grid(row=3,column=0)

def rn():
    regi.call()
#Logo
logo=ImageTk.PhotoImage(Image.open ("images\codeowls.png"),width=10, height =50)
main = Label(root,image=logo,borderwidth="0")
main.grid(row=5,column=0)

u=Entry(root,text="Enter Username")
p=Entry(root,text="Enter Password",show="*")
l=Button(root,text="Login",command=check)
rn= Button(root,text="Register Now", command=rn)

u.grid(row=0,column=0)
p.grid(row=1,column=0)
l.grid(row=2,column=0)
rn.grid(row=3,column=0)
root.mainloop()