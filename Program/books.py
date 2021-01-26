from tkinter import *
from PIL import ImageTk,Image
import webbrowser
   
def books(root) :  
    def ecepush():
       BFrame_Right = LabelFrame(root, padx=10,pady=10,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)  
       #list ece books and setup their info here itself
    def phypush():
       BFrame_Right = LabelFrame(root, padx=10,pady=10,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)
    def mathpush():
       BFrame_Right = LabelFrame(root, padx=10,pady=10,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)
    def csepush():
       BFrame_Right = LabelFrame(root, padx=10,pady=10,bg="#344e5c",width=200,height=200)
       BFrame_Right.grid(row=2,column=1)
        
    BFrame_left = LabelFrame(root, padx=10,pady=10,bg="#344e5c",width=200,height=200)
    #my button definitions
    ecebutton=Button(BFrame_left,text="Ece ",command=ecepush)
    phybutton=Button(BFrame_left,text="Phy ")
    mathbutton=Button(BFrame_left,text="Maths ")
    csebutton=Button(BFrame_left,text="CSE ")
    
    #my button grids
    BFrame_left.grid(row=2,column=0)
    ecebutton.grid(row=0,column=0)
    phybutton.grid(row=1,column=0)
    mathbutton.grid(row=2,column=0)
    csebutton.grid(row=3,column=0)
    