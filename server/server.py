from socket import *
import json, multiprocessing
from threading import Thread

CONNECTIONS = multiprocessing.cpu_count()
BY = 1024

class Server(object):
	__address = None
	__socket = None
	__keyAuthetication = None
	def __init__(self, address):
		self.__address = address

	def run(self):
		self.__socket = socket(AF_INET, SOCK_STREAM)
		self.__socket.bind(self.__address)
		self.__socket.listen(CONNECTIONS)
		self.__requestKey()
		
		while True:
			socket_cliente, address_client = self.__socket.accept()
			print "Client Connected!!!"
			th=Thread( target=self.analyseRequest,
						args = ( socket_cliente, address_client))
			th.start()

	def analyseRequest(self, socket_cliente, address_client):
		msn = True
		request = ""
		while  msn != None:
			msn = socket_cliente.recv(BY)
			request +=msn
		print request
	def requestKey(self):
		try:
			self.__keyAuthetication = raw_input("Enter key Autentication:")
			return True
		except:
			return False 



