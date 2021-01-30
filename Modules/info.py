from tkinter import *
import webbrowser
import requests 
import json 
import datetime 

def weather(Main):
    # Dates 
    dt = datetime.datetime.now() 
    date = Label(Main, text=dt.strftime('%A--'), bg='white', font=("bold", 15)) 
    date.place(x=5, y=130) 
    month = Label(Main, text=dt.strftime('%m %B'), bg='white', font=("bold", 15)) 
    month.place(x=100, y=130) 
    
    # Time 
    hour = Label(Main, text=dt.strftime('%I:%M %p'),bg='white', font=("bold", 15)) 
    hour.place(x=10, y=160) 
    
    # City Search 
    city_name = StringVar() 
    city_entry = Entry(Main, textvariable=city_name, width=45) 
    city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S) 
    
    
    def city_name(): 
    
        # API Call 
        api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city_entry.get() + "&units=metric&appid="+"45cf08acb49a2f6aaa93254d8c277028") 
    
        api = json.loads(api_request.content) 
    
        # Temperatures 
        y = api['main'] 
        current_temprature = y['temp'] 
        humidity = y['humidity'] 
        tempmin = y['temp_min'] 
        tempmax = y['temp_max'] 
    
        # Coordinates 
        x = api['coord'] 
        longtitude = x['lon'] 
        latitude = x['lat'] 
    
        # Country 
        z = api['sys'] 
        country = z['country'] 
        citi = api['name'] 
    
        # Adding the received info into the screen 
        lable_temp.configure(text=current_temprature) 
        lable_humidity.configure(text=humidity) 
        max_temp.configure(text=tempmax) 
        min_temp.configure(text=tempmin)  
        lable_country.configure(text=country) 
        lable_citi.configure(text=citi) 
    
    
    # Search Bar and Button 
    city_nameButton = Button(Main, text="Search", command=city_name) 
    city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S) 
    
    
    # Country  Names and Coordinates 
    lable_citi = Label(Main, text="...", width=0,bg='white', font=("bold", 15)) 
    lable_citi.place(x=10, y=63) 
    
    lable_country = Label(Main, text="...", width=0,bg='white', font=("bold", 15)) 
    lable_country.place(x=135, y=63) 
    
    # Current Temperature 
    
    lable_temp = Label(Main, text="...", width=0, bg='white',font=("Helvetica", 110), fg='black') 
    lable_temp.place(x=18, y=220) 
    
    # Other temperature details 
    
    humi = Label(Main, text="Humidity: ", width=0,bg='white', font=("bold", 15)) 
    humi.place(x=3, y=400) 
    
    lable_humidity = Label(Main, text="...", width=0,bg='white', font=("bold", 15)) 
    lable_humidity.place(x=107, y=400) 
    
    
    maxi = Label(Main, text="Max. Temp.: ", width=0,bg='white', font=("bold", 15)) 
    maxi.place(x=3, y=430) 
    
    max_temp = Label(Main, text="...", width=0, bg='white', font=("bold", 15)) 
    max_temp.place(x=128, y=430) 
    
    
    mini = Label(Main, text="Min. Temp.: ", width=0,    bg='white', font=("bold", 15)) 
    mini.place(x=3, y=460) 
    
    min_temp = Label(Main, text="...", width=0,bg='white', font=("bold", 15)) 
    min_temp.place(x=128, y=460)
    
    return 0