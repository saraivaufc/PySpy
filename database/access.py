import sqlite3, os, os.path


db = os.path.dirname(os.path.abspath(__file__)) + "/temp/access.db"


class Access(object):
    __conn = None
    def __init__(self):
        self.__conn = sqlite3.connect(db)
    def getConnecion(self):
        return self.__conn
    
    def getCursor(self):
        return self.__conn.cursor()
    
    def commit(self):
        self.__conn.commit()