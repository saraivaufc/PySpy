import sys
from socket import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from manager import *

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