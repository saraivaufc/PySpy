import pygame, sys, os
import pygame.camera
import time, random
import base64

SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp"

pygame.init()
pygame.camera.init()

class Camera(object):
	__cam = None
	def __init__(self):
		try:
			self.__cam = pygame.camera.Camera(self.getCamerasConected()[0], (720,680))
		except:
			self.__cam = None

	def getImage(self):
		if self.__cam == None:
			return None
		self.__cam.start()
		image = self.__cam.get_image()
		self.__cam.stop()
		return image
	def getImageData(self):
		if self.__cam == None:
			return None
		path = self.captureImage()
		with open(path, "rb") as image_file:
			encoded_string = base64.b64encode(image_file.read())
		return encoded_string
		

	def captureImage(self):
		image = self.getImage()
		filename = "%s/%s.jpg" % (SAVEDIR, 'image')
		pygame.image.save(image, filename)
		return filename

	def getCamerasConected(self):
		cameras = pygame.camera.list_cameras()
		if not cameras:
			raise ValueError("Sorry, no cameras detected.")
		return cameras		