import json, time
from socket import *
from threading import Thread
from .manager import *
from .image import *
from pysocket import *
import pyaudio
import wave
import sys
from database import User

chunk = 1024

class Client(object):
    __addressTracker = None
    __server_connected = None 
    __keyAuthetication = None
    __manager = None
    __pysocket = None
    __user = None
    
    def __init__(self, addressTracker):
        self.__addressTracker = addressTracker
        self.__pysocket = Pysocket()
        self.__user = User("name", "username", "password")
        self.__manager = Manager(self.__user)
    