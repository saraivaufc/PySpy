import pygame, sys, os
import pygame.camera
import gtk.gdk
import time, random
import base64

SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp"

pygame.init()
pygame.camera.init()


class Display(object):
	__display = None 
	def __init__(self):
		pass
	
	def getDisplay(self):
		w = gtk.gdk.get_default_root_window()
		sz = w.get_size()
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
		pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
		return pb
	def getDisplayData(self):
		path = self.captureDisplay()
		with open(path, "rb") as image_file:
			encoded_string = base64.b64encode(image_file.read())
		return encoded_string
	
	def captureDisplay(self):
		display = self.getDisplay()
		if (display != None):
			filename = "%s/%s.png" % (SAVEDIR, 'display')
			display.save(filename,"png")
			return filename
		else:
			return None