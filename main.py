from tkinter import *
from PIL import ImageTk,Image
import random
import json
from tkinter import messagebox as mb
import Modules.notes as n
import Modules.academic as aca
import Modules.books as b
import Modules.videos as v
import Modules.misc as m

root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#24292e")
root.geometry("900x500")

def home():
    Main.lift()
    MainLeft.lift()
    
def books():
    home()
    b.books(root)

def videos():
    home()
    v.videos(root)

def academic():
    home()
    aca.academic(root)

def quiz():
    dem = Toplevel()
    dem.geometry("1000x500")
    dem.title("Quiz")
    class Quiz():
        def __init__(self):
            self.qn = 0
            self.ques = self.question(self.qn)
            self.opt_selected = IntVar()
            self.opts = self.radiobtns()
            self.display_options(self.qn)
            self.buttons()
            self.correct = 0

        def question(self, qn):
            t = Label(dem, text="Random Practice BS Quiz", width=62, bg="#24292e", fg="white", font=("times", 20, "bold"))
            t.place(x=0, y=2)
            qn = Label(dem, text=q[qn], width=100, font=("times", 16, "bold"), anchor="w")
            qn.place(x=70, y=100)
            return qn

        def radiobtns(self):
            val = 0
            b = []
            yp = 150
            while val < 4:
                btn = Radiobutton(dem, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
                b.append(btn)
                btn.place(x=100, y=yp)
                val += 1
                yp += 40
            return b

        def display_options(self, qn):
            val = 0
            self.opt_selected.set(0)
            self.ques['text'] = q[qn]
            for op in options[qn]:
                self.opts[val]['text'] = op
                val += 1

        def buttons(self):
            nbutton = Button(dem, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
            nbutton.place(x=300,y=380)
            quitbutton = Button(dem, text="Quit", command=dem.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
            quitbutton.place(x=480,y=380)

        def checkans(self, qn):
            if self.opt_selected.get() == a[qn]:
                return True
            
        def nextbtn(self):
            if self.checkans(self.qn):
                self.correct += 1
            self.qn += 1
            if self.qn == len(q):
                self.display_result()
            else:
                self.display_options(self.qn)       
            

        def display_result(self):
            score = int(self.correct / len(q) * 100)
            result = "Score: " + str(score) + "%"
            wc = len(q) - self.correct
            correct = "No. of correct answers: " + str(self.correct)
            wrong = "No. of wrong answers: " + str(wc)
            mb.showinfo("Result", "\n".join([result, correct, wrong]))

    def ece():
        global obj,q,options,a
        phyB.destroy()
        eceB.destroy()
        matB.destroy()
        cseB.destroy()
        with open(r'Modules\ece.json') as f:
            obj = json.load(f)
        q = (obj['ques'])
        options = (obj['options'])
        a = (obj['ans'])
        quiz = Quiz()

    def mat():
        global obj,q,options,a
        phyB.destroy()
        eceB.destroy()
        matB.destroy()
        cseB.destroy()
        with open(r'Modules\mat.json') as f:
            obj = json.load(f)
        q = (obj['ques'])
        options = (obj['options'])
        a = (obj['ans'])
        quiz = Quiz()

    def cse():
        global obj,q,options,a
        phyB.destroy()
        eceB.destroy()
        matB.destroy()
        cseB.destroy()
        yes = random.randint(0,7)
        with open(r'Modules\cse.json') as f:
            obj = json.load(f)
        q = (obj['ques'][yes:yes+3])
        options = (obj['options'][yes:yes+3])
        a = (obj['ans'][yes:yes+3])
        quiz = Quiz()

    def phy():
        global obj,q,options,a
        phyB.destroy()
        eceB.destroy()
        matB.destroy()
        cseB.destroy()
        with open(r'Modules\phy.json') as f:
            obj = json.load(f)
        q = (obj['ques'])
        options = (obj['options'])
        a = (obj['ans'])
        quiz = Quiz()

    cseB = Button(dem,text = 'CSE',command = cse, padx = 25, bg = 'black', fg = 'white')
    cseB.pack()    
    phyB = Button(dem,text = 'PHY',command = phy, padx = 25, bg = 'black', fg = 'white')
    phyB.pack()
    eceB = Button(dem,text = 'ECE',command = ece, padx = 25, bg = 'black', fg = 'white')
    eceB.pack()
    matB = Button(dem,text = 'MAT',command = mat, padx = 25, bg = 'black', fg = 'white')
    matB.pack()

    dem.mainloop()

def misc():
    home()
    m.notesmain(root)

def note():
    home()
    n.notesmain(root)

Top = LabelFrame(root,bg = "#24292e",width=200,height=10,borderwidth=0)
Top.grid(row = 0, column=0,columnspan=7,padx=10,pady=20)

Main = LabelFrame(root, padx=200,pady=20,bg="#1d2125",width=200,height=200)
Main.grid(row = 3, column = 2,columnspan = 10,rowspan = 10, padx=5,pady=5)

MainLeft = LabelFrame(root,bg="#24292e",pady=28,borderwidth=0)
MainLeft.grid(row = 3, column = 0,rowspan=10,padx=10)

logo=ImageTk.PhotoImage(Image.open (r"images\redbull.png"),width=10, height =50)
main = Label(Main,image=logo,borderwidth="0")
main.grid(row=0,column=0)

blank = []
for i in range(12):
    blank.append(Label(MainLeft, text=" Trying to make it long ",fg="#24292e",bg="#24292e"))
    blank[i].grid(row = i, column=1)

#Basic Label

homebutton = Button(Top,text="HOME",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=home)
booksnotes = Button(Top,text="Books",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1, command=books)
videosnotes = Button(Top,text="Videos",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=videos)
miscnotes = Button(Top,text="Misc",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command=misc)
notesnotes = Button(Top,text="Notes",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= note)
quiznotes = Button(Top,text="Practice Quiz",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= quiz)
Academic = Button(Top,text="Academic",padx=10,pady=10,fg="white",bg="#1d2125",borderwidth=1,command= academic)

homebutton.grid(row=0,column=0)
booksnotes.grid(row=0,column=2)
videosnotes.grid(row=0,column=8)
miscnotes.grid(row=0,column=12)
notesnotes.grid(row=0,column=4)
quiznotes.grid(row=0,column=10)
Academic.grid(row=0,column=6)

j=1
blanktop = []
for i in range(6):
    blanktop.append(Label(Top, text=" k k k ",fg="#24292e",bg="#24292e"))
    blanktop[i].grid(row = 0, column=j)
    j+=2

root.mainloop()