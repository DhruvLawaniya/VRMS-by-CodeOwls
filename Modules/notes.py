from tkinter import *
from PIL import ImageTk,Image
import videos
import games
import notes
import calculator as calc

def books() :
    return 0

def videos() :
    return 0

def calculator() :
    calc.call()

def games() :
    return 0

def notes() :
    return 0



root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#344e5c")
#root.iconbitmap("H:\Mid Sem Project\icon.ico")
root.geometry("1280x600")
    
#Basic Label
mainlabel1 = Label(root,pady=0,bg="#344e5c")
mainlabel2 = Label(root, text="",fg="red",bg="#344e5c")
books_button = Button(root,text="Books",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0, command=books)
videos_button = Button(root,text="Videos",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=videos)
games_button = Button(root,text="Games",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=games)
notes_button = Button(root,text="Notes",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command= notes)
calculator_button = Button(root,text="Calculator",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command= calculator)

#pack in grid
mainlabel1.grid(row=0,column =0)
mainlabel2.grid(row=1,column=0)
books_button.grid(row=1,column=2)
videos_button.grid(row=1,column=4)
games_button.grid(row=1,column=6)
notes_button.grid(row=1,column=8)
calculator_button.grid(row=1,column=10)

#
blankt = []
j = 3
for i in range(4):
    blankt.append(Label(root, text="        ",fg="red",bg="#344e5c"))
    blankt[i].grid(row = 1, column=j)
    j += 2

#Notes Labels
Phy_button = Button(root,text="EPHY",padx=25.5,pady=10,fg="red",bg="#344e5c",borderwidth=0)
CSE_button = Button(root,text="ECSE",padx=27,pady=10,fg="red",bg="#344e5c",borderwidth=0)
EECE_button = Button(root,text="EECE",padx=27,pady=10,fg="red",bg="#344e5c",borderwidth=0)
EMAT_button = Button(root,text="EMAT",padx=25,pady=10,fg="red",bg="#344e5c",borderwidth=0)

#Blank space ?
blank = []
j = 2
for i in range(4):
    blank.append(Label(root, text="",fg="red",bg="#344e5c"))
    blank[i].grid(row = j, column=1)
    j += 2

#Pack Notes
Phy_button.grid(row = 3, column = 1)
CSE_button.grid(row = 5, column = 1)
EECE_button.grid(row = 7, column = 1)
EMAT_button.grid(row = 9, column = 1)

#search box

#search=Entry(root,width=50,bg="red",fg="red",borderwidth=35)
#search.insert(0,"Search Stuff Here")
#search_button = Button(root,text="Click here to search",padx=10,pady=5,fg="red",bg="red",command= clickme)
#search.grid(row=4,column=0)
#search_button.grid(row=5,column=0)

root.mainloop()
