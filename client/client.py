import json
from socket import *
from threading import Thread
from .manager import *
from .image import *
from pysocket import *
import pyaudio
import wave
import sys

chunk = 1024

class Client(object):
    __addressTracker = None
    __server_connected = None 
    __keyAuthetication = None
    __manager = None
    __pysocket = None
    
    def __init__(self, addressTracker):
        self.__addressTracker = addressTracker
        self.__pysocket = Pysocket()
        self.__keyAuthetication = 'ssj33'
        #self.__keyAuthetication = raw_input("Enter key Autentication:")
        self.__manager = Manager(self.__keyAuthetication)
        
    def chooseServer(self):
        try:
            listS = json.loads(self.listServer())
        except:
            print "Erro loads ListServers"
            return None
        print "Available servers:", listS['servers']
        addressIp = str(raw_input("Enter IP:"))
        addressPort = int(raw_input("Enter Port:"))
        return (addressIp, addressPort)
    
    def listServer(self):
        data = json.dumps({'type': 2, 'code': 0, 'status': 'OK'})
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(self.__addressTracker)
        sock.sendall(data)
        return self.__pysocket.recvall(sock)
    
    def requestImage(self):
        address = self.chooseServer()
        th=Thread( target=self.streamImage,
                    args = (address, ) )
        th.start()
        
    def streamImage(self, address):
        img = Image(25)
        socketServer = socket(AF_INET, SOCK_STREAM)
        try:
            socketServer.connect(address)
        except:
            print "IP or PORT invalid!!!"
            return
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
        
    def streamDisplay(self, address):
        img = Image(25)
        socketServer = socket(AF_INET, SOCK_STREAM)
        try:    
            socketServer.connect(address)
        except:
            print "IP or PORT invalid!!!"
            return
        while True:
            display = self.__manager.requestDisplay(socketServer)
            if display == None:
                continue
            img.setImage(display)
            img.sleep()
    def requestAudio(self, size):
        address = self.chooseServer()
        th=Thread( target=self.streamAudio,
                    args = (address,size) )
        th.start()
    
    def streamAudio(self, address, size):
        socketServer = socket(AF_INET, SOCK_STREAM)
        try:    
            socketServer.connect(address)
        except:
            print "IP or PORT invalid!!!"
            return
        #while True:
        audio = self.__manager.requestAudio(socketServer, size)
        if audio == None:
            return
        print audio
        wf = wave.open(audio, 'rb')
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
        
        
    def requestKeyboard(self, size):
        address = self.chooseServer()
        th=Thread( target=self.streamKeyboard,
                    args = (address,size ) )
        th.start()
        
    def streamKeyboard(self, address, size):
        socketServer = socket(AF_INET, SOCK_STREAM)
        try:    
            socketServer.connect(address)
        except:
            print "IP or PORT invalid!!!"
            return
        while True:
            fileKeys = self.__manager.requestKeyboard(socketServer, size)
            if fileKeys == None:
                continue
            print open(fileKeys, "r").read()