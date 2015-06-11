from socket import *
import json, os
import time, random
import camera, display, keyboard, audio
import base64

BY = 1024 * 1024 * 1024
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

    def requestImagem(self, socketServer):
        data = json.dumps({'type': 3, 'code': 0 ,'status' : 'OK', 'key': self.__key})
        try:
            socketServer.sendall(data)
        except:
            return None
        return self.responseImagem(socketServer)
    
    def responseImagem(self,socketServer):
        response = socketServer.recv(BY)
        print response
        image = json.loads(response)
        return self.dataToImage(image)
    def dataToImage(self, data):
        data = data['image']
        filename = "%s/%s.jpg" % (SAVEDIR, 'image')
        fh = open(filename, "wb")
        fh.write(data.decode('base64'))
        fh.close()
        return filename
                
        
        
    
    def requestAudio(self, socketServer):
        data = json.dumps({'type': 4, 'code': 0 ,'status' : 'OK','size': 1024 * 3 ,  'key': self.__key})
        try:
            socketServer.sendall(data)
        except:
            print "requestAudio Erro!!!"
            return None
        return self.responseAudio(socketServer)
    
    def responseAudio(self, socketServer):
        response = socketServer.recv(BY)
        open("/home/user/teste.txt", "w").write(response)
        response = json.loads(str(response))
        return self.dataToAudio(response)
    
    def dataToAudio(self, response):
        data = response['audio']
        filename = "%s/%s.wav" % (SAVEDIR, 'audio')
        fh = open(filename, "wb")
        fh.write(data.decode('base64'))
        fh.close()
        return filename
    def requestDisplay(self, socketServer):
        data = json.dumps({'type': 5, 'code': 0 ,'status' : 'OK', 'key': self.__key})
        try:
            socketServer.sendall(data)
        except:
            return None
        return self.responseDisplay(socketServer)
    
    def responseDisplay(self,socketServer):
        response = socketServer.recv(BY)
        print "Client", response, "Terminou"
        try:
            image = json.loads(str(response))
        except:
            return None
        return self.dataToDisplay(image)
    def dataToDisplay(self, data):
        data = data['display']
        filename = "%s/%s.png" % (SAVEDIR, 'display')
        fh = open(filename, "wb")
        fh.write(data.decode('base64'))
        fh.close()
        return filename
    
    def requestKeyboard(self, socketClient):
        data = json.dumps({'type': 6, 'code': 0 ,'status' : 'OK', 'key': self.__key})
        socketClient.send(data)
        return True