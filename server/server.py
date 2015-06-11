from socket import *
from random import randint
import json, multiprocessing
from threading import Thread
from manager import Manager
from multiprocessing.connection import SocketClient
import camera

CONNECTIONS = multiprocessing.cpu_count()
BY = 1024 * 300

class Server(object):
	__name = None
	__port = None
	__addressTracker = None
	__socket = None
	__keyAuthetication = None
	__manager = None
	def __init__(self, addressTracker):
		self.__addressTracker = addressTracker
		self.__name = 'Ciano Saraiva'
		#self.__name = raw_input("Enter name:")
		self.__keyAuthetication = 'ssj33'
		#self.__keyAuthetication = raw_input("Enter key Autentication:")
		self.__port = randint(30000,50000)
		self.__manager = Manager(self.__port)

	def run(self):
		self.__socket = socket(AF_INET, SOCK_STREAM)
		try:
			self.__socket.bind(('localhost', self.__port))
		except:
			print "IP or Port in Use"
			return
		self.__socket.listen(CONNECTIONS)
		self.__manager.broadcastMessage(self.__addressTracker, self.__name)

		while True:
			socket_cliente, address_client = self.__socket.accept()
			print "Client Connected!!!"
			th=Thread( target=self.analyseRequest,
						args = ( socket_cliente, address_client))
			th.start()

	def analyseRequest(self, socketClient, addressClient):
		print 'analyseRequest'
		request = socketClient.recv(BY)
		self.manager(request, socketClient, addressClient);
	
	def manager(self, request, socketClient, addressClient):
		print 'manager'
		request = json.loads(str(request))
		if request['status'] == 'OK':
			if int(request['type']) == 0 and int(request['code']) == 0:
				print "**** Ping ****"
				self.__manager.replyToPing(socketClient, self.__addressTracker)
			
			elif int(request['type']) == 1 and int(request['code']) == 1:
				print "**** Reply to Broadcast Message ****"
			
			elif int(request['type']) == 3 and int(request['code']) == 0:
				print "**** Request Imagem ****"
				self.__manager.requestImagem(socketClient)
				
			elif int(request['type']) == 4 and int(request['code']) == 0:
				print "**** Request Audio ****"
				self.__manager.requestAudio(socketClient,request['size'])
				
			elif int(request['type']) == 5 and int(request['code']) == 0:
				print "**** Request Display ****"
				self.__manager.requestDisplay(socketClient)
				
			elif int(request['type']) == 6 and int(request['code']) == 0:
				print "**** Request Keyboard ****"
				self.__manager.requestKeyboard(socketClient)

		else:
			print "Error request..."
			return