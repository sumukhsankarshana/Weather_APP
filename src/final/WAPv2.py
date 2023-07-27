#Importing necessary Modules
from tkinter import *
import requests
from PIL import ImageTk, Image
import json
from time import strftime

#Window creation 
root = Tk()
root.title("Weather App")
root.geometry("1280x851")
root['background'] = "white"

#Bg Image
new = ImageTk.PhotoImage(Image.open('HomeScreen.jpeg'))
background_label = Label(root, image=new)
background_label.pack()
top_frame=Frame(background_label, bg='lightblue', bd=3)
top_frame.place(relx=0,rely=0,relwidth=0.125,relheight=0.1)

#Display Time And date
def my_time():
    time_string =strftime('%I:%M:%S %p \n %A \n %x') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 	
my_font=('Courier',15,'bold') # display size and style
l1=Label(top_frame,font=my_font,fg='black',bg='lightblue')
l1.grid(row=0,column=0)

#Title Placement 
top_center=Frame(background_label, bg='White', bd=3)
top_center.place(relx=0.5,rely=0,relwidth=0.169,relheight=0.05)
l2=Label(top_center,font=my_font,fg='black',bg='white',text=' Weather Forcast ')
l2.grid(row=0,column=0)

#Creation of Search Frame
frame = Frame(root, bg='lightblue', bd=3)
frame.place(relx=0.088, rely=0.25, relwidth=0.50, relheight=0.050)

#Input Box
Input=Entry(frame,font=22,text=' Enter City Name: ',fg='black')
Input.place(relwidth=0.65, relheight=1)

#API Information 
def city_name():
    #API call
    api_key='1b9c647259ef525641cdabeca42ba135'
    api_request=requests.get(("https://api.openweathermap.org/data/2.5/weather?q="
							+ Input.get() + "&units=metric&appid="+api_key))
    api = json.loads(api_request.content)
    d= api['weather']
    desc=d[0]['description']
    icon=d[0]['icon']
    id=d[0]['id']
    
    # Temperatures
    t=api['main']
    cur_temp=t['temp']
    t_min=t['temp_min']
    t_max=t['temp_max']
    hum=t['humidity']  
    
    #Country
    ss=api['sys']
    country=ss['country']
    
    #City
    citi=api['name']    
    
    #Changing Background Pic
    if(id==800):
            new1 = ImageTk.PhotoImage(Image.open('ClearSky.jpeg'))
    elif(id>=801 and id<=804):
            new1 = ImageTk.PhotoImage(Image.open('Cloudy.jpeg'))
    elif(id>=300 and id<=321) or (id>=500 and id<=531):
            new1 = ImageTk.PhotoImage(Image.open('Rain.jpeg'))
    elif(id>=200 and id<=232):
            new1 = ImageTk.PhotoImage(Image.open('Thunder.jpeg'))
    elif(id>=600 and id<=622):
            new1 = ImageTk.PhotoImage(Image.open('snow.jpeg'))
    elif(id>=701 and id<=781):
            new1 = ImageTk.PhotoImage(Image.open('Mist.jpeg'))
    else:
        new1 = new   
    
    # Adding the received info into the screen
    C_temp.configure(text=cur_temp)
    lable_humidity.configure(text=hum)
    max_temp.configure(text=t_max)
    min_temp.configure(text=t_min)
    lable_country.configure(text=country)
    lable_citi.configure(text=citi)
    label_Desc.configure(text=desc)
    background_label.configure(image=new1)
    open_image(icon)
 
#Function for Icon
def open_image(icon):
    size = int(lower_frame.winfo_height()*0.50)
    img = ImageTk.PhotoImage(Image.open('./icons/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img  
    weather_icon.configure(image=img) 

#Search Button
button = Button(frame, text=" Search ", font=22, command=city_name)
button.place(relx=0.69, relheight=1, relwidth=0.3)

# Lower frame
lower_frame = Frame(root,bd=10,bg='#abdbe3')
lower_frame.place(relx=0.088, rely=0.3, relwidth=0.50, relheight=0.4)

# Country and other detauls
lable_citi = Label(lower_frame, text="", width=0,bg='lightblue', font=("Courier", 17, "bold"))
lable_citi.pack(side='top')
lable_country = Label(lower_frame, text="", width=0,bg='lightblue', font=("Courier", 17, "bold"))
lable_country.pack(side='top',pady=5)

#Temperature and other details
lable_temp = Label(lower_frame, text="Temperature :", width=0, bg='lightblue',font=("Courier",15,'bold'), fg='black')
lable_temp.place(x=0,y=85)

C_temp = Label(lower_frame, text="", width=0, bg='lightblue',font=("Courier", 15), fg='black')
C_temp.place(x=169,y=85)

maxi = Label(lower_frame, text="Max. Temp   : ", width=0,bg='lightblue', font=("Courier", 15,'bold'))
maxi.place(x=0, y=140)

max_temp = Label(lower_frame, text="", width=0,bg='lightblue', font=("Courier", 15))
max_temp.place(x=169, y=140)

mini = Label(lower_frame, text="Min. Temp   : ", width=0,bg='lightblue', font=("Courier", 15, "bold"))
mini.place(x=0, y=195)

min_temp = Label(lower_frame, text="", width=0,bg='lightblue', font=("Courier", 15))
min_temp.place(x=169, y=195)

humi = Label(lower_frame, text="Humidity    : ", width=0,bg='lightblue', font=("Courier", 15, "bold"))
humi.place(x=0, y=250)

lable_humidity = Label(lower_frame, text="", width=0,bg='lightblue', font=("Courier", 15))
lable_humidity.place(x=169, y=250)

weather_icon = Canvas(lower_frame, bg='lightblue', bd=0, highlightthickness=0)
weather_icon.place(relx=.59, rely=0.25, relwidth=0.40, relheight=0.50)

label_Desc=Label(lower_frame, text="", width=0,bg='lightblue', font=("Courier", 14, "bold"))
label_Desc.place(relx=0.63,rely=0.75)

#Funtion Call for current Time and date
my_time()
 
#main Command
root.mainloop()
 