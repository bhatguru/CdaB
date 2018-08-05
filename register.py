# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import sqlite3
from screen import resolution
conn = sqlite3.connect('Users.db',timeout=5.0)
class Ui_registerForm(object):
    def setupUi(self, registerForm):
        registerForm.setObjectName("registerForm")
        width, height = resolution()
        registerForm.resize(width, height)
        registerForm.setStyleSheet("selection-background-color: rgb(255, 255, 255);")
        self.regformwidget = QtWidgets.QWidget(registerForm)
        self.regformwidget.setGeometry(QtCore.QRect(width/2.45, 280, 261, 141))
        self.regformwidget.setObjectName("regformwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.regformwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.reguser = QtWidgets.QLineEdit(self.regformwidget)
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
        self.reguser.setPalette(palette)
        self.reguser.setAutoFillBackground(False)
        self.reguser.setStyleSheet("")
        self.reguser.setObjectName("reguser")
        self.reguser.setPlaceholderText("User Name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reguser)
        self.regpasswd = QtWidgets.QLineEdit(self.regformwidget)
        self.regpasswd.setObjectName("regpasswd")
        self.regpasswd.setPlaceholderText("Password")
        self.regpasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.regpasswd.textChanged.connect(self.passwordcheck)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.regpasswd)
        self.signup = QtWidgets.QPushButton(self.regformwidget)
        self.signup.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.signup.setText("Sign Up")
        self.signup.setObjectName("signup")
        self.signup.setDisabled(True)
        self.signup.clicked.connect(self.insertuser)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.signup)
        self.cregpaswd = QtWidgets.QLineEdit(self.regformwidget)
        self.cregpaswd.setObjectName("cregpaswd")
        self.cregpaswd.setPlaceholderText("Confirm Password")
        self.cregpaswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cregpaswd.textChanged.connect(self.passwordcheck)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cregpaswd)
        self.registerwidget = QtWidgets.QWidget(registerForm)
        self.registerwidget.setGeometry(QtCore.QRect(width/2.5, 100, 291, 331))
        self.registerwidget.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.registerwidget.setObjectName("registerwidget")
        self.reglabel = QtWidgets.QLabel(self.registerwidget)
        self.reglabel.setGeometry(QtCore.QRect(80, 40, 141, 111))
        self.reglabel.setStyleSheet("border-image: url(:/tst-imgs/large-icon-user.png);")
        self.reglabel.setText("")
        self.reglabel.setObjectName("reglabel")
        self.registerwidget.raise_()
        self.regformwidget.raise_()

    def insertuser(self):
        try:
            # print('button clicked')
            usrname = self.reguser.text()
            passwrd = self.cregpaswd.text()
            if usrname != 'vinay':
                conn.execute("INSERT INTO USERS VALUES(?,?)", (usrname, passwrd))
                conn.commit()
                conn.close()
                self.msgsuccessful()
                self.reguser.clear()
                self.regpasswd.clear()
                self.cregpaswd.clear()
        except:
            self.error()


    def txtempty(self):
        txtbx = [self.reguser.text(), self.regpasswd.text(), self.cregpaswd.text()]
        if txtbx[0] > str(0) and txtbx[1]> str(0) and txtbx[2]>str(0) :
            self.signup.setDisabled(False)
        else:
            self.signup.setDisabled(True)



    def passwordcheck(self):
        if self.regpasswd.text() == self.cregpaswd.text() and self.reguser.text() > str(0):
            self.signup.setDisabled(False)
        else:
            self.signup.setDisabled(True)

    def error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Username Already Exists")
        msg.setStandardButtons(QMessageBox.Ok)
        self.reguser.clear()
        self.regpasswd.clear()
        self.cregpaswd.clear()
        msg.exec_()

    def msgsuccessful(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("User Registered Successfuly")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        self.retranslateUi(registerForm)
        QtCore.QMetaObject.connectSlotsByName(registerForm)

    def retranslateUi(self, registerForm):
        _translate = QtCore.QCoreApplication.translate
        registerForm.setWindowTitle(_translate("registerForm", "Register"))
        self.reguser.setPlaceholderText(_translate("registerForm", "User Name"))
        self.regpasswd.setPlaceholderText(_translate("registerForm", "Password"))
        self.signup.setText(_translate("registerForm", "Submit"))
        self.cregpaswd.setPlaceholderText(_translate("registerForm", "Confirm Password"))

import imgs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerForm = QtWidgets.QWidget()
    ui = Ui_registerForm()
    ui.setupUi(registerForm)
    registerForm.show()
    sys.exit(app.exec_())

