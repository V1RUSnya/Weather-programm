# This Python file uses the following encoding: utf-8
import requests
import http.client
from twoip import TwoIP
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMainWindow, QApplication

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
        
        def city(s_city):
            style(1)
            try:
                print('City search...')
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

        def style(a):
            if a == 0:
                image = "1.png"
            elif a == 1:
                image = "2.png"
            elif a == 2:
                image = "3.png"
            pixmap = QPixmap(image)
            self.labelimage.setStyleSheet('background-image: url("1.png");')
            self.labelimage.setPixmap(pixmap)
            self.labelimage.setScaledContents(True)
            
        def sityfrom():
            conn = http.client.HTTPConnection("ifconfig.me")
            conn.request("GET", "/ip")
            response = conn.getresponse()
            ips = response.read().decode('utf-8')
            twoip = TwoIP(key = None)
            self.geo = twoip.geo(ip = ips)
            
        self.geo = "Moscow"
        city(self.geo)

def application():
    app = QApplication([])
    window = Start()
    window.show()
    app.exec()

application()
