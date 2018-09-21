# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usrmgmt.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox
import os
from login import *
from changepassword import *
import sqlite3
conn = sqlite3.connect('Users.db',timeout=10)
class Ui_Usermgmt(object):
    def changepasswd(self):
        self.chp = QtWidgets.QWidget()
        self.chp.ui = Ui_changepassword()
        self.chp.ui.setupUi(self.chp)
        self.chp.show()

    def deleteusr(self):
        self.delu = UApp()
        usrname = self.mgmtcomboBox.currentText()
        with open('delu.txt', 'w') as f:
            f.write(usrname)
            self.mgmtcomboBox.clear()
            self.scusers()

    def scusers(self):
        usrs = conn.execute("SELECT * FROM USERS")
        count = 0
        for col in usrs:
            count = +1
            self.mgmtcomboBox.addItem(col[0],[count])

    def whois(self):
        with open('is_logedin.txt') as f:
            data = [line.split() for line in f.readlines()]
            logedinuser = data[0]
            admin = ['vinay']
        if logedinuser == admin:
            self.mgmtcomboBox.setDisabled(False)
            self.mgmtremove.setDisabled(False)


    def setupUi(self, Usermgmt):
        Usermgmt.setObjectName("Usermgmt")
        Usermgmt.resize(443, 89)
        self.gridWidget = QtWidgets.QWidget(Usermgmt)
        self.gridWidget.setGeometry(QtCore.QRect(0, 20, 441, 51))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mgmtcomboBox = QtWidgets.QComboBox(self.gridWidget)
        self.mgmtcomboBox.setObjectName("mgmtcomboBox")
        self.mgmtcomboBox.setDisabled(True)
        self.gridLayout.addWidget(self.mgmtcomboBox, 0, 6, 1, 1)
        self.mgmtremove = QtWidgets.QToolButton(self.gridWidget)
        self.mgmtremove.setStyleSheet("")
        self.mgmtremove.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tst-imgs/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mgmtremove.setIcon(icon)
        self.mgmtremove.setObjectName("mgmtremove")
        self.mgmtremove.clicked.connect(self.deleteusr)
        self.mgmtremove.setDisabled(True)
        self.gridLayout.addWidget(self.mgmtremove, 0, 8, 1, 1)
        self.mgmtupdate = QtWidgets.QToolButton(self.gridWidget)
        self.mgmtupdate.setStyleSheet("")
        self.mgmtupdate.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tst-imgs/Apps-system-software-update-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mgmtupdate.setIcon(icon1)
        self.mgmtupdate.setObjectName("mgmtupdate")
        self.mgmtupdate.clicked.connect(self.changepasswd)
        self.gridLayout.addWidget(self.mgmtupdate, 0, 9, 1, 1)
        self.whois()
        self.scusers()

        self.retranslateUi(Usermgmt)
        QtCore.QMetaObject.connectSlotsByName(Usermgmt)

    def retranslateUi(self, Usermgmt):
        _translate = QtCore.QCoreApplication.translate
        Usermgmt.setWindowTitle(_translate("Usermgmt", "UserMgmt"))

import imgs

class UApp(QWidget):
    def __init__(self):
        super().__init__()
        buttonReply = QMessageBox.question(self, 'Important!!', "Do you like to Delete?", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            usrname = self.delu()
            if usrname != 'vinay':
                dlt = conn.execute("DELETE FROM USERS WHERE Username = :uname ", {'uname': usrname})
                conn.commit()
                self.successful()
        else:
            pass

    def delu(self):
        while 1:
            with open('delu.txt') as f:
                data = [line.split() for line in f.readlines()]
                for i in data:
                    self.dun = i[0]
                return self.dun

    def successful(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("User Deleted Successfuly")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Usermgmt = QtWidgets.QDialog()
    ui = Ui_Usermgmt()
    ui.setupUi(Usermgmt)
    Usermgmt.show()
    sys.exit(app.exec_())

