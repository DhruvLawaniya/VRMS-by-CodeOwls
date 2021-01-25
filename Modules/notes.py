from tkinter import *
from PIL import ImageTk,Image
import calculator as calc
import links


root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#344e5c")
#root.iconbitmap("H:\Mid Sem Project\icon.ico")
root.geometry("700x400")
    
def books() :
    return 0

def videos() :
    return 0

def calculator() :
    calc.call()

def games() :
    return 0

def note() :
    mainloop()
    return 0

#icons
pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
nb=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)

#subject functions
def phy():
    def phynote():
        links.phynote()
    
    def phytut():
        links.phytut()

    Phy_frame = LabelFrame(root, text = "Physics", padx=10,pady=10,bg="#344e5c",width=200,height=200)
    Phy_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

    phynotes=Button(Phy_frame,text="Physics Notes", image = nb, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=phynote)
    phynotes.grid(row=0,column=5,padx=10,columnspan=5)
    phynotes.image=nb

    phytutorials=Button(Phy_frame,text="Physics Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=phytut)
    phytutorials.grid(row=0,column=10,padx=10,columnspan=5)
    phytutorials.image=pdf_logo 
    return 0

def cse():
    #links
    def csenote():
        links.csenote()
    
    def csetut():
        links.csetut()
    
    CSE_frame = LabelFrame(root, text = "Computer", padx=10,pady=10,bg="#344e5c",width=200,height=200)
    CSE_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

    CSEnotes=Button(CSE_frame, text="Computer Notes", image = nb, compound="top",padx=50, bg="#344e5c", borderwidth=0,command=csenote)
    CSEnotes.grid(row=0,column=5,padx=10,columnspan=5)
    CSEnotes.image=nb

    CSEtutorials=Button(CSE_frame,text="Computer Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=csetut)
    CSEtutorials.grid(row=0,column=10,padx=10,columnspan=5)
    CSEtutorials.image=pdf_logo
    return 0

def eece():
    def eecenote():
        links.eecenote()
    
    def eecetut():
        links.eecetut()

    eece_frame = LabelFrame(root, text = "EECE", padx=10,pady=10,bg="#344e5c",width=200,height=200)
    eece_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

    eecenotes=Button(eece_frame,text="EECE Notes", image = nb, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=eecenote)
    eecenotes.grid(row=0,column=5,padx=10,columnspan=5)
    eecenotes.image=nb

    eecetutorials=Button(eece_frame,text="EECE Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=eecetut)
    eecetutorials.grid(row=0,column=10,padx=10,columnspan=5)
    eecetutorials.image=pdf_logo
    return 0

def math():
    def mathnote():
        links.mathnote()
    
    def mathtut():
        links.mathtut()

    mat_frame = LabelFrame(root, text = "Mathematics", padx=10,pady=10,bg="#344e5c",width=200,height=200)
    mat_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

    matnotes=Button(mat_frame,text="Math Notes", image = nb, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=mathnote)
    matnotes.grid(row=0,column=5,padx=10,columnspan=5)
    matnotes.image=nb

    mattutorials=Button(mat_frame,text="Math Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=mathtut)
    mattutorials.grid(row=0,column=10,padx=10,columnspan=5)
    mattutorials.image=pdf_logo
    

    return 0

#Basic Label
mainlabel1 = Label(root,pady=0,bg="#344e5c")
mainlabel2 = Label(root, text="",fg="red",bg="#344e5c")
booksnotes = Button(root,text="Books",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0, command=books)
videosnotes = Button(root,text="Videos",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=videos)
gamesnotes = Button(root,text="Games",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command=games)
notesnotes = Button(root,text="Notes",padx=10,pady=10,fg="red",bg="#344e5c",borderwidth=0,command= note)
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
