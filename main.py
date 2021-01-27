from tkinter import *
from PIL import ImageTk,Image
import Modules.calculator as calc
import Modules.notes as n

import Modules.books as b
import Modules.videos as v

root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#24292e")
root.geometry("1000x500")

def home():
    Main.lift()
    MainLeft.lift()
    
def books() :
    b.books(root)

def videos() :
    v.videos(root)

def calculator() :
    calc.call()

def games() :
    return 0

def note():
    LeftFrame = LabelFrame(root,bg="#1d2125",pady=28,borderwidth=0)
    LeftFrame.grid(row = 3, column = 0,rowspan=10,padx=10)

    Phynotes = Button(LeftFrame,text="EPHY",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=0,command=phy)
    CSEnotes = Button(LeftFrame,text="ECSE",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=0,command=cse)
    EECEnotes = Button(LeftFrame,text="EECE",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=0,command = eece)
    EMATnotes = Button(LeftFrame,text="EMAT",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=0,command = math)

    Phynotes.grid(row = 0, column = 1)
    CSEnotes.grid(row = 2, column = 1)
    EECEnotes.grid(row = 4, column = 1)
    EMATnotes.grid(row = 6, column = 1)
 
    #blank
    blank = []
    j = 1
    for i in range(4):
        blank.append(Label(LeftFrame, text=" Trying to make it long ",fg="#1d2125",bg="#1d2125"))
        blank[i].grid(row = j, column=1)
        j += 2

    LeftFrame.lift()

def phy():
    n.phys(root)

def math():
    n.math(root)

def eece():
    n.eece(root)

def cse():
    n.cse(root)


Main = LabelFrame(root, padx=200,pady=20,bg="#1d2125",width=200,height=200)
Main.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

MainLeft = LabelFrame(root,bg="#1d2125",pady=28,borderwidth=0)
MainLeft.grid(row = 3, column = 0,rowspan=10,padx=10)

blank = []
for i in range(8):
    blank.append(Label(MainLeft, text=" Trying to make it long ",fg="#1d2125",bg="#1d2125"))
    blank[i].grid(row = i, column=1)


logo=ImageTk.PhotoImage(Image.open (r"images\redbull.png"),width=10, height =50)
main = Label(Main,image=logo)
main.grid(row=0,column=0)


#Basic Label
mainlabel1 = Label(root,pady=0,bg="#1d2125")
mainlabel2 = Label(root, text="",fg="white",bg="#1d2125")
homebutton = Button(root,text="HOME",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=home)
booksnotes = Button(root,text="Books",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1, command=books)
videosnotes = Button(root,text="Videos",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=videos)
gamesnotes = Button(root,text="Games",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=games)
notesnotes = Button(root,text="Notes",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= note)
calculatornotes = Button(root,text="Calculator",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= calculator)

#blank space
#blankt = []
#j = 3
#for i in range(4):
#    blankt.append(Label(root, text="     can't see me   ",fg="#1d2125",bg="#1d2125"))
#    blankt[i].grid(row = 1, column=j)
#    j += 2

#pack in grid
homebutton.grid(row=0,column=0)
mainlabel1.grid(row=0,column =0)
booksnotes.grid(row=0,column=1)
videosnotes.grid(row=0,column=2)
gamesnotes.grid(row=0,column=3)
notesnotes.grid(row=0,column=4)
calculatornotes.grid(row=0,column=5)

root.mainloop()