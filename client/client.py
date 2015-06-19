# -*- coding: utf-8 -*-


from PyKDE4.kdeui import KSeparator
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from database import User
from image import *
from listen_servers_ui import Ui_ListServers
from login_ui import Ui_Login
from manager import *
from pysocket import *
from socket import *
from threading import Thread
from threads import *
import json, time
import sys, os
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
		MainWindow.resize(663, 491)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
		self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.verticalLayout_2 = QtGui.QVBoxLayout()
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.qImage = QtGui.QGraphicsView(self.centralwidget)
		self.qImage.setObjectName(_fromUtf8("qImage"))
		self.horizontalLayout.addWidget(self.qImage)
		self.kseparator = KSeparator(self.centralwidget)
		self.kseparator.setObjectName(_fromUtf8("kseparator"))
		self.horizontalLayout.addWidget(self.kseparator)
		self.qDesktop = QtGui.QGraphicsView(self.centralwidget)
		self.qDesktop.setObjectName(_fromUtf8("qDesktop"))
		self.horizontalLayout.addWidget(self.qDesktop)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.keyboard = QtGui.QLineEdit(self.centralwidget)
		self.keyboard.setObjectName(_fromUtf8("keyboard"))
		self.verticalLayout_2.addWidget(self.keyboard)
		self.horizontalLayout_2.addLayout(self.verticalLayout_2)
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.Login = QtGui.QPushButton(self.centralwidget)
		self.Login.setText(_fromUtf8(""))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(os.path.abspath(__file__)) + "/icons/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Login.setIcon(icon)
		self.Login.setIconSize(QtCore.QSize(40, 40))
		self.Login.setCheckable(False)
		self.Login.setObjectName(_fromUtf8("Login"))
		self.verticalLayout.addWidget(self.Login)
		self.ConnectServer = QtGui.QPushButton(self.centralwidget)
		self.ConnectServer.setText(_fromUtf8(""))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(os.path.abspath(__file__)) + "/icons/server.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ConnectServer.setIcon(icon1)
		self.ConnectServer.setIconSize(QtCore.QSize(40, 40))
		self.ConnectServer.setObjectName(_fromUtf8("ConnectServer"))
		self.verticalLayout.addWidget(self.ConnectServer)
		self.connectWebCam = QtGui.QPushButton(self.centralwidget)
		self.connectWebCam.setText(_fromUtf8(""))
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(os.path.abspath(__file__)) + "/icons/webcam.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.connectWebCam.setIcon(icon2)
		self.connectWebCam.setIconSize(QtCore.QSize(40, 40))
		self.connectWebCam.setCheckable(False)
		self.connectWebCam.setObjectName(_fromUtf8("connectWebCam"))
		self.verticalLayout.addWidget(self.connectWebCam)
		self.connectDesktop = QtGui.QPushButton(self.centralwidget)
		self.connectDesktop.setText(_fromUtf8(""))
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(os.path.abspath(__file__)) + "/icons/desktop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.connectDesktop.setIcon(icon3)
		self.connectDesktop.setIconSize(QtCore.QSize(40, 40))
		self.connectDesktop.setCheckable(False)
		self.connectDesktop.setObjectName(_fromUtf8("connectDesktop"))
		self.verticalLayout.addWidget(self.connectDesktop)
		self.connectAudio = QtGui.QPushButton(self.centralwidget)
		self.connectAudio.setText(_fromUtf8(""))
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(os.path.abspath(__file__)) + "/icons/microphone.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.connectAudio.setIcon(icon4)
		self.connectAudio.setIconSize(QtCore.QSize(40, 40))
		self.connectAudio.setCheckable(False)
		self.connectAudio.setObjectName(_fromUtf8("connectAudio"))
		self.verticalLayout.addWidget(self.connectAudio)
		self.connectKeyboard = QtGui.QPushButton(self.centralwidget)
		self.connectKeyboard.setText(_fromUtf8(""))
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(os.path.abspath(__file__)) + "/icons/keyboard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.connectKeyboard.setIcon(icon5)
		self.connectKeyboard.setIconSize(QtCore.QSize(40, 40))
		self.connectKeyboard.setCheckable(False)
		self.connectKeyboard.setObjectName(_fromUtf8("connectKeyboard"))
		self.verticalLayout.addWidget(self.connectKeyboard)
		self.horizontalLayout_2.addLayout(self.verticalLayout)
		self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 25))
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
		try:
			sock.connect(self.__addressTracker)
		except:
			msn = QMessageBox.warning(self, "Tracker",
                "Servers not found...", QMessageBox.Close)
			return
		sock.sendall(data)
		try:
			response = json.loads(self.__pysocket.recvall(sock))['servers']
		except:
			return None
		return response

	def requestImage(self):
		print 'Request Image'
		t = UpdateImage(self.__server_connected, self.__manager, self)
		QtCore.QObject.connect(t, QtCore.SIGNAL(_fromUtf8("update()")), self.streamImage)
		t.start()
		
	def streamImage(self):
		self.setImageWebCam(SAVEDIR + 'image.jpg')
	def requestDisplay(self):
		print 'Request Desktop'
		t = UpdateDesktop(self.__server_connected, self.__manager, self)
		QtCore.QObject.connect(t, QtCore.SIGNAL(_fromUtf8("update()")), self.streamDisplay)
		t.start()
		
	def streamDisplay(self):
		self.setImageDesktop(SAVEDIR + 'display.png')
		
	def requestAudio(self, size = 1024):
		print 'Request Audio'
		t = UpdateAudio(self.__server_connected,size,  self.__manager, self)
		QtCore.QObject.connect(t, QtCore.SIGNAL(_fromUtf8("update()")), self.streamAudio)
		t.start()
		
	def streamAudio(self):
		t = PlayAudio(SAVEDIR + 'audio.wav', self)
		t.start()
		
	def requestKeyboard(self, size = 40):
		print 'Request Keyboard'
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
