from tkinter import *
from PIL import ImageTk,Image
import calculator as calc
import notesmod as n
import books as b
import videos as v

root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#344e5c")
root.geometry("1000x500")


def books() :
    b.books(root)

def videos() :
    v.videos(root)

def calculator() :
    calc.call()

def games() :
    return 0

def note():
    Phynotes = Button(root,text="EPHY",padx=25.5,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=phy)
    CSEnotes = Button(root,text="ECSE",padx=27,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=cse)
    EECEnotes = Button(root,text="EECE",padx=27,pady=10,fg="red",bg="#344e5c",borderwidth=0,command = eece)
    EMATnotes = Button(root,text="EMAT",padx=25,pady=10,fg="red",bg="#344e5c",borderwidth=0,command = math)

    Phynotes.grid(row = 3, column = 1)
    CSEnotes.grid(row = 5, column = 1)
    EECEnotes.grid(row = 7, column = 1)
    EMATnotes.grid(row = 9, column = 1)

    #blank
    blank = []
    j = 2
    for i in range(4):
        blank.append(Label(root, text=" Trying to make it long ",fg="#344e5c",bg="#344e5c"))
        blank[i].grid(row = j, column=1)
        j += 2
    return 0

def phy():
    n.phys(root)

def math():
    n.math(root)

def eece():
    n.eece(root)

def cse():
    n.cse(root)

Noteframe = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
Noteframe.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)

Main = LabelFrame(root, padx=200,pady=20,bg="#344e5c",width=200,height=200)
Main.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)


logo=ImageTk.PhotoImage(Image.open (r"images\redbull.png"),width=10, height =50)
main = Label(Main,image=logo)
main.grid(row=0,column=0)


#Basic Label
mainlabel1 = Label(root,pady=0,bg="#344e5c")
mainlabel2 = Label(root, text="",fg="red",bg="#344e5c")
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
mainlabel1.grid(row=0,column =0)
mainlabel2.grid(row=1,column=0)
booksnotes.grid(row=1,column=2)
videosnotes.grid(row=1,column=4)
gamesnotes.grid(row=1,column=6)
notesnotes.grid(row=1,column=8)
calculatornotes.grid(row=1,column=10)

#Blank space ?
blank = []
j = 2
for i in range(4):
    blank.append(Label(root, text=" Trying to make it long ",fg="#344e5c",bg="#344e5c"))
    blank[i].grid(row = j, column=1)
    j += 2


root.mainloop()