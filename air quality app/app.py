from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root=Tk()
root.title('Weather app')
root.geometry("600x100")


def zipplookup():
   #zipp.get()
    #zipplabel=Label(root, text=zipp.get())
    #zipplabel.grid(row=1,column=0, columnspan=2)
    try:
        api_request= requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipp.get()+"&distance=5&API_KEY=EE407C24-889D-4511-8804-DF483F0A4786")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']

        #if and else statement
        if category == "Good":
            weather_color= "#0C0"
        elif category == "Moderate":
            weather_color= "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color= "#ff9900"
        elif category == "Unhealthy":
            weather_color= "#FF0000"
        elif category == "Very Unhealthy":
            weather_color= "#990066"
        elif category == "Hazardous":
            weather_color= "#660000"
        
        root.configure(background=weather_color)

        #labeling
        mylabel= Label(root,text=city + " Air quality value is : " + str(quality)+ " " +" which is "+ category, font=("Helvetica",20),background=weather_color)
        mylabel.grid(row=1,column=0, columnspan=2)
    except Exception as e:
        api= "Error...."


zipp=Entry(root)
zipp.grid(row=0,column=0,stick=W+E+N+S)

zippButton=Button(root, text="Zip code here", command=zipplookup)
zippButton.grid(row=0,column=1,stick=W+E+N+S)





root.mainloop()