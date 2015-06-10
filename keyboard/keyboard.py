import pygame, sys, os
import pygame.camera
import time, random

SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp"

pygame.init()
pygame.camera.init()

class Keyboard(object):
	def __init__(self):
		pass

	def captureKeys(self):
		pass
