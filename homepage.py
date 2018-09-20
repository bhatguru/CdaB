# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from screen import *
from usrmgmt import *
from clientreg import *
from clidelete import *
from viewclient import *
from EditClients import *
class Ui_AssociateDataBase(object):
    def currusr(self):
        while 1:
            with open('is_logedin.txt') as f:
                data = [line.split() for line in f.readlines()]
                for i in data:
                    self.lguser = i[0]
                return self.lguser

    def useropen(self):
        self.usmgmt = QtWidgets.QDialog()
        self.usmgmt.ui = Ui_Usermgmt()
        self.usmgmt.ui.setupUi(self.usmgmt)
        self.usmgmt.show()

    def clidelopen(self):
        self.cld = QtWidgets.QDialog()
        self.cld.ui = Ui_Dialogc()
        self.cld.ui.setupUi(self.cld)
        self.cld.show()

    def ClientView(self):
        self.clv = QtWidgets.QDialog()
        self.clv.ui = Ui_Form()
        self.clv.ui.setupUi(self.clv)
        self.clv.show()


    def regcliopen(self):
        self.regcl = QtWidgets.QMainWindow()
        self.regcl.ui = Ui_RegisterClient()
        self.regcl.ui.setupUi(self.regcl)
        self.regcl.show()

    def editcliopen(self):
        self.edt = QtWidgets.QWidget()
        self.edt.ui = Ui_Formedit()
        self.edt.ui.setupUi(self.edt)
        self.edt.show()

    def setupUi(self, AssociateDataBase):
        AssociateDataBase.setObjectName("AssociateDataBase")
        width, height = resolution()
        AssociateDataBase.resize(width, height)
        self.centralwidget = QtWidgets.QWidget(AssociateDataBase)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(width/2.6, 200, 321, 201))
        self.logo.setStyleSheet("border-image: url(:/tst-imgs/Client_list.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.mngusr = QtWidgets.QPushButton(self.centralwidget)
        self.mngusr.setGeometry(QtCore.QRect(20, 87, 41, 31))
        self.mngusr.setMaximumSize(QtCore.QSize(41, 31))
        self.mngusr.setStyleSheet("")
        self.mngusr.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tst-imgs/man.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mngusr.setIcon(icon)
        self.mngusr.setIconSize(QtCore.QSize(25, 25))
        self.mngusr.setObjectName("mngusr")
        self.mngusr.setToolTip("User Management")
        self.mngusr.clicked.connect(self.useropen)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(20, 130, 41, 31))
        self.add.setStyleSheet("")
        self.add.setText("")
        self.add.setToolTip("Client Registration")
        self.add.clicked.connect(self.regcliopen)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tst-imgs/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add.setIcon(icon1)
        self.add.setIconSize(QtCore.QSize(25, 25))
        self.add.setObjectName("add")
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setGeometry(QtCore.QRect(20, 180, 41, 31))
        self.remove.setStyleSheet("")
        self.remove.setText("")
        self.remove.setToolTip("Remove Clients")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tst-imgs/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon2)
        self.remove.setIconSize(QtCore.QSize(25, 25))
        self.remove.setObjectName("remove")
        self.remove.clicked.connect(self.clidelopen)
        self.is_loged = QtWidgets.QLabel(self.centralwidget)
        self.is_loged.setGeometry(QtCore.QRect(width-100, 45, 100, 31))
        self.is_loged.setObjectName("adlable")
        self.view = QtWidgets.QPushButton(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(20, 220, 41, 31))
        self.view.setStyleSheet("")
        self.view.setText("")
        self.view.setToolTip("View Clients")
        self.view.clicked.connect(self.ClientView)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tst-imgs/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view.setIcon(icon3)
        self.view.setIconSize(QtCore.QSize(25, 25))
        self.view.setObjectName("view")
        self.edit = QtWidgets.QPushButton(self.centralwidget)
        self.edit.setGeometry(QtCore.QRect(20, 270, 41, 31))
        self.edit.setStyleSheet("")
        self.edit.setText("")
        self.edit.setToolTip("Edit Clients")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/tst-imgs/contract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit.setIcon(icon4)
        self.edit.setIconSize(QtCore.QSize(25, 25))
        self.edit.setObjectName("edit")
        self.edit.clicked.connect(self.editcliopen)
        AssociateDataBase.setCentralWidget(self.centralwidget)
        self.is_loged.setText(self.currusr())

        self.retranslateUi(AssociateDataBase)
        QtCore.QMetaObject.connectSlotsByName(AssociateDataBase)

    def retranslateUi(self, AssociateDataBase):
        _translate = QtCore.QCoreApplication.translate
        AssociateDataBase.setWindowTitle(_translate("AssociateDataBase", "Home"))

import imgs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AssociateDataBase = QtWidgets.QMainWindow()
    ui = Ui_AssociateDataBase()
    ui.setupUi(AssociateDataBase)
    AssociateDataBase.show()
    sys.exit(app.exec_())

