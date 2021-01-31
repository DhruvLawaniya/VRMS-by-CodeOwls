from tkinter import *
from tkinter import messagebox as mb
import random
import json

root = Tk()
root.geometry("1000x500")
root.title("Quiz")

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
        t = Label(root, text="Random Practice BS Quiz", width=62, bg="#24292e", fg="white", font=("times", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=100, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
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
        nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=300,y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
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

cseB = Button(root,text = 'CSE',command = cse, padx = 25, bg = 'black', fg = 'white')
cseB.pack()    
phyB = Button(root,text = 'PHY',command = phy, padx = 25, bg = 'black', fg = 'white')
phyB.pack()
eceB = Button(root,text = 'ECE',command = ece, padx = 25, bg = 'black', fg = 'white')
eceB.pack()
matB = Button(root,text = 'MAT',command = mat, padx = 25, bg = 'black', fg = 'white')
matB.pack()

root.mainloop()