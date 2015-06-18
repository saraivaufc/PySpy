import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from server import Server
import socket

s = Server((socket.gethostname(), 50000))
s.run()