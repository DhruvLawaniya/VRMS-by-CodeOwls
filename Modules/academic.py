from tkinter import *
from PIL import ImageTk,Image
import webbrowser

   
def academic(root) :  
    def timetable():
       #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5) 
       #list ece books and setup their info here itself
       urlbook1 = "https://icampus.bennett.edu.in/#/home/v1/stimetable"
       book1= Button(BFrame_Right,text="TimeTable",compound="top",image=img2,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       BFrame_Right.lift()


    def marks():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)
       #list ece books and setup their info here itself
       urlbook1 = "https://icampus.bennett.edu.in/#/home/wm/sstudentmarks"
       book1= Button(BFrame_Right,text="Marks",compound="top",image=img2,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       BFrame_Right.lift()

    def fees():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)  
       #list ece books and setup their info here itself
       urlbook1 = "https://icampus.bennett.edu.in/#/home/v3/feepayment"
       book1= Button(BFrame_Right,text="Fees Payment",compound="top",image=img2,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       BFrame_Right.lift()

    def cirriculum():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=80,pady=75,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row = 3, column = 2,columnspan = 10,rowspan = 15, padx=5,pady=5)  
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/1cXpD9mr00kRyqUYqnb-mqBdw5tvvU5CP/view"
       book1= Button(BFrame_Right,text="CURRICULAM FOR BTECH CSE PROGRAM: 2020-24",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)

    img = ImageTk.PhotoImage(Image.open(r"images\pdf.png"),height=50,width=50)    
    BFrame_left = LabelFrame(root,bg="#1d2125",pady=28,borderwidth=0)
    
    img2 = ImageTk.PhotoImage(Image.open(r"images\chrome.png"),height=50,width=50)
    #my button definitions
    timetablebutton=Button(BFrame_left,text="Time-Table",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=0,command=timetable)
    marksbutton=Button(BFrame_left,text="Marks",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=0,command=marks)
    feesbutton=Button(BFrame_left,text="Fees Payment",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=0,command=fees)
    cirriculumbutton=Button(BFrame_left,text="Curriculum",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=0,command=cirriculum)

    #my button grids
    BFrame_left.grid(row = 3, column = 0,rowspan=10,padx=10)
    timetablebutton.grid(row=0,column=1)
    marksbutton.grid(row=2,column=1)
    feesbutton.grid(row=4,column=1)
    cirriculumbutton.grid(row=6,column=1)

    blank = []
    j = 1
    for i in range(4):
        blank.append(Label(BFrame_left, text=" Trying to make it long ",fg="#1d2125",bg="#1d2125"))
        blank[i].grid(row = j, column=1)
        j += 2
    
    BFrame_left.lift()