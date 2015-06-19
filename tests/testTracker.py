import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import socket
from tracker import Tracker
import pysocket
p = pysocket.Pysocket()
t = Tracker((p.get_lan_ip(), 50000))
t.run()