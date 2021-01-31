from tkinter import *
from PIL import ImageTk,Image
import Modules.calculator as calc
import Modules.notes as n
import Modules.academic as aca
import Modules.books as b
import Modules.videos as v
import Modules.games as g

root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#24292e")
root.geometry("900x500")

def home():
    Main.lift()
    MainLeft.lift()
    
def books():
    home()
    b.books(root)

def videos():
    home()
    v.videos(root)

def academic():
    home()
    aca.academic(root)

def calculator():
    home()
    calc.call()

def games():
    home()
    g.games(root)
    return 0

def note():
    home()
    n.notesmain(root)

Top = LabelFrame(root,bg = "#24292e",width=200,height=10,borderwidth=0)
Top.grid(row = 0, column=0,columnspan=7,padx=10,pady=20)

Main = LabelFrame(root, padx=200,pady=20,bg="#1d2125",width=200,height=200)
Main.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

MainLeft = LabelFrame(root,bg="#24292e",pady=28,borderwidth=0)
MainLeft.grid(row = 3, column = 0,rowspan=10,padx=10)

logo=ImageTk.PhotoImage(Image.open (r"images\redbull.png"),width=10, height =50)
main = Label(Main,image=logo,borderwidth="0")
main.grid(row=0,column=0)

blank = []
for i in range(12):
    blank.append(Label(MainLeft, text=" Trying to make it long ",fg="#24292e",bg="#24292e"))
    blank[i].grid(row = i, column=1)

#Basic Label

homebutton = Button(Top,text="HOME",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=home)
booksnotes = Button(Top,text="Books",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1, command=books)
videosnotes = Button(Top,text="Videos",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=videos)
gamesnotes = Button(Top,text="Games",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=games)
notesnotes = Button(Top,text="Notes",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= note)
calculatornotes = Button(Top,text="Calculator",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= calculator)
Academic = Button(Top,text="Academic",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= academic)

homebutton.grid(row=0,column=0)
booksnotes.grid(row=0,column=2)
videosnotes.grid(row=0,column=8)
gamesnotes.grid(row=0,column=12)
notesnotes.grid(row=0,column=4)
calculatornotes.grid(row=0,column=10)
Academic.grid(row=0,column=6)

j=1
blanktop = []
for i in range(6):
    blanktop.append(Label(Top, text=" k k k ",fg="#24292e",bg="#24292e"))
    blanktop[i].grid(row = 0, column=j)
    j+=2

root.mainloop()