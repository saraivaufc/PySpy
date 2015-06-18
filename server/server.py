# -*- encoding=utf-8 -*-
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from socket import *
from random import randint
import json, multiprocessing
from threading import Thread
from manager import Manager
from multiprocessing.connection import SocketClient
import camera
from database import *
import datetime

CONNECTIONS = multiprocessing.cpu_count()
BY = 1024 * 300

class Server(object):
	__name = None
	__port = None
	__addressTracker = None
	__socket = None
	__manager = None
	__userDAO = None
	def __init__(self, addressTracker):
		self.__addressTracker = addressTracker
		self.__name = raw_input("Enter name from server:")
		self.__port = randint(30000,50000)
		self.__manager = Manager(self.__port)
		self.__userDAO = UserDAO()
		self.menu()

	def menu(self):
		try:
			option = int(raw_input("""O que você deseja fazer?\n(1) Iniciar o servidor\n(2) Criar usuário\n(3) Ver usuários\n(4) Sair\nOpção escolhida:"""))
		except:
			self.menu()
		if option == 1:
			self.run()
		elif option == 2:
			self.createUser()
		elif option == 3:
			print self.listUsers()
		elif option == 4:
			sys.exit(0)
			return
		else:
			self.menu()
		self.menu()

	def run(self):
		self.__socket = socket(AF_INET, SOCK_STREAM)
		try:
			self.__socket.bind((socket.gethostname(), self.__port))
		except:
			print "IP or Port in Use"
			return
		self.__socket.listen(CONNECTIONS)
		self.__manager.broadcastMessage(self.__addressTracker, self.__name)
		th=Thread( target=self.runThread,
						args = ())
		th.start()
		
	def runThread(self):
		while True:
			socket_cliente, address_client = self.__socket.accept()
			print "Client Connected!!!"
			th=Thread( target=self.analyseRequest,
						args = ( socket_cliente, address_client))
			th.start()
		
	def createUser(self):
		name = str(raw_input("ENTER NAME:"))
		username = str(raw_input("ENTER USERNAME:"))
		password = str(raw_input("ENTER PASSWORD:"))
		password2 = str(raw_input("REPEAT PASSWORD:"))
		if password != password2:
			print "PASSWORD DIFERENT!!!"
		else:
			uDAO = UserDAO()
			user = User(name, username, password)
			uDAO.insert(user)
			print "USER INSERT SUCCESS!!!"
	def listUsers(self):
		uDAO = UserDAO()
		return uDAO.list()
	
	def isAuthenticated(self, request, msn):
		print "ANALISE AUTHENTICATION..."
		try:
			username = request['username']
			password = request['password']
		except:
			print "USER IS NOT AUTHENTICATED!!!"
			return False
		uDAO = UserDAO()
		user = uDAO.getUser(username)
		if len(user) == 1:
			if user[0][2] == password:
				print "USER IS AUTHENTICATED!!!"
				uDAO.log(User(str(user[0][0]), str(user[0][1])), msn) 
				
				return True
			else:
				print "USER IS NOT AUTHENTICATED!!!"
				return False
		else:
			print "USER IS NOT AUTHENTICATED!!!"
			return False
			
		
	def analyseRequest(self, socketClient, addressClient):
		print 'analyseRequest'
		request = socketClient.recv(BY)
		self.manager(request, socketClient, addressClient);
	
	def manager(self, request, socketClient, addressClient):
		print 'manager'
		try:
			request = json.loads(str(request))
			now = datetime.datetime.now()
		except:
			print "Erro Loads Reqquest in Manager" 
			return
		if request['status'] == 'OK':
			if int(request['type']) == 0 and int(request['code']) == 0:
				print "**** Ping ****"
				self.__manager.replyToPing(socketClient, self.__addressTracker)
			
			elif int(request['type']) == 1 and int(request['code']) == 1:
				print "**** Reply to Broadcast Message ****"
			
			elif int(request['type']) == 3 and int(request['code']) == 0:
				print "**** Request Imagem ****"
				if self.isAuthenticated(request, "REQUEST IMAGE IN " + str(now) ) == False:
					socketClient.sendall("502")
				else:
					self.__manager.requestImagem(socketClient)
				
			elif int(request['type']) == 4 and int(request['code']) == 0:
				print "**** Request Audio ****"
				if self.isAuthenticated(request, "REQUEST AUDIO IN " + str(now)) == False:
					socketClient.sendall("502")
				else:
					self.__manager.requestAudio(socketClient,request['size'])
				
			elif int(request['type']) == 5 and int(request['code']) == 0:
				print "**** Request Display ****"
				if self.isAuthenticated(request, "REQUEST DISPLAY IN " + str(now)) == False:
					socketClient.sendall("502")
				else:
					self.__manager.requestDisplay(socketClient)
				
			elif int(request['type']) == 6 and int(request['code']) == 0:
				print "**** Request Keyboard ****"
				if self.isAuthenticated(request, "REQUEST KEYBOARD IN " + str(now)) == False:
					socketClient.sendall("502")
				else:
					self.__manager.requestKeyboard(socketClient,request['size'])

		else:
			print "Error request..."
			return