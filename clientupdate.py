# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientupdate.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
conn = sqlite3.connect('Users.db',timeout=10)
class Ui_Update(object):

    # def check(self):
    #     if self.is_selected() != "empty" and self.updatevalue.text() != str(0):
    #         self.updatebtn.setDisabled(False)

    def UpdateData(self):
        c_name, name_id = self.read_cli()
        slctd = self.is_selected()
        if slctd == 'tan':
            tan = self.updatevalue.text()
            updt = conn.execute("UPDATE clientsreg SET tan = :tan WHERE name_id = :name_id ",
                                {'tan': tan, 'name_id': name_id})
            conn.commit()
            self.successfull()
        elif slctd == 'gstn':
            gstn_paswd = self.updatevalue.text()
            updt = conn.execute("UPDATE clientsreg SET gstn_paswd = :gstn_paswd WHERE name_id = :name_id ",
                                {'gstn_paswd': gstn_paswd, 'name_id': name_id})
            conn.commit()
            self.successfull()
        else:
            traces = self.updatevalue.text()
            updt = conn.execute("UPDATE clientsreg SET traces = :traces WHERE name_id = :name_id ",
                                {'traces': traces, 'name_id': name_id})
            self.successfull()
            conn.commit()

    def successfull(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Information Updated Successfully")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def successful(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Please Check Radio Button to Update")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def is_selected(self):
        if self.gstn.isChecked() == True:
            self.updatevalue.setText("Enter New GSTN Password..")
            self.dt ="gstn"
            return self.dt
        elif self.tan.isChecked() == True:
            self.updatevalue.setText("Enter Tan Details")
            self.dt = "tan"
            return self.dt
        elif self.traces.isChecked() == True:
            self.updatevalue.setText("Enter Traces Details")
            self.dt = "traces"
            return self.dt
        else:
            self.successful()
            dt = "empty"
            return self.dt


    def read_cli(self):
        while 1:
            with open('curr_cli.txt') as f:
                data = [line.split() for line in f.readlines()]
                for i in data:
                    self.lgcli = i[0]
                    self.lgid = i[1]
                return self.lgcli, self.lgid


    def setupUi(self, Update):
        Update.setObjectName("Update")
        Update.resize(655, 168)
        self.gridLayout = QtWidgets.QGridLayout(Update)
        self.gridLayout.setObjectName("gridLayout")
        self.clientname = QtWidgets.QLabel(Update)
        self.clientname.setObjectName("clientname")
        self.gridLayout.addWidget(self.clientname, 0, 0, 1, 1)
        self.horizontalWidget = QtWidgets.QWidget(Update)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gstn = QtWidgets.QRadioButton(self.horizontalWidget)
        self.gstn.setObjectName("gstn")
        self.horizontalLayout.addWidget(self.gstn)
        self.tan = QtWidgets.QRadioButton(self.horizontalWidget)
        self.tan.setObjectName("tan")
        self.horizontalLayout.addWidget(self.tan)
        self.traces = QtWidgets.QRadioButton(self.horizontalWidget)
        self.traces.setObjectName("traces")
        self.horizontalLayout.addWidget(self.traces)
        self.okbtn = QtWidgets.QToolButton(self.horizontalWidget)
        self.okbtn.setText("")
        self.okbtn.clicked.connect(self.is_selected)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tst-imgs/if_ok-sign_173063.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.okbtn.setIcon(icon)
        self.okbtn.setIconSize(QtCore.QSize(18, 18))
        self.okbtn.setObjectName("okbtn")
        self.horizontalLayout.addWidget(self.okbtn)
        self.gridLayout.addWidget(self.horizontalWidget, 1, 0, 1, 1)
        self.horizontalWidget1 = QtWidgets.QWidget(Update)
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.updatevalue = QtWidgets.QLineEdit(self.horizontalWidget1)
        self.updatevalue.setObjectName("updatevalue")
        self.horizontalLayout_2.addWidget(self.updatevalue)
        self.updatebtn = QtWidgets.QToolButton(self.horizontalWidget1)
        self.updatebtn.setText("")
        self.updatebtn.clicked.connect(self.UpdateData)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tst-imgs/if_Update_100114.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updatebtn.setIcon(icon1)
        self.updatebtn.setIconSize(QtCore.QSize(18, 18))
        self.updatebtn.setObjectName("updatebtn")
        # self.updatebtn.setDisabled(True)
        self.horizontalLayout_2.addWidget(self.updatebtn)
        self.gridLayout.addWidget(self.horizontalWidget1, 2, 0, 1, 1)
        self.horizontalWidget.raise_()
        name,name_id = self.read_cli()
        self.clientname.setText(name)
        # self.check()
        self.clientname.raise_()


        self.retranslateUi(Update)
        QtCore.QMetaObject.connectSlotsByName(Update)

    def retranslateUi(self, Update):
        _translate = QtCore.QCoreApplication.translate
        Update.setWindowTitle(_translate("Update", "Update"))
        # self.clientname.setText(_translate("Update", "client_name"))
        self.gstn.setText(_translate("Update", "GSTN_PASSWORD"))
        self.tan.setText(_translate("Update", "TAN"))
        self.traces.setText(_translate("Update", "TRACES"))
        self.okbtn.setToolTip(_translate("Update", "OK"))
        self.updatevalue.setToolTip(_translate("Update", "Enter value to update"))
        self.updatebtn.setToolTip(_translate("Update", "Update"))

import imgs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Update = QtWidgets.QWidget()
    ui = Ui_Update()
    ui.setupUi(Update)
    Update.show()
    sys.exit(app.exec_())

