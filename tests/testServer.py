import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from server import Server
import socket, pysocket
p = pysocket.Pysocket()
s = Server((p.get_lan_ip(), 50000))
s.run()