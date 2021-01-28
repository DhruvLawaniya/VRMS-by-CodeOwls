from tkinter import *
import requests 
import json
import random
from PIL import ImageTk, Image

root = Tk() 
root.title("Misc") 
root.geometry("1000x500") 
root['background'] = "white"

api_req = requests.get('https://type.fit/api/quotes')
api = json.loads(api_req.content)
b = random.choice(api)

quote = Label(root,text = b['text']).pack()
author = Label(root,text = '-'+b['author']).pack()



root.mainloop()