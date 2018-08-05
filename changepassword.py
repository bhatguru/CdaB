# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepassword.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
conn = sqlite3.connect('Users.db')
from screen import *
class Ui_changepassword(object):

    def successful(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Password Changed Successfuly")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def updatepassword(self):
        newp = self.cnchnewpwd.text()
        usrname = self.usernamecombo.currentText()
        updt = conn.execute("UPDATE USERS SET Password = :password WHERE Username = :uname ",{'password': newp, 'uname': usrname})
        conn.commit()
        self.successful()
        self.choldpawd.clear()
        self.chnewpwd.clear()
        self.cnchnewpwd.clear()
        self.choldpawd.setDisabled(True)
        self.chnewpwd.setDisabled(True)
        self.cnchnewpwd.setDisabled(True)



    def chngbtndsbl(self):
        if self.chnewpwd.text() == self.cnchnewpwd.text():
            self.changepwd.setDisabled(False)
        else:
            self.changepwd.setDisabled(True)
    def pvalid(self):
        if self.chnewpwd.text() > str(0):
            self.cnchnewpwd.setDisabled(False)
        else:
            self.cnchnewpwd.setDisabled(True)
    def oldpvalidate(self):
        uname = self.usernamecombo.currentText()
        old = conn.execute("SELECT Password FROM USERS WHERE Username = ?",(uname,))
        for i in old:
            oldp = i[0]
        oldps = self.choldpawd.text()
        if oldps != oldp:
            self.chnewpwd.setDisabled(True)
        else:
            self.chnewpwd.setDisabled(False)

    def scusers(self):
            self.usernamecombo.addItem(self.currtusr())
    def currtusr(self):
        while 1:
            with open('is_logedin.txt') as f:
                data = [line.split() for line in f.readlines()]
                for i in data:
                    self.lguser = i[0]
                    return self.lguser

    def setupUi(self, changepassword):
        changepassword.setObjectName("changepassword")
        width, height = resolution()
        changepassword.resize(width, height)
        self.signupwidget = QtWidgets.QWidget(changepassword)
        self.signupwidget.setGeometry(QtCore.QRect(width/2.5, 120, 291, 331))
        self.signupwidget.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.signupwidget.setObjectName("signupwidget")
        self.signuplabel = QtWidgets.QLabel(self.signupwidget)
        self.signuplabel.setGeometry(QtCore.QRect(80, 10, 141, 111))
        self.signuplabel.setStyleSheet("border-image: url(:/tst-imgs/large-icon-user.png);")
        self.signuplabel.setText("")
        self.signuplabel.setObjectName("signuplabel")
        self.signuplabel.raise_()
        self.formWidget = QtWidgets.QWidget(changepassword)
        self.formWidget.setGeometry(QtCore.QRect(width/2.45, 270, 261, 171))
        self.formWidget.setObjectName("formWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.choldpawd = QtWidgets.QLineEdit(self.formWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.choldpawd.setPalette(palette)
        self.choldpawd.setAutoFillBackground(False)
        self.choldpawd.setStyleSheet("")
        self.choldpawd.textChanged.connect(self.oldpvalidate)
        self.choldpawd.setEchoMode(QtWidgets.QLineEdit.Password)
        pswd_regex = QtCore.QRegExp('[A-Za-z0-9@#$%^&+=]{8,}')
        validator = QtGui.QRegExpValidator(pswd_regex)
        self.choldpawd.setValidator(validator)
        self.choldpawd.setObjectName("choldpawd")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.choldpawd)
        self.chnewpwd = QtWidgets.QLineEdit(self.formWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.chnewpwd.setPalette(palette)
        self.chnewpwd.setAutoFillBackground(False)
        self.chnewpwd.setStyleSheet("")
        pwd_regex1 = QtCore.QRegExp('[A-Za-z0-9@#$%^&+=]{8,}')
        validator = QtGui.QRegExpValidator(pwd_regex1)
        self.chnewpwd.setValidator(validator)
        self.chnewpwd.setObjectName("chnewpwd")
        self.chnewpwd.setDisabled(True)
        self.chnewpwd.textChanged.connect(self.pvalid)
        self.chnewpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chnewpwd)
        self.cnchnewpwd = QtWidgets.QLineEdit(self.formWidget)
        self.cnchnewpwd.setObjectName("cnchnewpwd")
        pwd_regex2 = QtCore.QRegExp('[A-Za-z0-9@#$%^&+=]{8,}')
        validator = QtGui.QRegExpValidator(pwd_regex2)
        self.cnchnewpwd.setValidator(validator)
        self.cnchnewpwd.setDisabled(True)
        self.cnchnewpwd.textChanged.connect(self.chngbtndsbl)
        self.cnchnewpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cnchnewpwd)
        self.changepwd = QtWidgets.QPushButton(self.formWidget)
        self.changepwd.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.changepwd.setObjectName("changepwd")
        self.changepwd.setDisabled(True)
        self.changepwd.clicked.connect(self.updatepassword)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.changepwd)
        self.usernamecombo = QtWidgets.QComboBox(self.formWidget)
        self.usernamecombo.setObjectName("usernamecombo")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernamecombo)
        self.scusers()

        self.retranslateUi(changepassword)
        QtCore.QMetaObject.connectSlotsByName(changepassword)

    def retranslateUi(self, changepassword):
        _translate = QtCore.QCoreApplication.translate
        changepassword.setWindowTitle(_translate("changepassword", "change password"))
        self.choldpawd.setPlaceholderText(_translate("changepassword", "Old Password"))
        self.chnewpwd.setPlaceholderText(_translate("changepassword", "New Password"))
        self.cnchnewpwd.setPlaceholderText(_translate("changepassword", "Confirm Password"))
        self.changepwd.setText(_translate("changepassword", "Change"))

import imgs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changepassword = QtWidgets.QWidget()
    ui = Ui_changepassword()
    ui.setupUi(changepassword)
    changepassword.show()
    sys.exit(app.exec_())

