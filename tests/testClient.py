import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from client import Client
import sys, socket

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Client(('52.10.227.18', 50000))
    ex.show()
    sys.exit(app.exec_())