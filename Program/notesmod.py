from tkinter import *
from PIL import ImageTk,Image
import links

def phys(root):
    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
    nb=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)

    Phyframe = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
    Phyframe.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)

    def phynote():
        links.phynote()
    
    def phytut():
        links.phytut()

    phynotes=Button(Phyframe,text="Physics Notes", image = nb, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=phynote)
    phynotes.grid(row=0,column=5,padx=10,columnspan=5)
    phynotes.image=nb

    phytutorials=Button(Phyframe,text="Physics Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=phytut)
    phytutorials.grid(row=0,column=10,padx=10,columnspan=5)
    phytutorials.image=pdf_logo

    Phyframe.lift()

    return 0

def eece(root):
    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
    nb=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)

    def eecenote():
        links.eecenote()
    
    def eecetut():
        links.eecetut()

    eece_frame = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
    eece_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)
    
    eecenotes=Button(eece_frame,text="EECE Notes", image = nb, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=eecenote)
    eecenotes.grid(row=0,column=5,padx=10,columnspan=5)
    eecenotes.image=nb

    eecetutorials=Button(eece_frame,text="EECE Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=eecetut)
    eecetutorials.grid(row=0,column=10,padx=10,columnspan=5)
    eecetutorials.image=pdf_logo

    eece_frame.lift()
    return 0

def cse(root):
    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
    nb=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)

    def csenote():
        links.csenote()
    
    def csetut():
        links.csetut()

    CSE_frame = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
    CSE_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)
    

    CSEnotes=Button(CSE_frame, text="Computer Notes", image = nb, compound="top",padx=50, bg="#344e5c", borderwidth=0,command=csenote)
    CSEnotes.grid(row=0,column=5,padx=10,columnspan=5)
    CSEnotes.image=nb

    CSEtutorials=Button(CSE_frame,text="Computer Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=csetut)
    CSEtutorials.grid(row=0,column=10,padx=10,columnspan=5)
    CSEtutorials.image=pdf_logo
    return 0

def math(root):
    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
    nb=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)
    
    def mathnote():
        links.mathnote()
    
    def mathtut():
        links.mathtut()

    mat_frame = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
    mat_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)
    matnotes=Button(mat_frame,text="Math Notes", image = nb, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=mathnote)
    matnotes.grid(row=0,column=5,padx=10,columnspan=5)
    matnotes.image=nb

    mattutorials=Button(mat_frame,text="Math Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=mathtut)
    mattutorials.grid(row=0,column=10,padx=10,columnspan=5)
    mattutorials.image=pdf_logo
    

    return 0