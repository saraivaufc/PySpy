class User(object):
    __name = None
    __username = None
    __password = None
    
    def __init__(self, name, username, password='pyspy'):
        self.__name = name
        self.__username = username
        self.__password = password
        
    def toString(self):
        return "[name = "+self.__name+", username = "+self.__username+"]"
    
    def setName(self, name):
        self.__name = name
    
    def setUsername(self, username):
        self.__username = username
    
    def setPassword(self, password):
        self.__password = password    
    
    def getName(self):
        return self.__name
    
    def getUsername(self):
        return str(self.__username)
    
    def getPassword(self):
        return str(self.__password)
    
    