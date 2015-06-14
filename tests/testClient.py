from client import Ui_MainWindow
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow(('localhost', 23302))
    ex.show()
    sys.exit(app.exec_())