import json
from socket import *
from .manager import *

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
    
    def listServer(self):
        data = json.dumps({'type': 2, 'code': 0, 'status': 'OK'})
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(self.__addressTracker)
        sock.sendall(data)
        msn = sock.recv(BY)
        print msn
    
    def requestImage(self):
        addressIp = str(raw_input("Enter IP:"))
        addressPort = int(raw_input("Enter Port:"))
        address = (addressIp, addressPort)
        image = self.__manager.requestImagem(address)
        print image