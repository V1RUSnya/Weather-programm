from time import sleep
from tkinter import *
import requests

class weather:
    def __init__(self,city):
        self.appid = '5efbceafa8b3b152582211eb98168e3b'
        self.city = city

    def __str__(self):
        TextData = 'Температура: {0}, {1}'.format(self.temp,self.info)
        return TextData

    def Main():
        try:
            print('Поиск города...')
            city = txt.get()
            appid = '5efbceafa8b3b152582211eb98168e3b'
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': appid})
            data = res.json()
            cities = ["{} ({})".format(d['name'], d['sys']['country'])
                      for d in data['list']]
            sleep(1.5)
            print('Успешно!')
            print("Город:", cities)
            city_id = data['list'][0]['id']
            try:
                print('Запрос информации о погоде...')
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                data = res.json()
                sleep(1.5)
                print('Успешно!')
                print("Температура:", data['main']['temp'])
                print(data['weather'][0]['description'])
                #print(len(data['weather'][0]['description']))
                dlina = len(data['weather'][0]['description'])
                if dlina<15:
                    window.geometry('300x70')
                else:
                    window.geometry('375x70')
                tempp = data['main']['temp'],'\u2103'
                #lblb.configure(text=(data['weather'][0]['description']))
                lala.configure(text=(data['name']))
                #lbla.configure(text=(tempp))
            except:
                lbl.configure(text='Ошибка поиска погоды!')
                print('Ошибка запроса погоды!')
                window.geometry('300x70')
        except ValueError:
            lbl.configure(text='Ошибка поиска города!')
            print('Ошибка поиска города!')
            window.geometry('300x70')

window = Tk()

window['bg'] = 'white'
window.title('Погода')
window.geometry('230x70')
window.resizable(width=False, height=False)

frame = Frame(window)
frame = Frame(window, bg='white')
frame.place(relx=0.02, relwidth=1, relheight=1)

txt = Entry(frame, width=10, font=('Arial Blod', 15))
txt.grid(column=1, row=1)
txt.insert(END, 'Belgorod')

lbl = Label(window, text='Temp:', font=('Arial Blod', 15), bg="white")
lbl.grid(column=1, row=0)

lalala = Label(frame, text='', font=('Arial Blod', 15), bg="white")
lalala.grid(column=1, row=0)

lala = Label(frame, text='', font=('Arial Blod', 15), bg="white")
lala.grid(column=4, row=1)

btn = Button(frame, text='Узнать',font=('Arial Blod', 10), bg='white', command=weather.Main())
btn.grid(column=2, row=1)

window.mainloop()
