# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
from PyQt4.Qt import QStandardItemModel, QStandardItem


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ListServers(QtGui.QDialog):
    def __init__(self,parent=None):
        self.confirm = None
        self.__index = None
        self.__model = QStandardItemModel()
        
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("LIst Servers"))
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.list_servers = QtGui.QListView(Dialog)
        self.list_servers.setObjectName(_fromUtf8("list_servers"))
        self.verticalLayout.addWidget(self.list_servers)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        self.list_servers.setModel(self.__model)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.list_servers, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.listServersClicked)
        
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def listServersClicked(self, index):
        print "Lista Clicada"
        self.__index = index
        
    def getItem(self):
        return self.__model.itemFromIndex(self.__index)
        
    def getModel(self):
        return self.__model

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "SERVERS", None))
        
    def add(self, text):
        item= QStandardItem(text)
        self.__model.appendRow(item)
        

