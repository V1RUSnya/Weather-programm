# This Python file uses the following encoding: utf-8
import requests
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QFileInfo, QSize
from PyQt6.QtWidgets import QFileDialog, QWidget, QVBoxLayout, QLabel, QPushButton, QMainWindow, QApplication, QMessageBox

class Start(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.appid = "5efbceafa8b3b152582211eb98168e3b"
        
        self.setWindowTitle("Weather")
        self.setFixedSize(QSize(350, 200))
        
        self.label = QLabel()
        self.labelimage = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.labelimage)
        layout.addWidget(self.label)
        
        self.container = QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)
        
        def city(NameofSity):
            try:
                print('City search...')
                s_city = NameofSity
                res = requests.get("http://api.openweathermap.org/data/2.5/find",
                                   params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': self.appid})
                data = res.json()
                cities = ["{} ({})".format(d['name'], d['sys']['country'])
                          for d in data['list']]
                print('Successful!')
                print("City: ", cities)
                city_id = data['list'][0]['id']
                try:
                    print('Requesting weather information...')
                    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': self.appid})
                    data = res.json()
                    print('Successful!')
                    print("Temperature:", data['main']['temp'])
                    print(data['weather'][0]['description'])
                    #print(len(data['weather'][0]['description'])) #Отображает длину строк
                    dlina = len(data['weather'][0]['description'])
                    #if dlina<15:
                        #window.geometry('300x70')
                    #else:
                        #window.geometry('375x70')
                    tempp = data['main']['temp'],'\u2103'
                    #lblb.configure(text=(data['weather'][0]['description']))
                    #lala.configure(text=(data['name']))
                    #lbla.configure(text=(tempp))
                except:
                    #lbla.configure(text='Ошибка поиска погоды!')
                    print('Weather request error!')
            except:
                #lbla.configure(text='Ошибка поиска города!')
                print('City search error!')
                #window.geometry('300x70')       

        def style(a):
            if a == 0:
                pixmap = QPixmap('image.jpg')
            if a == 1:
                pixmap = QPixmap('image.jpg')
            if a == 2:
                pixmap = QPixmap('image.jpg')
            self.labelimage.setPixmap(pixmap)
        city(NameofSity = "Belgorod")

def application():
    app = QApplication([])
    window = Start()
    window.show()
    app.exec()

application()
