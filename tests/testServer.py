import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from server import Server

s = Server(('localhost', 50000))
s.run()