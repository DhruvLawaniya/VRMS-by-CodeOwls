from tkinter import *
from PIL import ImageTk,Image
import webbrowser

root = Tk()
root.title("Learning Management System By Code Owls")
root.geometry("1280x600")

def phy_playlist():
    webbrowser.open("https://www.youtube.com/playlist?list=PLygAjP_YxBHt_UujAIJW1KxW4qWDpWS5U",new=1)



def videos() :
    yt_logo=ImageTk.PhotoImage(Image.open (r"images\youtube logo.ico"))

    phy_button=Button(text="Physics Lectures", image=yt_logo, compound="top",padx=50,command=phy_playlist)
    phy_button.grid(row=5,column=5)
    phy_button.image=yt_logo

videos_button = Button(root,text="Videos",padx=10,pady=10,fg="blue",bg="#ffffff",command=videos)
videos_button.grid(row=1,column=1)

root.mainloop()



#EHSS103L : https://www.youtube.com/playlist?list=PLygAjP_YxBHtiT_CwZ4KD4yIR5xVsBfWg
#EMAT101L : https://www.youtube.com/playlist?list=PLygAjP_YxBHv7BhIK0hj2mA7v-zdnlp3d
#ECSE105L : https://www.youtube.com/playlist?list=PLygAjP_YxBHu79djZc_rtMDA1YiAPeBSQ
#EECE105L : https://www.youtube.com/playlist?list=PLygAjP_YxBHuwloF5QEiJqnq_o5zQMPZo