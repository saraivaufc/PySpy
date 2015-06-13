import sys  #for exit
import struct
import time

End = '}'
#Sim, e gambi, mas funciona
class Pysocket(object):
    def __init__(self):
        pass
    def recvall(self, sock):
        total_data=[]
        data='' 
        while True: 
            try:
                data=sock.recv(8192)
            except:
                print "Erro ao receber os dados..."
                return None
            if End in data: 
                total_data.append(data) 
                break 
            total_data.append(data)
        result=''.join(total_data) 
        return result