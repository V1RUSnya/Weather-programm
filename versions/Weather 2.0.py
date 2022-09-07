from tkinter import *
import requests
appid = "5efbceafa8b3b152582211eb98168e3b"

def city():
    try:
        s_city = txt.get()
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            print("temp:", data['main']['temp'])
            lbla.configure(text=(city_id))
            lblc.configure(text=(data['main']['temp']))
            window.geometry('280x70')
        except:
            lbla.configure(text='Ошибка поиска погоды!')
            print('Ошибка поиска погоды!')
            window.geometry('300x70')
    except:
        lbla.configure(text='Ошибка поиска города!')
        print('Ошибка поиска города!')
        window.geometry('300x70')


window = Tk()

window['bg'] = 'white'
window.title('Погода')
window.geometry('250x70')
window.resizable(width=False, height=False)

frame = Frame(window)
frame = Frame(window, bg='white')
frame.place(relx=0.02, relwidth=1, relheight=1)

txt = Entry(frame, width=10, font=('Arial Blod', 15))
txt.grid(column=1, row=1)
txt.insert(END, 'Belgorod')

lbl = Label(window, text='City id =', font=('Arial Blod', 15), bg="white")
lbl.grid(column=1, row=0)

lbla = Label(window, text='ID', font=('Arial Blod', 15), bg="white")
lbla.grid(column=2, row=0)

lblb = Label(window, text='Temp =', font=('Arial Blod', 15), bg="white")
lblb.grid(column=3, row=0)

lblc = Label(window, text='TEMP', font=('Arial Blod', 15), bg="white")
lblc.grid(column=4, row=0)

lala = Label(frame, text='', font=('Arial Blod', 15), bg="white")
lala.grid(column=1, row=0)

btn = Button(frame, text='Узнать',font=('Arial Blod', 10), bg='white', command=city)
btn.grid(column=2, row=1)

window.mainloop()
