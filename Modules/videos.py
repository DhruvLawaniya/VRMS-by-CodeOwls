from tkinter import *
from PIL import ImageTk,Image
import webbrowser

root = Tk()
root.title("Learning Management System By Code Owls")
root.geometry("1280x600")

def phy_playlist():
    webbrowser.open("https://www.youtube.com/playlist?list=PLygAjP_YxBHt_UujAIJW1KxW4qWDpWS5U")
def ece_playlist():
    webbrowser.open("https://www.youtube.com/playlist?list=PLygAjP_YxBHuwloF5QEiJqnq_o5zQMPZo")
def cse_playlist():
    webbrowser.open("https://www.youtube.com/playlist?list=PLygAjP_YxBHu79djZc_rtMDA1YiAPeBSQ")


def videos() :
    yt_logo=ImageTk.PhotoImage(Image.open (r"images\youtube logo.ico"))

    phy_button=Button(text="Physics Lectures", image=yt_logo, compound="top",padx=50,command=phy_playlist)
    phy_button.grid(row=1,column=1)
    phy_button.image=yt_logo
    ece_button=Button(text="Electrical Lectures", image=yt_logo, compound="top",padx=46,command=ece_playlist)
    ece_button.grid(row=2,column=1)
    ece_button.image=yt_logo
    cse_button=Button(text="Computer Science Lectures", image=yt_logo, compound="top",padx=21,command=cse_playlist)
    cse_button.grid(row=3,column=1)
    cse_button.image=yt_logo

videos_button = Button(root,text="Videos",padx=10,pady=10,fg="blue",bg="#ffffff",command=videos)
videos_button.grid(row=0,column=0)

root.mainloop()