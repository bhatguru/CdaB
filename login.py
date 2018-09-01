# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from screen import *
from homepage import *
from register import *
class Ui_login_3(object):

    def is_logedin(self):
        lgd = str(self.loginuname.text())
        with open('is_logedin.txt','w') as f:
            f.write(lgd)

    def logincheck(self):
        usrname = self.loginuname.text()
        passwd = self.loginpwd.text()
        result = conn.execute(" SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (usrname, passwd))
        if (len(result.fetchall()) > 0):
            self.is_logedin()
            self.homeopen()
        else:
            self.InvalidInfo()
            self.loginuname.clear()
            self.loginpwd.clear()

    def Disabled(self):
        if self.loginuname.text() and self.loginpwd.text() != str(0):
            self.login.setDisabled(False)

    def InvalidInfo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Invalid Username or Password")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # def Nodata(self):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Critical)
    #     msg.setText("Please Enter User Name and Password")
    #     msg.setStandardButtons(QMessageBox.Ok)
    #     msg.exec_()

    def homeopen(self):
        self.hopen = QtWidgets.QMainWindow()
        self.hopen.ui = Ui_AssociateDataBase()
        self.hopen.ui.setupUi(self.hopen)
        self.hopen.show()


    def openreg(self):
        self.sigp = QtWidgets.QWidget()
        self.sigp.ui = Ui_registerForm()
        self.sigp.ui.setupUi(self.sigp)
        self.sigp.show()

    def setupUi(self, login_3):
        login_3.setObjectName("login_3")
        width, height = resolution()
        login_3.resize(width, height)
        login_3.setStyleSheet("")
        login_3.setWindowIcon(QtGui.QIcon("appicon.png"))
        self.signupwidget = QtWidgets.QWidget(login_3)
        self.signupwidget.setGeometry(QtCore.QRect(width/2.5, 100, 291, 331))
        self.signupwidget.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.signupwidget.setObjectName("signupwidget")
        self.signuplabel = QtWidgets.QLabel(self.signupwidget)
        self.signuplabel.setGeometry(QtCore.QRect(80, 40, 141, 111))
        self.signuplabel.setStyleSheet("border-image: url(:/tst-imgs/large-icon-user.png);")
        self.signuplabel.setText("")
        self.signuplabel.setObjectName("signuplabel")
        self.formWidget = QtWidgets.QWidget(login_3)
        self.formWidget.setGeometry(QtCore.QRect(width/2.45, 280, 261, 141))
        self.formWidget.setObjectName("formWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.loginuname = QtWidgets.QLineEdit(self.formWidget)
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
        self.loginuname.setPalette(palette)
        self.loginuname.setAutoFillBackground(False)
        self.loginuname.setStyleSheet("")
        self.loginuname.setObjectName("loginuname")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginuname)
        self.loginpwd = QtWidgets.QLineEdit(self.formWidget)
        self.loginpwd.setObjectName("signuppwd")
        self.loginpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.loginpwd)
        self.login = QtWidgets.QPushButton(self.formWidget)
        self.login.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.login.setObjectName("login")
        self.login.setDisabled(True)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.login)
        self.signup = QtWidgets.QPushButton(self.formWidget)
        self.signup.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.signup.setObjectName("signup")
        self.signup.clicked.connect(self.openreg)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.signup)
        self.loginuname.textChanged.connect(self.Disabled)
        self.loginpwd.textChanged.connect(self.Disabled)
        self.login.clicked.connect(self.logincheck)

        self.retranslateUi(login_3)
        QtCore.QMetaObject.connectSlotsByName(login_3)

    def retranslateUi(self, login_3):
        _translate = QtCore.QCoreApplication.translate
        login_3.setWindowTitle(_translate("login_3", "login"))
        self.loginuname.setPlaceholderText(_translate("login_3", "User Name"))
        self.loginpwd.setPlaceholderText(_translate("login_3", "Password"))
        self.login.setText(_translate("login_3", "Login"))
        self.signup.setText(_translate("login_3", "SignUp"))

import imgs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_3 = QtWidgets.QWidget()
    ui = Ui_login_3()
    ui.setupUi(login_3)
    login_3.show()
    sys.exit(app.exec_())

