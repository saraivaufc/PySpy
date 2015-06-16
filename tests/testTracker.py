import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from tracker import Tracker

t = Tracker(('localhost', 23302))
t.run()