# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from screen import *
from usrmgmt import *
class Ui_AssociateDataBase(object):
    def delfile(self):
        os.remove("is_logedin.txt")
    def useropen(self):
        self.usmgmt = QtWidgets.QDialog()
        self.usmgmt.ui = Ui_Usermgmt()
        self.usmgmt.ui.setupUi(self.usmgmt)
        self.usmgmt.show()

    def setupUi(self, AssociateDataBase):
        AssociateDataBase.setObjectName("AssociateDataBase")
        AssociateDataBase.resize(708, 480)
        self.centralwidget = QtWidgets.QWidget(AssociateDataBase)
        self.centralwidget.setObjectName("centralwidget")
        width, height = resolution()
        AssociateDataBase.resize(width, height)
        AssociateDataBase.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(width/2.6, 200, 321, 201))
        self.logo.setStyleSheet("border-image: url(:/tst-imgs/Client_list.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.mngusr = QtWidgets.QPushButton(self.centralwidget)
        self.mngusr.setGeometry(QtCore.QRect(20, 137, 41, 31))
        self.mngusr.setMaximumSize(QtCore.QSize(41, 31))
        self.mngusr.setStyleSheet("")
        self.mngusr.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tst-imgs/man.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mngusr.setIcon(icon)
        self.mngusr.setIconSize(QtCore.QSize(25, 25))
        self.mngusr.setObjectName("mngusr")
        self.mngusr.clicked.connect(self.useropen)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(20, 180, 41, 31))
        self.add.setStyleSheet("")
        self.add.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tst-imgs/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add.setIcon(icon1)
        self.add.setIconSize(QtCore.QSize(25, 25))
        self.add.setObjectName("add")
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setGeometry(QtCore.QRect(20, 220, 41, 31))
        self.remove.setStyleSheet("")
        self.remove.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tst-imgs/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon2)
        self.remove.setIconSize(QtCore.QSize(25, 25))
        self.remove.setObjectName("remove")
        self.view = QtWidgets.QPushButton(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(20, 260, 41, 31))
        self.view.setStyleSheet("")
        self.view.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tst-imgs/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view.setIcon(icon3)
        self.view.setIconSize(QtCore.QSize(25, 25))
        self.view.setObjectName("view")
        self.edit = QtWidgets.QPushButton(self.centralwidget)
        self.edit.setGeometry(QtCore.QRect(20, 300, 41, 31))
        self.edit.setStyleSheet("")
        self.edit.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/tst-imgs/contract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit.setIcon(icon4)
        self.edit.setIconSize(QtCore.QSize(25, 25))
        self.edit.setObjectName("edit")
        self.websurf = QtWidgets.QPushButton(self.centralwidget)
        self.websurf.setGeometry(QtCore.QRect(20, 340, 41, 31))
        self.websurf.setStyleSheet("")
        self.websurf.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/tst-imgs/internet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.websurf.setIcon(icon5)
        self.websurf.setIconSize(QtCore.QSize(25, 25))
        self.websurf.setObjectName("websurf")
        self.closewin = QtWidgets.QPushButton(self.centralwidget)
        self.closewin.setGeometry(QtCore.QRect(20, 100, 41, 31))
        self.closewin.setStyleSheet("")
        self.closewin.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/tst-imgs/Actions-dialog-close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closewin.setIcon(icon6)
        self.closewin.setIconSize(QtCore.QSize(25, 25))
        self.closewin.setObjectName("closewin")
        AssociateDataBase.setCentralWidget(self.centralwidget)

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

