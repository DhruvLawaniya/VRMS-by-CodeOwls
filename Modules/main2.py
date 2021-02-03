from tkinter import *
from PIL import ImageTk,Image
import Modules.quizframe as qu
import Modules.notes as n
import Modules.academic as aca
import Modules.books as b
import Modules.videos as v
import Modules.misc as m


def call(str):
    global root
    root = Toplevel()
    root.title("Learning Management System By Code Owls")
    root.configure(bg="#24292e")
    root.geometry("900x500")

    #Functions
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

    def quiz():
        home()
        qu.notesmain(root)

    def misc():
        home()
        m.notesmain(root)

    def note():
        home()
        n.notesmain(root)

    #Frames
    Top = LabelFrame(root,bg = "#24292e",width=200,height=10,borderwidth=0)
    Top.grid(row = 0, column=0,columnspan=7,padx=10,pady=20)

    Main = LabelFrame(root, padx=200,pady=20,bg="#1d2125",width=200,height=200)
    Main.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

    MainLeft = LabelFrame(root,bg="#24292e",pady=28,borderwidth=0)
    MainLeft.grid(row = 3, column = 0,rowspan=10,padx=10)

    #Logo
    logo=ImageTk.PhotoImage(Image.open ("images\codeowls.png"),width=10, height =50)
    main = Label(Main,image=logo,borderwidth="0")
    main.grid(row=0,column=0)

    #Buttons
    homebutton = Button(Top,text="HOME",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=home)
    booksnotes = Button(Top,text="Books",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1, command=books)
    videosnotes = Button(Top,text="Videos",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=videos)
    miscnotes = Button(Top,text="Miscellaneous",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=misc)
    notesnotes = Button(Top,text="Notes",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= note)
    quiznotes = Button(Top,text="Practice Quiz",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= quiz)
    Academic = Button(Top,text="Academic",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= academic)
    welcome = Label(Top,text=("Welcome,"+str),padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1)

    #Postion of Buttons
    homebutton.grid(row=0,column=0)
    booksnotes.grid(row=0,column=2)
    videosnotes.grid(row=0,column=8)
    miscnotes.grid(row=0,column=12)
    notesnotes.grid(row=0,column=4)
    quiznotes.grid(row=0,column=10)
    Academic.grid(row=0,column=6)
    welcome.grid(row=0,column=18)

    #Blank spaces
    blank = []
    for i in range(18):
        blank.append(Label(MainLeft, text=" Trying to make it long ",fg="#24292e",bg="#24292e"))
        blank[i].grid(row = i, column=1)
    j=1
    blanktop = []
    for i in range(6):
        blanktop.append(Label(Top, text=" k k k ",fg="#24292e",bg="#24292e"))
        blanktop[i].grid(row = 0, column=j)
        j+=2

    root.mainloop()