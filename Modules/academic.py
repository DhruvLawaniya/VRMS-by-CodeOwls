from tkinter import *
from PIL import ImageTk,Image
import webbrowser
root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#344e5c")
root.geometry("1920x1080")

   
def academic() :  
    def timetable():
       #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)  
       #list ece books and setup their info here itself
       urlbook1 = "https://icampus.bennett.edu.in/#/home/v1/stimetable"
       book1= Button(BFrame_Right,text="TimeTable",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       BFrame_Right.lift()


    def marks():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)  
       #list ece books and setup their info here itself
       urlbook1 = "https://icampus.bennett.edu.in/#/home/wm/sstudentmarks"
       book1= Button(BFrame_Right,text="Marks",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       BFrame_Right.lift()

    def fees():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)  
       #list ece books and setup their info here itself
       urlbook1 = "https://icampus.bennett.edu.in/#/home/v3/feepayment"
       book1= Button(BFrame_Right,text="Fees Payment",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       BFrame_Right.lift()

    def cirriculum():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)  
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/1cXpD9mr00kRyqUYqnb-mqBdw5tvvU5CP/view"
       book1= Button(BFrame_Right,text="CURRICULA FOR B.TECH. CSE PROGRAM: 2020-24",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       BFrame_Right.lift()

    img = ImageTk.PhotoImage(Image.open(r"images\pdf.png"),height=50,width=50)    
    BFrame_left = LabelFrame(root, padx=10,pady=10,bg="#344e5c",width=200,height=200)
    #my button definitions
    timetablebutton=Button(BFrame_left,text="Ece ",command=timetable)
    marksbutton=Button(BFrame_left,text="Phy ",command=marks)
    feesbutton=Button(BFrame_left,text="Maths ",command=fees)
    cirriculumbutton=Button(BFrame_left,text="CSE ",command=cirriculum)
    
    #my button grids
    BFrame_left.grid(row=2,column=0)
    ecebutton.grid(row=0,column=0)
    phybutton.grid(row=1,column=0)
    mathbutton.grid(row=2,column=0)
    csebutton.grid(row=3,column=0)