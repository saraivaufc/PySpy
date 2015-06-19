import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from server import Server

s = Server(('52.10.227.18', 50000))
s.run()