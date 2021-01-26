from tkinter import *
from PIL import ImageTk,Image
import webbrowser
root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#344e5c")

root.geometry("1920x1080")

   
def books() :  
    def ecepush():
       #functions
       def openwebbook1():
         webbrowser.open(urlbook1,new)
       def openwebbook2():
         webbrowser.open(urlbook2,new)
       new=1
       BFrame_Right = LabelFrame(root, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)  
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
       BFrame_Right = LabelFrame(root, padx=100,pady=100,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)  
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
       BFrame_Right.grid(row=2,column=1)  
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
       BFrame_Right.grid(row=2,column=1)  
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
    BFrame_left.grid(row=2,column=0)
    ecebutton.grid(row=0,column=0)
    phybutton.grid(row=1,column=0)
    mathbutton.grid(row=2,column=0)
    csebutton.grid(row=3,column=0)
   

    















    #functions :
    #def openweb():
    #    webbrowser.open("https://drive.google.com/file/d/1-ozF-lwUS24ZTM3on2FfrJh6uYtiw6ml/view?usp=sharing",new=1)
    #alon's code
    #def phy():
    #def phynote():
     #   return 0
    
    #def phytut():
#        return 0
#
 #   Phy_frame = LabelFrame(root, text = "Physics", padx=10,pady=10,bg="#344e5c",width=200,height=200)
  #  Phy_frame.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

   # phynotes=Button(Phy_frame,text="Physics Notes",  compound="top",padx=50,bg="#344e5c",borderwidth=0,command=phynote)
    #phynotes.grid(row=0,column=5,padx=10,columnspan=5)
    #phynotes.image=nb

    #phytutorials=Button(Phy_frame,text="Physics Tutorials", image = pdf_logo, compound="top",padx=50,bg="#344e5c",borderwidth=0,command=phytut)
    #phytutorials.grid(row=0,column=10,padx=10,columnspan=5)
    #phytutorials.image=pdf_logo 
 
    #images
    #img = ImageTk.PhotoImage(Image.open(r"images\pdf.png"),height=50,width=50)
        
    #url
    #url = "https://drive.google.com/file/d/1-ozF-lwUS24ZTM3on2FfrJh6uYtiw6ml/view?usp=sharing"
    #new = 1

    #define frame
        
    #define buttons
    #book1= Button(Phy_frame,text="Griffith's Into Electrodynamics",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #book2= Button(Phy_frame,text="Instructors solution manual",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #book3= Button(root,text="Intro to Real Analysis",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #book4= Button(root,text="hello",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #book5= Button(root,text="hello",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #book6= Button(root,text="hello",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #book7= Button(root,text="hello",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #book8= Button(root,text="hello",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #book9= Button(root,text="hello",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #book10= Button(root,text="hello",compound="top",image=img,bg="#344e5c",borderwidth=0,command=openweb)
    #pack in grid
    #book1.grid(row=4,column=2)
    #book2.grid(row=4,column=3)
    #book3.grid(row=4,column=4)
    #book4.grid(row=4,column=5)
    #book5.grid(row=4,column=6)
    #book6.grid(row=5,column=2)
    #book7.grid(row=5,column=3)
    #book8.grid(row=5,column=4)
    #book9.grid(row=5,column=5)
    #book10.grid(row=5,column=6)
    
    #assign image
    #book2.image=img
    #book3.image=img
    #book4.image=img
    #book5.image=img
    #book6.image=img
    #book7.image=img
    #book8.image=img
    #book9.image=img
    #book10.image=img

    
#Basic Label
books_button = Button(root,text="Books",padx=10,pady=10,fg="blue",bg="#ffffff",command=books)

#pack in grid
books_button.grid(row=0,column=0)

root.mainloop()
