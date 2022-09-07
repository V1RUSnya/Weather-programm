from tkinter import *
from tkinter import messagebox
import requests

s_city = "Belgorod, RU"
city_id = 578072
appid = "5efbceafa8b3b152582211eb98168e3b"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print(s_city)
print("temp:", data['main']['temp'])
messagebox.showinfo('Погода:',data['main']['temp'])
