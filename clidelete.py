# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clidelete.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
conn = sqlite3.connect('Users.db',timeout=10)
class Ui_Dialogc(object):

    def successful(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Client Deleted Successfuly")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def currusr(self):
        while 1:
            with open('is_logedin.txt') as f:
                data = [line.split() for line in f.readlines()]
                for i in data:
                    self.lguser = i[0]
                return self.lguser

    def listclid(self):
        owner = self.currusr()
        clients = conn.execute("SELECT * FROM clientsreg WHERE owner = :owner",{'owner':owner})
        count = 0
        for col in clients.fetchall():
            count = +1
            # print(col)
            self.comboBoxs.addItem(str(col[0]),[count])

    def sttxt(self):
        cid = self.comboBoxs.currentText()
        clients = conn.execute("SELECT c_name FROM clientsreg WHERE name_id = :name_id", {'name_id': cid})
        for c_name in clients.fetchall():
            for i in c_name:
                self.lineEditcl.clear()
                self.lineEditcl.setText(i)


    def deleteclient(self):
        clid = self.comboBoxs.currentText()
        dlt = conn.execute("DELETE FROM clientsreg WHERE name_id = :name_id ",{'name_id': clid})
        conn.commit()
        self.successful()
        self.comboBoxs.clear()
        self.listclid()

    def setupUi(self, Dialogc):
        Dialogc.setObjectName("Dialogc")
        Dialogc.resize(487, 63)
        self.toolButtondel = QtWidgets.QToolButton(Dialogc)
        self.toolButtondel.setGeometry(QtCore.QRect(390, 20, 31, 26))
        self.toolButtondel.setStyleSheet("image: url(:/tst-imgs/remove.png);")
        self.toolButtondel.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tst-imgs/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtondel.setIcon(icon)
        self.toolButtondel.setObjectName("toolButtondel")
        self.toolButtondel.clicked.connect(self.deleteclient)
        self.comboBoxs = QtWidgets.QComboBox(Dialogc)
        self.comboBoxs.setGeometry(QtCore.QRect(10, 20, 141, 28))
        self.comboBoxs.setObjectName("comboBoxs")
        self.comboBoxs.currentTextChanged.connect(self.sttxt)
        self.lineEditcl = QtWidgets.QLineEdit(Dialogc)
        self.lineEditcl.setGeometry(QtCore.QRect(170, 20, 201, 28))
        self.lineEditcl.setObjectName("lineEditcl")
        self.lineEditcl.setEnabled(False)
        self.toolButtondel_2 = QtWidgets.QToolButton(Dialogc)
        self.toolButtondel_2.setGeometry(QtCore.QRect(430, 20, 31, 26))
        self.toolButtondel_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Actions-dialog-close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtondel_2.setIcon(icon1)
        self.toolButtondel_2.setObjectName("toolButtondel_2")
        self.toolButtondel_2.clicked.connect(Dialogc.close)
        self.listclid()


        self.retranslateUi(Dialogc)
        QtCore.QMetaObject.connectSlotsByName(Dialogc)

    def retranslateUi(self, Dialogc):
        _translate = QtCore.QCoreApplication.translate
        Dialogc.setWindowTitle(_translate("Dialogc", "Delete clients"))

import imgs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialogc = QtWidgets.QDialog()
    ui = Ui_Dialogc()
    ui.setupUi(Dialogc)
    Dialogc.show()
    sys.exit(app.exec_())

