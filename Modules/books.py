from tkinter import *
from PIL import ImageTk,Image
import webbrowser


   
def books(root) :  
    def ecepush():
       #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       def openwebbook2():
         webbrowser.open(urlbook2,new)
       new=1
       BFrame_Right = LabelFrame(root,columnspan = 10,rowspan = 15, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=3,column=2)  
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/1BfJUZc6QZmCjBllSsvdWYu3kMHJLJuFj/view?usp=sharing"
       
       urlbook2 = "https://drive.google.com/file/d/1-ozF-lwUS24ZTM3on2FfrJh6uYtiw6ml/view?usp=sharing"
       urlbook3 = "https://drive.google.com/file/d/1-ozF-lwUS24ZTM3on2FfrJh6uYtiw6ml/view?usp=sharing"
       book1= Button(BFrame_Right,text="Introductory Circuit Analysis",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       book2= Button(BFrame_Right,text="Electronic Devices And Circuits",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook2)
       book2.grid(row=4,column=3)
       BFrame_Right.lift()


    def phypush():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       def openwebbook2():
         webbrowser.open(urlbook2,new)
       new=1
       BFrame_Right = LabelFrame(root,columnspan = 10,rowspan = 15, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=3,column=2)  
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/1aMedhLqIBva1qXTFq4K26mvkZw6ZB3Z-/view?usp=sharing"
       
       urlbook2 = "https://drive.google.com/file/d/19AyL4xv-tcStsmWU0HBeANqT2IWdaU9D/view?usp=sharing"
       urlbook3 = "https://drive.google.com/file/d/1-ozF-lwUS24ZTM3on2FfrJh6uYtiw6ml/view?usp=sharing"
       book1= Button(BFrame_Right,text="Griffith's Into Electrodynamics",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       book2= Button(BFrame_Right,text="Instructors Solution Manual",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook2)
       book2.grid(row=4,column=3)
       BFrame_Right.lift()
    def mathpush():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       def openwebbook2():
         webbrowser.open(urlbook2,new)
       def openwebbook3():
         webbrowser.open(urlbook3,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=3,column=2)  
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/1lQOd54h6lS-1uRBSLFh_f3wIrpjDetu2/view?usp=sharing"
       
       urlbook2 = "https://drive.google.com/file/d/1F_8YCTVB3f-7I3GwcXE4QasZ5VgX8Xc8/view?usp=sharing"
       urlbook3 = "https://drive.google.com/file/d/1LtY4BpQq5aBU5q_WjTZoNYEItrzeJdKu/view?usp=sharing"
       book1= Button(BFrame_Right,text="Introduction To Real Analysis",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       book2= Button(BFrame_Right,text="Ross Elementary Analysis",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook2)
       book2.grid(row=4,column=3)
       book3= Button(BFrame_Right,text="Thomas Calculus",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook3)
       book3.grid(row=4,column=4)
       BFrame_Right.lift()

    def csepush():
        #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       def openwebbook2():
         webbrowser.open(urlbook2,new)
       def openwebbook3():
         webbrowser.open(urlbook3,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=3,column=2)  
       #list ece books and setup their info here itself
       urlbook1 = "https://drive.google.com/file/d/16WnwpmYBC5ULP5JvprACY6l7u09O9PxX/view?usp=sharing"
       
       urlbook2 = "https://drive.google.com/file/d/1ERSe-zEJxj1kut8xN-YgoKC4ZJmGanxs/view?usp=sharing"
       urlbook3 = "https://drive.google.com/file/d/1haFTD3ptgYbH25ZkgNH9A_BIUFkoi-V6/view?usp=sharing"
       book1= Button(BFrame_Right,text="Introduction To Computer \nScience Using Python",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook1)
       book1.grid(row=4,column=2)
       book2= Button(BFrame_Right,text="Think CS Python",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook2)
       book2.grid(row=4,column=3)
       book3= Button(BFrame_Right,text="Think Python",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openwebbook3)
       book3.grid(row=4,column=4)
       BFrame_Right.lift()

    img = ImageTk.PhotoImage(Image.open(r"images\pdf.png"),height=50,width=50)    
    BFrame_left = LabelFrame(root, padx=10,pady=10,bg="#344e5c",width=200,height=200)
    #my button definitions
    ecebutton=Button(BFrame_left,text="Ece ",command=ecepush)
    phybutton=Button(BFrame_left,text="Phy ",command=phypush)
    mathbutton=Button(BFrame_left,text="Maths ",command=mathpush)
    csebutton=Button(BFrame_left,text="CSE ",command=csepush)
    
    #my button grids
    BFrame_left.grid(row=3,column=0)
    ecebutton.grid(row=0,column=0)
    phybutton.grid(row=1,column=0)
    mathbutton.grid(row=2,column=0)
    csebutton.grid(row=3,column=0)
   
#books_button = Button(root,text="Books",padx=10,pady=10,fg="blue",bg="#ffffff",command=books)

#pack in grid
#books_button.grid(row=0,column=0)

#root.mainloop()
