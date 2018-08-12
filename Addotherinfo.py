# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Addotherinfo.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addother(object):
    def setupUi(self, addother):
        addother.setObjectName("addother")
        addother.resize(527, 193)
        self.cliname = QtWidgets.QLabel(addother)
        self.cliname.setGeometry(QtCore.QRect(9, 9, 81, 18))
        self.cliname.setObjectName("cliname")
        self.groupBoxother = QtWidgets.QGroupBox(addother)
        self.groupBoxother.setGeometry(QtCore.QRect(10, 60, 503, 101))
        self.groupBoxother.setObjectName("groupBoxother")
        self.horizontalWidgetother = QtWidgets.QWidget(self.groupBoxother)
        self.horizontalWidgetother.setGeometry(QtCore.QRect(10, 30, 491, 80))
        self.horizontalWidgetother.setObjectName("horizontalWidgetother")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidgetother)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.desc = QtWidgets.QLineEdit(self.horizontalWidgetother)
        self.desc.setObjectName("desc")
        self.horizontalLayout.addWidget(self.desc)
        self.data = QtWidgets.QLineEdit(self.horizontalWidgetother)
        self.data.setObjectName("data")
        self.horizontalLayout.addWidget(self.data)
        self.toolButtonsave = QtWidgets.QToolButton(self.horizontalWidgetother)
        self.toolButtonsave.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tst-imgs/if_ok-sign_173063.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonsave.setIcon(icon)
        self.toolButtonsave.setIconSize(QtCore.QSize(18, 18))
        self.toolButtonsave.setObjectName("toolButtonsave")
        self.horizontalLayout.addWidget(self.toolButtonsave)

        self.retranslateUi(addother)
        QtCore.QMetaObject.connectSlotsByName(addother)

    def retranslateUi(self, addother):
        _translate = QtCore.QCoreApplication.translate
        addother.setWindowTitle(_translate("addother", "Other Information"))
        self.cliname.setText(_translate("addother", "Client Name"))
        self.groupBoxother.setTitle(_translate("addother", "Other Information"))
        self.desc.setText(_translate("addother", "Enter Description"))
        self.data.setText(_translate("addother", "Enter Data"))

import imgs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addother = QtWidgets.QWidget()
    ui = Ui_addother()
    ui.setupUi(addother)
    addother.show()
    sys.exit(app.exec_())

