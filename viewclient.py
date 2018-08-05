# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewclient.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
conn = sqlite3.connect('Users.db',timeout=10)

class Ui_Form(object):

    def filterdata(self):
        self.cliinfo.clear()
        self.cliinfo.setHorizontalHeaderLabels(
            ["Name_id ", "Name", "Mobile", "Pan", "GSTN", "DOB", "IT_paswd", "Tan", "Traces", "GSTN_paswd", "Owner"])
        self.cliinfo.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.cliinfo.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.cliinfo.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.cliinfo.horizontalHeaderItem(3).setToolTip("Column 4 ")
        self.cliinfo.horizontalHeaderItem(4).setToolTip("Column 5 ")
        self.cliinfo.horizontalHeaderItem(5).setToolTip("Column 6 ")
        self.cliinfo.horizontalHeaderItem(6).setToolTip("Column 7 ")
        self.cliinfo.horizontalHeaderItem(7).setToolTip("Column 8 ")
        self.cliinfo.horizontalHeaderItem(8).setToolTip("Column 9 ")
        self.cliinfo.horizontalHeaderItem(9).setToolTip("Column 10 ")
        self.cliinfo.horizontalHeaderItem(10).setToolTip("Column 11 ")
        cid = cid = self.comboBoxv.currentText()
        owner = self.currusr()
        result = conn.execute("SELECT * FROM clientsreg WHERE name_id = :name_id", {'name_id': cid})
        self.cliinfo.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.cliinfo.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.cliinfo.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        otinf = conn.execute("SELECT * FROM otherinfo WHERE name_id = :name_id", {'name_id': cid})
        self.otherinfo.clear()
        self.otherinfo.setVisible(True)
        self.otherinfo.setRowCount(1000)
        self.otherinfo.setColumnCount(3)
        self.otherinfo.setHorizontalHeaderLabels([ "Description", "Data","Name_id "])
        self.otherinfo.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.otherinfo.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.otherinfo.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.otherinfo.setRowCount(0)
        for row_number, row_data in enumerate(otinf):
            self.otherinfo.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.otherinfo.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



    def PullData(self):
        self.cliinfo.clear()
        self.cliinfo.setHorizontalHeaderLabels(
            ["Name_id ", "Name", "Mobile", "Pan", "GSTN", "DOB", "IT_paswd", "Tan", "Traces", "GSTN_paswd", "Owner"])
        self.cliinfo.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.cliinfo.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.cliinfo.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.cliinfo.horizontalHeaderItem(3).setToolTip("Column 4 ")
        self.cliinfo.horizontalHeaderItem(4).setToolTip("Column 5 ")
        self.cliinfo.horizontalHeaderItem(5).setToolTip("Column 6 ")
        self.cliinfo.horizontalHeaderItem(6).setToolTip("Column 7 ")
        self.cliinfo.horizontalHeaderItem(7).setToolTip("Column 8 ")
        self.cliinfo.horizontalHeaderItem(8).setToolTip("Column 9 ")
        self.cliinfo.horizontalHeaderItem(9).setToolTip("Column 10 ")
        self.cliinfo.horizontalHeaderItem(10).setToolTip("Column 11 ")
        owner = self.currusr()
        result = conn.execute("SELECT * FROM clientsreg WHERE owner = :owner",{'owner':owner})
        self.cliinfo.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.cliinfo.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.cliinfo.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

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
    def sttxt(self):
        cid = self.comboBoxv.currentText()
        clients = conn.execute("SELECT c_name FROM clientsreg WHERE name_id = :name_id", {'name_id': cid})
        for c_name in clients.fetchall():
            for i in c_name:
                self.lineEditv.clear()
                self.lineEditv.setText(i)
    def listclid(self):
        owner = self.currusr()
        clients = conn.execute("SELECT * FROM clientsreg WHERE owner = :owner",{'owner':owner})
        count = 0
        for col in clients.fetchall():
            count = +1
            # print(col)
            self.comboBoxv.addItem(str(col[0]),[count])

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 480)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.cliinfo = QtWidgets.QTableWidget(Form)
        self.cliinfo.setRowCount(0)
        self.cliinfo.setObjectName("cliinfo")
        self.cliinfo.setColumnCount(0)
        self.gridLayout.addWidget(self.cliinfo, 1, 0, 1, 4)
        self.lineEditv = QtWidgets.QLineEdit(Form)
        self.lineEditv.setObjectName("lineEditv")
        self.gridLayout.addWidget(self.lineEditv, 0, 1, 1, 1)
        self.otherinfo = QtWidgets.QTableWidget(Form)
        self.otherinfo.setObjectName("otherinfo")
        self.otherinfo.setColumnCount(0)
        self.otherinfo.setRowCount(0)
        self.otherinfo.setVisible(False)
        self.gridLayout.addWidget(self.otherinfo, 2, 0, 1, 4)
        self.comboBoxv = QtWidgets.QComboBox(Form)
        self.comboBoxv.setObjectName("comboBoxv")
        self.comboBoxv.currentTextChanged.connect(self.sttxt)
        self.gridLayout.addWidget(self.comboBoxv, 0, 0, 1, 1)
        self.toolButtonopen = QtWidgets.QToolButton(Form)
        self.toolButtonopen.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tst-imgs/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonopen.setIcon(icon)
        self.toolButtonopen.setObjectName("toolButtonopen")
        self.toolButtonopen.clicked.connect(self.filterdata)
        self.gridLayout.addWidget(self.toolButtonopen, 0, 2, 1, 1)
        self.toolButtonclose = QtWidgets.QToolButton(Form)
        self.toolButtonclose.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tst-imgs/Actions-dialog-close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonclose.setIcon(icon1)
        self.toolButtonclose.setObjectName("toolButtonclose")
        self.toolButtonclose.clicked.connect(Form.close)
        self.gridLayout.addWidget(self.toolButtonclose, 0, 3, 1, 1)
        self.cliinfo.setRowCount(1000)
        self.cliinfo.setColumnCount(11)
        self.listclid()
        self.PullData()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ViewClients"))
        self.toolButtonopen.setToolTip(_translate("Form", "view"))
        self.toolButtonclose.setToolTip(_translate("Form", "close"))

import imgs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

