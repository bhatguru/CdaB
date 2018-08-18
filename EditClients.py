# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditClients.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from clientupdate import *
from Addotherinfo import *
from PyQt5.QtWidgets import QMessageBox
import sqlite3
conn = sqlite3.connect('Users.db')

class Ui_Formedit(object):

    def curr_cli(self):
        lgd = [self.lineEditedit.text(), self.comboBoxedit.currentText()]
        itms = (lgd[0], lgd[1])
        with open('curr_cli.txt','w') as f:
            f.write(str(itms))

    def currusr(self):
        while 1:
            with open('is_logedin.txt') as f:
                data = [line.split() for line in f.readlines()]
                for i in data:
                    self.lguser = i[0]
                return self.lguser

    def sttxt(self):
        cid = self.comboBoxedit.currentText()
        clients = conn.execute("SELECT c_name FROM clientsreg WHERE name_id = :name_id", {'name_id': cid})
        for c_name in clients.fetchall():
            for i in c_name:
                self.lineEditedit.clear()
                self.lineEditedit.setText(i)

    def listclid(self):
        owner = self.currusr()
        clients = conn.execute("SELECT * FROM clientsreg WHERE owner = :owner",{'owner':owner})
        count = 0
        for col in clients.fetchall():
            count = +1
            # print(col)
            self.comboBoxedit.addItem(str(col[0]),[count])

    def ClientUpdate(self):
        self.clu = QtWidgets.QWidget()
        self.clu.ui = Ui_Update()
        self.clu.ui.setupUi(self.clu)
        self.clu.show()

    def AddOtherInfo(self):
        self.oth = QtWidgets.QWidget()
        self.oth.ui = Ui_addother()
        self.oth.ui.setupUi(self.oth)
        self.oth.show()

    def successful(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Client Deleted Successfuly")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def deleteclient(self):
        clid = self.lineEditedit.text()
        dlt = conn.execute("DELETE FROM clientsreg WHERE name_id = :name_id ",{'name_id': clid})
        conn.commit()
        self.successful()
        self.comboBoxedit.clear()
        self.lineEditedit.clear()
        self.listclid()
        self.sttxt()




    def setupUi(self, Formedit):
        Formedit.setObjectName("Formedit")
        Formedit.resize(432, 79)
        self.gridLayout = QtWidgets.QGridLayout(Formedit)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxedit = QtWidgets.QComboBox(Formedit)
        self.comboBoxedit.setObjectName("comboBoxedit")
        self.comboBoxedit.currentTextChanged.connect(self.sttxt)
        self.gridLayout.addWidget(self.comboBoxedit, 0, 0, 1, 1)
        self.lineEditedit = QtWidgets.QLineEdit(Formedit)
        self.lineEditedit.setObjectName("lineEditedit")
        self.gridLayout.addWidget(self.lineEditedit, 0, 1, 1, 1)
        self.update = QtWidgets.QToolButton(Formedit)
        self.update.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tst-imgs/if_Update_100114.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update.setIcon(icon)
        self.update.setIconSize(QtCore.QSize(18, 18))
        self.update.setObjectName("update")
        self.update.clicked.connect(self.ClientUpdate)
        self.gridLayout.addWidget(self.update, 0, 2, 1, 1)
        self.delete_2 = QtWidgets.QToolButton(Formedit)
        self.delete_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tst-imgs/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_2.setIcon(icon1)
        self.delete_2.setIconSize(QtCore.QSize(18, 18))
        self.delete_2.setObjectName("delete_2")
        self.delete_2.clicked.connect(self.deleteclient)
        self.gridLayout.addWidget(self.delete_2, 0, 3, 1, 1)
        self.addotherinfo = QtWidgets.QToolButton(Formedit)
        self.addotherinfo.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tst-imgs/if_Add_create_new_more_plus_1886085.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addotherinfo.setIcon(icon2)
        self.addotherinfo.setIconSize(QtCore.QSize(18, 18))
        self.addotherinfo.setObjectName("addotherinfo")
        self.addotherinfo.clicked.connect(self.AddOtherInfo)
        self.gridLayout.addWidget(self.addotherinfo, 0, 4, 1, 1)
        self.close = QtWidgets.QToolButton(Formedit)
        self.close.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tst-imgs/Actions-dialog-close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon3)
        self.close.setIconSize(QtCore.QSize(18, 18))
        self.close.setObjectName("close")
        self.close.clicked.connect(Formedit.close)
        self.gridLayout.addWidget(self.close, 0, 5, 1, 1)
        self.listclid()
        self.curr_cli()

        self.retranslateUi(Formedit)
        QtCore.QMetaObject.connectSlotsByName(Formedit)

    def retranslateUi(self, Formedit):
        _translate = QtCore.QCoreApplication.translate
        Formedit.setWindowTitle(_translate("Formedit", "Edit_Clients"))
        self.comboBoxedit.setToolTip(_translate("Formedit", "client id"))
        self.lineEditedit.setToolTip(_translate("Formedit", "client name"))
        self.update.setToolTip(_translate("Formedit", "Update"))
        self.delete_2.setToolTip(_translate("Formedit", "Delete"))
        self.addotherinfo.setToolTip(_translate("Formedit", "Add Other Info"))
        self.close.setToolTip(_translate("Formedit", "Close"))

import imgs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Formedit = QtWidgets.QWidget()
    ui = Ui_Formedit()
    ui.setupUi(Formedit)
    Formedit.show()
    sys.exit(app.exec_())

