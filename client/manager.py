from socket import *
import json, os
import time, random
import camera, display, keyboard, audio
import base64

BY = 1024 * 300
SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp"

class Manager(object):
    __camera = None
    __display = None
    __keyboard = None
    __audio = None
    __port = None
    __key = None
    
    def __init__(self, key):
        self.__camera = camera.Camera()
        self.__display = display.Display()
        self.__keyboard = keyboard.Keyboard()
        self.__audio = audio.Audio()
        self.__key = key

    def requestImagem(self, addressServer):
        data = json.dumps({'type': 3, 'code': 0 ,'status' : 'OK', 'key': self.__key})
        socketServer = socket(AF_INET, SOCK_STREAM)
        socketServer.connect(addressServer)
        socketServer.sendall(data)
        return self.responseImagem(socketServer)
    
    def responseImagem(self,socketServer):
        image = socketServer.recv(BY)
        return self.dataToImage(image)
    def dataToImage(self, data):
        print data
        imgdata = base64.b64decode(str(data))
        timestamp = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
        filename = "%s/%s.jpg" % (SAVEDIR, timestamp)
        with open(filename, 'wb') as f:
            f.write(imgdata)
        return filename
                
        
        

    def requestAudio(self, socketClient):
        data = json.dumps({'type': 4, 'code': 0 ,'status' : 'OK', 'key': self.__key})
        socketClient.sendall(data)
        return True

    def requestDisplay(self, socketClient):
        data = json.dumps({'type': 5, 'code': 0 ,'status' : 'OK', 'key': self.__key})
        socketClient.sendall(data)
        return True

    def requestKeyboard(self, socketClient):
        data = json.dumps({'type': 6, 'code': 0 ,'status' : 'OK', 'key': self.__key})
        socketClient.send(data)
        return True