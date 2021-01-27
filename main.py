from tkinter import *
from PIL import ImageTk,Image
import Modules.calculator as calc
import Modules.notes as n
#import Modules.links
import Modules.books as b
import Modules.videos as v

root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#344e5c")
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
    LeftFrame = LabelFrame(root,bg="#344e5c",pady=28,borderwidth=0)
    LeftFrame.grid(row = 3, column = 0,rowspan=10,padx=10)

    Phynotes = Button(LeftFrame,text="EPHY",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=phy)
    CSEnotes = Button(LeftFrame,text="ECSE",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=cse)
    EECEnotes = Button(LeftFrame,text="EECE",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command = eece)
    EMATnotes = Button(LeftFrame,text="EMAT",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command = math)

    Phynotes.grid(row = 0, column = 1)
    CSEnotes.grid(row = 2, column = 1)
    EECEnotes.grid(row = 4, column = 1)
    EMATnotes.grid(row = 6, column = 1)
 
    #blank
    blank = []
    j = 1
    for i in range(4):
        blank.append(Label(LeftFrame, text=" Trying to make it long ",fg="#344e5c",bg="#344e5c"))
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


Main = LabelFrame(root, padx=200,pady=20,bg="#344e5c",width=200,height=200)
Main.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

MainLeft = LabelFrame(root,bg="#344e5c",pady=28,borderwidth=0)
MainLeft.grid(row = 3, column = 0,rowspan=10,padx=10)

blank = []
for i in range(8):
    blank.append(Label(MainLeft, text=" Trying to make it long ",fg="#344e5c",bg="#344e5c"))
    blank[i].grid(row = i, column=1)


logo=ImageTk.PhotoImage(Image.open (r"images\redbull.png"),width=10, height =50)
main = Label(Main,image=logo)
main.grid(row=0,column=0)


#Basic Label
mainlabel1 = Label(root,pady=0,bg="#344e5c")
mainlabel2 = Label(root, text="",fg="red",bg="#344e5c")
homebutton = Button(root,text="HOME",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0, command=home)
booksnotes = Button(root,text="Books",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0, command=books)
videosnotes = Button(root,text="Videos",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=videos)
gamesnotes = Button(root,text="Games",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=games)
notesnotes = Button(root,text="Notes",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command= note)
calculatornotes = Button(root,text="Calculator",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command= calculator)

#blank space
blankt = []
j = 3
for i in range(4):
    blankt.append(Label(root, text="     can't see me   ",fg="#344e5c",bg="#344e5c"))
    blankt[i].grid(row = 1, column=j)
    j += 2

#pack in grid
homebutton.grid(row=1,column=0)
mainlabel1.grid(row=0,column =0)
booksnotes.grid(row=1,column=2)
videosnotes.grid(row=1,column=4)
gamesnotes.grid(row=1,column=6)
notesnotes.grid(row=1,column=8)
calculatornotes.grid(row=1,column=10)

root.mainloop()