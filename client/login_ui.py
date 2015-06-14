# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Login(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)
		self.confirm = None

	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(426, 299)
		Dialog.setModal(True)
		self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
		self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
		self.verticalLayout_3 = QtGui.QVBoxLayout()
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.verticalLayout_2 = QtGui.QVBoxLayout()
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.label = QtGui.QLabel(Dialog)
		font = QtGui.QFont()
		font.setPointSize(24)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout.addWidget(self.label)
		spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem1)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem2)
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem3)
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.label_2 = QtGui.QLabel(Dialog)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.verticalLayout.addWidget(self.label_2)
		self.username = QtGui.QLineEdit(Dialog)
		self.username.setObjectName(_fromUtf8("username"))
		self.verticalLayout.addWidget(self.username)
		self.label_3 = QtGui.QLabel(Dialog)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.verticalLayout.addWidget(self.label_3)
		self.password = QtGui.QLineEdit(Dialog)
		self.password.setEchoMode(QtGui.QLineEdit.Password)
		self.password.setObjectName(_fromUtf8("password"))
		self.verticalLayout.addWidget(self.password)
		self.horizontalLayout_2.addLayout(self.verticalLayout)
		spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem4)
		self.horizontalLayout_2.setStretch(0, 2)
		self.horizontalLayout_2.setStretch(1, 4)
		self.horizontalLayout_2.setStretch(2, 2)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.verticalLayout_3.addLayout(self.verticalLayout_2)
		spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_3.addItem(spacerItem5)
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.verticalLayout_3.addWidget(self.buttonBox)
		self.verticalLayout_4.addLayout(self.verticalLayout_3)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Login", None))
		self.label.setText(_translate("Dialog", "LOGIN", None))
		self.label_2.setText(_translate("Dialog", "Username", None))
		self.label_3.setText(_translate("Dialog", "Password", None))





