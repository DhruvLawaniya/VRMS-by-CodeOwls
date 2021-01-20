from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Learning Management System By Code Owls")
root.iconbitmap("H:\Mid Sem Project\icon.ico")
def buttoncommand() :
    buttonLabel=Label(root,text="Sup I am a stupid calculator")
    buttonLabel.grid(row=3,column=0)
   
def clickme() :
    search_button=Label(root,text=search.get(),fg="blue")
    search_button.grid(row=6,column=0)
    
#Basic Label
mainlabel1 = Label(root,text="   College Assistant")
mainlabel2 = Label(root, text="By CodeOwls")
calcu_button = Button(root,text="Calculator",padx=50,pady=50,fg="blue",bg="red",command= buttoncommand)
#pack in grid
mainlabel1.grid(row=0,column =0)
mainlabel2.grid(row=1,column=0)
calcu_button.grid(row=2,column=0)
#search box

search=Entry(root,width=50,bg="red",fg="blue",borderwidth=35)
search.insert(0,"Search Stuff Here")
search_button = Button(root,text="Click here to search",padx=10,pady=5,fg="blue",bg="red",command= clickme)
search.grid(row=4,column=0)
search_button.grid(row=5,column=0)

root.mainloop()