import json
from socket import *
from threading import Thread
from .manager import *
from .image import *

BY = 1024 * 300

class Client(object):
    __addressTracker = None
    __server_connected = None 
    __keyAuthetication = None
    __manager = None
    def __init__(self, addressTracker):
        self.__addressTracker = addressTracker
        self.__keyAuthetication = 'ssj33'
        #self.__keyAuthetication = raw_input("Enter key Autentication:")
        self.__manager = Manager(self.__keyAuthetication)
        
    def chooseServer(self):
        listS = json.loads(self.listServer())
        print "Available servers:", listS['servers']
        addressIp = str(raw_input("Enter IP:"))
        addressPort = int(raw_input("Enter Port:"))
        return (addressIp, addressPort)
    
    def listServer(self):
        data = json.dumps({'type': 2, 'code': 0, 'status': 'OK'})
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(self.__addressTracker)
        sock.sendall(data)
        return sock.recv(BY)
    
    def requestImage(self):
        address = self.chooseServer()
        th=Thread( target=self.streamImage,
                    args = (address, ) )
        th.start()
        th.join()
        
    def streamImage(self, address):
        img = Image()
        socketServer = socket(AF_INET, SOCK_STREAM)
        socketServer.connect(address)
        while True:
            image = self.__manager.requestImagem(socketServer)
            if image == None:
                continue
            img.setImage(image)
            img.sleep()
    def requestDisplay(self):
        address = self.chooseServer()
        th=Thread( target=self.streamDisplay,
                    args = (address, ) )
        th.start()
        th.join()
        
    def streamDisplay(self, address):
        img = Image()
        socketServer = socket(AF_INET, SOCK_STREAM)
        socketServer.connect(address)
        while True:
            display = self.__manager.requestDisplay(socketServer)
            if display == None:
                continue
            img.setImage(display)
            img.sleep()