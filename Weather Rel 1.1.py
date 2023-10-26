# -*- coding: cp1251 -*-
import sys
import requests
import http.client
from twoip import TwoIP
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.appid = "5efbceafa8b3b152582211eb98168e3b"
        self.geo = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(210, 100)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0); ")
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 211, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.MainLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setHorizontalSpacing(10)
        self.MainLayout.setVerticalSpacing(12)
        self.MainLayout.setObjectName("MainLayout")
        self.L1 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L1.setFont(font)
        self.L1.setObjectName("L1")
        self.MainLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.L1)
        self.CityLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CityLabel.setFont(font)
        self.CityLabel.setObjectName("CityLabel")
        self.MainLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.CityLabel)
        self.L2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.L2.setFont(font)
        self.L2.setObjectName("L2")
        self.MainLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.L2)
        self.MainTemp = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MainTemp.setFont(font)
        self.MainTemp.setObjectName("MainTemp")
        self.MainLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.MainTemp)
        self.LabelOption = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LabelOption.setFont(font)
        self.LabelOption.setObjectName("LabelOption")
        self.L1.setStyleSheet("color: white;")
        self.L2.setStyleSheet("color: white;")
        self.MainTemp.setStyleSheet("color: white;")
        self.LabelOption.setStyleSheet("color: white;")
        self.CityLabel.setStyleSheet("color: white;")
        self.MainLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.LabelOption)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather"))
        self.L1.setText(_translate("MainWindow", "City:"))
        self.CityLabel.setText(_translate("MainWindow", "Belgorod"))
        self.L2.setText(_translate("MainWindow", "Temp: "))
        self.MainTemp.setText(_translate("MainWindow", "24,6 C"))
        self.LabelOption.setText(_translate("MainWindow", "Погода"))
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
                print("City: ", cities)
                city_id = data['list'][0]['id']
                try:
                    print('Requesting weather information...')
                    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': self.appid})
                    data = res.json()
                    print("Temperature:", data['main']['temp'])
                    print(data['weather'][0]['description'])
                    tempp = str(data['main']['temp'])
                    self.MainTemp.setText(tempp + " C")
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
    MainWindow.setGeometry(1920 - 210, 1080 - 140, 210, 100)
    MainWindow.show()
    sys.exit(app.exec())
