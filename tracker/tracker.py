import json, multiprocessing
from socket import *
from threading import Thread

BY = 1024 * 100
CONNECTIONS = multiprocessing.cpu_count()

class Tracker():
	__address = None
	__listClients = None
	__socket = None

	def __init__(self, address = None):
		self.__address = address
		self.__listClients = []

	def run(self):
		print "run"
		self.__socket = socket(AF_INET, SOCK_STREAM)
		self.__socket.bind(self.__address)
		self.__socket.listen(CONNECTIONS)
		while True:
			socketCliente, addressClient = self.__socket.accept()
			print "Client Connected -- IP = ", str(addressClient) + " ..."
			th=Thread( target=self.analyseRequest,
						args = ( socketCliente, addressClient))
			th.start()

	def analyseRequest(self, socketCliente, addressClient):
		print "analyseRequest"
		request = socketCliente.recv(BY)
		print request
		self.manager(request, socketCliente, addressClient)

	def manager(self, request, socket_cliente, address_client):
		print "manager"
		request = json.loads(str(request))
		
		if request['status'] == 'OK':
			if int(request['type']) == 0 and int(request['code']) == 1:
				print '**** Reply to Ping ****'
				address_client = (address_client[0], int(request['port']))
				if not address_client in self.__listClients:
					self.__listClients.append(address_client)

			elif int(request['type']) == 1 and int(request['code']) == 0:
				print '**** Broadcast Message ****'
				address_client = (address_client[0], int(request['port']))
				if not address_client in self.__listClients:
					self.__listClients.append(address_client)
				
				
			elif int(request['type']) == 2 and int(request['code']) == 0:
				print '**** I ask clients connected ****'
				data = json.dumps({'type':2,'code':1, 'status': 'OK', 'servers': self.__listClients})
				socket_cliente.sendall(data)
			else:
				print "Request not mapping..."
		else:
			print "Error request..."
			return
