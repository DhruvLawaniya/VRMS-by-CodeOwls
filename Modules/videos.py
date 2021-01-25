from tkinter import *
from PIL import ImageTk,Image
import webbrowser

root = Tk()
root.title("Learning Management System By Code Owls")
root.geometry("1280x600")

def openweb():
    webbrowser.open("https://drive.google.com/file/d/15_PaSoLMEi5GqQrCbvNnZggnDyNEyo-5/view?usp=sharing",new=1)

def videos() :
    img=ImageTk.PhotoImage(Image.open (r"D:\\Uni\Semester 1\ECSE105L\Project\SemProject\Code-Owls-First-Sem-Project\Modules\Images\h.jpg"))
    lab=Button(text="bruh",image=img, compound="top")
    lab.grid(row=5,column=0)
    lab.image=img

mainlabel1 = Label(root,pady=0,bg="#344e5c")
mainlabel2 = Label(root, text="",fg="blue",bg="#344e5c")
videos_button = Button(root,text="Videos",padx=10,pady=10,fg="blue",bg="#ffffff",command=videos)

#pack in grid
videos_button.grid(row=1,column=1)

root.mainloop()


#EPHY105L : https://www.youtube.com/playlist?list=PLygAjP_YxBHt_UujAIJW1KxW4qWDpWS5U
#EHSS103L : https://www.youtube.com/playlist?list=PLygAjP_YxBHtiT_CwZ4KD4yIR5xVsBfWg
#EMAT101L : https://www.youtube.com/playlist?list=PLygAjP_YxBHv7BhIK0hj2mA7v-zdnlp3d
#ECSE105L : https://www.youtube.com/playlist?list=PLygAjP_YxBHu79djZc_rtMDA1YiAPeBSQ
#EECE105L : https://www.youtube.com/playlist?list=PLygAjP_YxBHuwloF5QEiJqnq_o5zQMPZo