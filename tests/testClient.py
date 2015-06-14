from client import Client
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Client(('localhost', 23302))
    ex.show()
    sys.exit(app.exec_())