import pygame, sys
from pygame.locals import *
import time, random
import gtk, pygtk
from threading import Thread

pygame.init()
c = pygame.time.Clock()
window = gtk.Window()
screen = window.get_screen()  
        
class Image(object):
    __display = None
    __size = None
    __sleep = None
    def __init__(self, sleep = 5,size=(int(screen.get_width() * 0.8),int(screen.get_height() * 0.8) )):
        self.__size = size 
        self.__sleep = sleep
        self.__display = pygame.display.set_mode(self.__size)
        th=Thread( target=self.update,
                    args = () )
        th.start()
    def setImage(self, path):
        img=pygame.image.load(path) 
        self.__display.blit(img,(0,0))
        pygame.display.flip()
        
    def sleep(self):
        c.tick(self.__sleep)
        
    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            try:
                self.__display.update()
            except:
                return