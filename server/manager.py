from socket import *
import json
import camera, display, keyboard, audio, pygame
from multiprocessing.connection import SocketClient


clock = pygame.time.Clock()

class Manager(object):
	__camera = None
	__display = None
	__keyboard = None
	__audio = None
	__port = None
	
	def __init__(self, port):
		self.__camera = camera.Camera()
		self.__display = display.Display()
		self.__keyboard = keyboard.Keyboard()
		self.__audio = audio.Audio()
		self.__port = port

	def replyToPing(self, addressTracker):
		data = json.dumps({'type': 0, 'code': 1 ,'status': 'OK', 'port': self.__port})
		s = socket(AF_INET, SOCK_STREAM)
		s.connect(addressTracker)
		s.sendall(data)
		s.close()
		return True

	def broadcastMessage(self, addressTracker, name):
		print 'Send BroadcastMessage'
		data = json.dumps({'type': 1, 'code': 0 ,'status': 'OK','name': name, 'port': self.__port})
		s = socket(AF_INET, SOCK_STREAM)
		s.connect(addressTracker)
		s.sendall(data)
		s.close()
		return True

	def requestImagem(self, socketServer):
		while True:
			image = self.__camera.getImageData()
			data = json.dumps({'type': 3, 'code': 1 ,'status' : 'OK', 'image': image})
			try:
				socketServer.sendall(data)
			except:
				break
		return True

	def requestAudio(self, socketClient):
		audio = "sds"
		data = json.dumps({'type': 4, 'code': 1 ,'status' : 'OK', 'audio': audio})
		socketClient.sendall(data)
		return True

	def requestDisplay(self, socketClient):
		while True:
			display = self.__display.getDisplayData()
			data = json.dumps({'type': 5, 'code': 1 ,'status' : 'OK', 'display': display})
			try:
				print "Server", data
				socketClient.sendall(data)
			except:
				break
		return True

	def requestKeyboard(self, socketClient):
		keyboard = "Cc"
		data = json.dumps({'type': 6, 'code': 1 ,'status' : 'OK', 'keyboard': keyboard})
		socketClient.send(data)
		return True