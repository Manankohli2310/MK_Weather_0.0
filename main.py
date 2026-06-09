from tkinter import *
import tkinter as tk
from geopy.geocoders import Photon
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


root=Tk()
root.title("MK Weather")
root.geometry('900x500+300+200')
root.resizable(False,False)

root.iconbitmap("logo.ico")




#time
name=Label(root,font=("arial",12,"bold"),fg="#FF914D", text="LAST SYNCED")
name.place(x=20,y=20)
dot1=Label(root,text="...",font=("Helvicta",18,"bold"),fg="#404040")
dot1.place(x=25,y=39)
clock=Label(root,font=("Helvetica",18),fg="#404040")
clock.place(x=20,y=45)


# bottom frame
frame=Frame(root,width=900, height=180, bg="#817FA0")
frame.pack(side=BOTTOM)



# details
details=PhotoImage(file="detail1.png")
l=Label(image=details)
l.place(x=350,y=352)

#date
date = datetime.now()
c=Label(root,text=f"{date:%B %d, %Y}",font=("Georgia", 12),bg="#9faac3")
c.place(x=387, y=388)
date1= datetime.now()
d=Label(root,text=f"{date1:%A}", font=("Georgia",11),bg="#9faac3")
d.place(x=387,y=410)


def getweather():
    city = textfield.get()
   


    geolocator=Photon(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)




    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&cnt=4&appid=ebfd0889b491a935848be72d1cda0bb0&units=metric&exclude=hourly"
    r = requests.get(api).json()

    feels_like = r['main']['feels_like']
    humidity = r['main']['humidity']
    pressure = r['main']['pressure']
    wind = r['wind']['speed']
    description = r['weather'][0]['description']
    temp = r['main']['temp']
    temp_min = r['main']['temp_min']
    temp_max = r['main']['temp_max']
    country = r['sys']['country']



    f.config(text=(feels_like,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,'hPa'))
    w.config(text=(wind,'m/s'))
    d.config(text=(description))
    t.config(text=(temp,"°"))
    tm1.config(text=(temp_min,"°C"))
    tm2.config(text=(temp_max,"°C"))
    cn.config(text=(country))






# Search Box

Search_image=PhotoImage(file="Copy of search.png")
myimage=Label(image=Search_image)
myimage.place(x=290,y=130)

mk=PhotoImage(file="MK (1).png")
MY=Label(image=mk, bg="#404040")
MY.place(x=320, y=145)
textfield=tk.Entry(root,justify="center", width=17, font=("poppins",25,"bold"), bg="#404040", border=0, fg="#d9d9d9")
textfield.place(x=370,y=152)
textfield.focus()

Search_icon=PhotoImage(file="Copy of search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getweather)

myimage_icon.place(x=670,y=143)





# label

my_image=PhotoImage(file="Unt.png")

Label(root, image=my_image, bg="#404040").place(x=40,y=110)
label=Label(root, text="Feels Like :", font=("Helvetica", 10,"bold"), fg="black", bg="#d9d9d9")
label.place(x=49,y=120)

label1=Label(root, text="Humidity :", font=("Helvetica", 10, "bold"), fg="black", bg="#D9D9D9")
label1.place(x=50,y=140)

label2=Label(root, text="Pressure :", font=("Helvetica", 10, "bold"), fg="black", bg="#D9D9D9")
label2.place(x=50,y=160)

label3=Label(root, text="Wind Speed :", font=("Helvetica", 10, "bold"), fg="black", bg="#D9D9D9")
label3.place(x=50,y=180)

label4=Label(root, text="Description :", font=("Helvetica", 10, "bold"), fg="black", bg="#D9D9D9")
label4.place(x=50,y=200)

label10=Label(root,text="Min.Temp :",font=("Georgia",11),bg="#9faac3")
label10.place(x=575,y=372)
label11=Label(root,text="Max.Temp :",font=("Georgia",11),bg="#9faac3")
label11.place(x=575,y=404)
label12=Label(root,text="Country Code :",font=("Georgia",11),bg="#9faac3")
label12.place(x=575,y=432)

# current weather
MAIN4=PhotoImage(file="main frame.png")
label4=Label(image=MAIN4, bg="#e3e8e4", bd=3)
label4.place(x=70, y=350)

label5=Label(root,text="CURRENT WEATHER :", font=("arial", 12,"bold"), fg="#FF914D", bg="#D9D9D9")
label5.place(x=78, y=377)
dot=Label(root, text="...",font=("arial", 18,"bold"),fg="#404040",bg="#D9D9D9")
dot.place(x=145, y=398)


# logo
img=PhotoImage(file="1000011641-removebg-preview.png")
label6=Label(image=img )
label6.place(x=670, y=18)

# design

winter=PhotoImage(file="w.png")
label1=Label(image=winter)
label1.place(x=250, y=216)

haze=PhotoImage(file="h.png")
label2=Label(image=haze)
label2.place(x=345, y=200)

winter1=PhotoImage(file="w.png")
label3=Label(image=winter1)
label3.place(x=440, y=216)

haze1=PhotoImage(file="h.png")
label4=Label(image=haze1)
label4.place(x=535, y=200)

winter2=PhotoImage(file="w.png")
label5=Label(image=winter2)
label5.place(x=630, y=216)

haze2=PhotoImage(file="h.png")
label6=Label(image=haze2)
label6.place(x=725, y=200)

#placing api's
f=Label(root,font=("Helvetica",10),fg='black',bg='#D9D9D9')
f.place(x=132,y=121)
h=Label(root,font=("Helvetica",10),fg='black',bg='#D9D9D9')
h.place(x=124,y=141)
p=Label(root,font=("Helvetica",10),fg='black',bg='#D9D9D9')
p.place(x=123,y=161)
w=Label(root,font=("Helvetica",10),fg='black',bg='#D9D9D9')
w.place(x=143,y=181)
d=Label(root,font=("Helvetica",10),fg='black',bg='#D9D9D9')
d.place(x=136,y=201)


t=Label(root,font=("Arial", 30,"bold"), fg="#404040", bg="#D9D9D9")
t.place(x=80,y=401)

tm1=Label(root,font=("Georgia",12),bg="#9faac3")
tm1.place(x=665,y=372)
tm2=Label(root,font=("Georgia",12),bg="#9faac3")
tm2.place(x=670,y=405)
cn=Label(root,font=("Georgia",11),bg="#9faac3")
cn.place(x=687,y=433)









root.mainloop()