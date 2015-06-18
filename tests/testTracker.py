import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from tracker import Tracker
import socket

t = Tracker(('192.168.0.122', 50000))
t.run()