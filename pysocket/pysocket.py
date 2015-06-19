import sys  #for exit
import struct
import time
import os
if os.name != "nt":
    import fcntl
    import struct


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
        
    def get_interface_ip(self, ifname):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

    def get_lan_ip(self):
        import socket
        ip = socket.gethostbyname(socket.gethostname())
        if ip.startswith("127.") and os.name != "nt":
            interfaces = [
                "eth0",
                "eth1",
                "eth2",
                "wlan0",
                "wlan1",
                "wifi0",
                "ath0",
                "ath1",
                "ppp0",
                ]
            for ifname in interfaces:
                try:
                    ip = self.get_interface_ip(ifname)
                    break
                except IOError:
                    pass
        return ip