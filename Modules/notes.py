from tkinter import *
from PIL import ImageTk,Image
  
import webbrowser

def csenote():
    webbrowser.open("https://drive.google.com/drive/folders/1WjknjKJ81ajNQZpb7tKUy5ohMxGJWz30")
    return 0

def csetut():
    webbrowser.open("https://drive.google.com/drive/folders/1uNngYCa-L4JyXOwR14lT7Yi0BCMDXiNt")
    return 0

def eecenote():
    webbrowser.open("https://drive.google.com/drive/folders/1YSPKLGk-Q2Ml1Lr3rZIVedcgj65IKp5z")
    return 0

def eecetut():
    webbrowser.open("https://drive.google.com/drive/folders/1O2riFGPlZuxZ8di4nCl5QG2jM46Rwd-D")
    return 0

def mathnote():
    webbrowser.open("https://drive.google.com/drive/folders/1PVM_4r4bBMDs1nzJsQEBVuL--hxHOtvw")
    return 0

def mathtut():
    webbrowser.open("https://drive.google.com/drive/folders/1cwessWTlenOgAD3lClxvP2Bov61FULAO")
    return 0

def phynote():
    webbrowser.open("https://drive.google.com/drive/folders/1Bch6DpcM1T_YesopG06C_RL9Yd-cN_UH")
    return 0

def phytut():
    webbrowser.open("https://drive.google.com/drive/folders/1YO43v74zG0hD2FFtEjusOGOl3thlkOwV")
    return 0

def phys(root):
    pdf_logo=ImageTk.PhotoImage(Image.open (r"images\pdf.png"),width=10, height =50)
    nb=ImageTk.PhotoImage(Image.open (r"images\notebook.png"),width=10, height =50)

    Phyframe = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
    Phyframe.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)


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
    
    

    mat_frame = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
    mat_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)
    matnotes=Button(mat_frame,text="Math Notes", image = nb, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=mathnote)
    matnotes.grid(row=0,column=5,padx=10,columnspan=5)
    matnotes.image=nb

    mattutorials=Button(mat_frame,text="Math Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=mathtut)
    mattutorials.grid(row=0,column=10,padx=10,columnspan=5)
    mattutorials.image=pdf_logo
    

    return 0

def notesmain(root):
    LeftFrame = LabelFrame(root,bg="#24292e",pady=28,borderwidth=0)
    LeftFrame.grid(row = 3, column = 0,rowspan=10,padx=10)

    Phynotes = Button(LeftFrame,text="EPHY",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=lambda:phys(root))
    CSEnotes = Button(LeftFrame,text="ECSE",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command=lambda:cse(root))
    EECEnotes = Button(LeftFrame,text="EECE",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command =lambda:eece(root))
    EMATnotes = Button(LeftFrame,text="EMAT",padx=10,pady=10,fg="white",bg="#24292e",borderwidth=0,command = lambda:math(root))

    Phynotes.grid(row = 0, column = 1)
    CSEnotes.grid(row = 2, column = 1)
    EECEnotes.grid(row = 4, column = 1)
    EMATnotes.grid(row = 6, column = 1)
 
    #blank
    blank = []
    j = 1
    for i in range(4):
        blank.append(Label(LeftFrame, text=" Trying to make it long ",fg="#24292e",bg="#24292e"))
        blank[i].grid(row = j, column=1)
        j += 2

    LeftFrame.lift()