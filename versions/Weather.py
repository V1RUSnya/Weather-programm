from tkinter import *
import requests

s_city = "Belgorod, RU"
city_id = 578072
appid = "5efbceafa8b3b152582211eb98168e3b"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

def clicked():
    print(s_city)
    print("temp:", data['main']['temp'])
    lbll.configure(text=data['main']['temp'])
    window.geometry('475x75')

window = Tk()

#window['bg'] = '#FFFAFA'
window.title('Погода')
window.geometry('435x75')
window.resizable(width=False, height=False)

frame = Frame(window)
#frame = Frame(window, bg='#FFFAFA')
frame.place(relx=0.02, relwidth=1, relheight=1)

lbl = Label(frame, text='Сейчас: ', font=('Arial Blod', 30))
lbl.grid(column=0, row=0)

lbll = Label(frame, text='?', font=('Arial Blod', 30))
lbll.grid(column=1, row=0)

lblll = Label(frame, text=' градусов', font=('Arial Blod', 30))
lblll.grid(column=2, row=0)

btn = Button(frame, text='Проверить', bg='white', command=clicked)
btn.grid(column=1, row=1)

window.mainloop()
