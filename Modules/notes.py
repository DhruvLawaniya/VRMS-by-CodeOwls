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

def phy():
    Phy_frame = LabelFrame(root, text = "Physics", padx=10,pady=10,bg="#344e5c",width=200,height=200)
    Phy_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.ico"),width=10, height =50)
    phynotes=Button(Phy_frame,text="Physics Lectures", image = pdf_logo, compound="top",padx=50)
    phynotes.grid(row=0,column=5,padx=10,columnspan=5)
    phynotes.image=pdf_logo

    phytutorials=Button(Phy_frame,text="Physics Lectures", image = pdf_logo, compound="top",padx=50)
    phytutorials.grid(row=0,column=10,padx=10,columnspan=5)
    phytutorials.image=pdf_logo 
    return 0    

def cse():
    return 0

def eece():
    return 0

def math():
    return 0

root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#344e5c")
#root.iconbitmap("H:\Mid Sem Project\icon.ico")
root.geometry("1280x600")
    
#Basic Label
mainlabel1 = Label(root,pady=0,bg="#344e5c")
mainlabel2 = Label(root, text="",fg="red",bg="#344e5c")
booksnotes = Button(root,text="Books",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0, command=books)
videosnotes = Button(root,text="Videos",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=videos)
gamesnotes = Button(root,text="Games",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=games)
notesnotes = Button(root,text="Notes",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command= notes)
calculatornotes = Button(root,text="Calculator",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command= calculator)

#pack in grid
mainlabel1.grid(row=0,column =0)
mainlabel2.grid(row=1,column=0)
booksnotes.grid(row=1,column=2)
videosnotes.grid(row=1,column=4)
gamesnotes.grid(row=1,column=6)
notesnotes.grid(row=1,column=8)
calculatornotes.grid(row=1,column=10)

#
blankt = []
j = 3
for i in range(4):
    blankt.append(Label(root, text="        ",fg="red",bg="#344e5c"))
    blankt[i].grid(row = 1, column=j)
    j += 2

#Notes Labels
Phynotes = Button(root,text="EPHY",padx=25.5,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=phy)
CSEnotes = Button(root,text="ECSE",padx=27,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=cse)
EECEnotes = Button(root,text="EECE",padx=27,pady=10,fg="red",bg="#344e5c",borderwidth=0,command = eece)
EMATnotes = Button(root,text="EMAT",padx=25,pady=10,fg="red",bg="#344e5c",borderwidth=0,command = math)

#Blank space ?
blank = []
j = 2
for i in range(4):
    blank.append(Label(root, text="",fg="red",bg="#344e5c"))
    blank[i].grid(row = j, column=1)
    j += 2

#Pack Notes
Phynotes.grid(row = 3, column = 1)
CSEnotes.grid(row = 5, column = 1)
EECEnotes.grid(row = 7, column = 1)
EMATnotes.grid(row = 9, column = 1)

#search box

#search=Entry(root,width=50,bg="red",fg="red",borderwidth=35)
#search.insert(0,"Search Stuff Here")
#searchnotes = Button(root,text="Click here to search",padx=10,pady=5,fg="red",bg="red",command= clickme)
#search.grid(row=4,column=0)
#searchnotes.grid(row=5,column=0)

root.mainloop()
