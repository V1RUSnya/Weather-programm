# -*- coding: utf-8 -*-
import requests
import http.client
from twoip import TwoIP
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.appid = "5efbceafa8b3b152582211eb98168e3b"
        self.geo = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(267, 99)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTemp = QtWidgets.QLabel(parent=self.centralwidget)
        self.MainTemp.setGeometry(QtCore.QRect(0, 0, 181, 51))
        
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        
        self.MainTemp.setFont(font)
        self.MainTemp.setObjectName("MainTemp")
        self.CityLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.CityLabel.setGeometry(QtCore.QRect(0, 50, 181, 21))
        
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(10)
        
        self.CityLabel.setFont(font)
        self.CityLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.CityLabel.setWordWrap(False)
        self.CityLabel.setObjectName("CityLabel")
        self.LabelOption = QtWidgets.QLabel(parent=self.centralwidget)
        self.LabelOption.setGeometry(QtCore.QRect(0, 70, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(12)
        self.LabelOption.setFont(font)
        self.LabelOption.setObjectName("LabelOption")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather"))
        self.MainTemp.setText(_translate("MainWindow", "00 C"))
        self.CityLabel.setText(_translate("MainWindow", "404"))
        self.LabelOption.setText(_translate("MainWindow", "404"))
        
    def StartSearch(self):
         try:
              conn = http.client.HTTPConnection("ifconfig.me")
              conn.request("GET", "/ip")
              response = conn.getresponse()
              ips = response.read().decode('utf-8')
              twoip = TwoIP(key = None)
              self.geo = twoip.geo(ip = ips)
              self.CityLabel.setText(str(self.geo['city']))
              self.city(self.geo['city'])
         except Exception as e:
              print(f"Cant acess to API, load default city! Error: {e}")
              self.CityLabel.setText("Belgorod")
              self.city("Belgorod")
        
    def city(self, s_city):
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
                    tempp = str(data['main']['temp'])
                    self.MainTemp.setText(tempp)
                    self.LabelOption.setText(str(data['weather'][0]['description']))
                except:
                    print('Weather request error!')
        except:
                print('City search error!') 
                                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.StartSearch()
    MainWindow.show()
    sys.exit(app.exec())
