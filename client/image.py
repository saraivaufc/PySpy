import pygame, sys
import time, random

pygame.init()
c = pygame.time.Clock()

class Image(object):
    __display = None
    __size = None
    def __init__(self, size=(640,480)):
        self.__size = size
        self.__display = pygame.display.set_mode(self.__size, 0)
    def setImage(self, path):
        img=pygame.image.load(path) 
        self.__display.blit(img,(0,0))
        pygame.display.flip()
        
    def sleep(self):
        c.tick(25)