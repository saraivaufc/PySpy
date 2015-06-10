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
        
    def streamImage(self, address):
        img = Image()
        i = 1
        while i < 20:
            image = self.__manager.requestImagem(address)
            if image == None:
                break
            img.setImage(image)
            img.sleep()
            i = i+1
    def requestDisplay(self):
        address = self.chooseServer()
        th=Thread( target=self.streamDisplay,
                    args = (address, ) )
        th.start()
        
    def streamDisplay(self, address):
        img = Image(1)
        i = 1
        while i < 20:
            display = self.__manager.requestDisplay(address)
            if display == None:
                continue
            img.setImage(display)
            img.sleep()
            i = i+1