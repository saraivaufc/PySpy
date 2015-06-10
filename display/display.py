import pygame, sys, os
import pygame.camera
import gtk.gdk
import time, random

SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp"

pygame.init()
pygame.camera.init()


class Display(object):
	__display = None 
	def __init__(self):
		pass
	def captureScreen(self):
		w = gtk.gdk.get_default_root_window()
		sz = w.get_size()
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
		pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
		if (pb != None):
			timestamp = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
			filename = "%s/%s.jpg" % (SAVEDIR, timestamp)
			pb.save(filename,"png")
			return filename
		else:
			return None
