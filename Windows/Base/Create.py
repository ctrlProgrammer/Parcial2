# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Create.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Create(object):
    def setupUi(self, Create):
        Create.setObjectName("Create")
        Create.resize(262, 585)
        self.centralwidget = QtWidgets.QWidget(Create)
        self.centralwidget.setObjectName("centralwidget")
        self.AceptarInfoV = QtWidgets.QPushButton(self.centralwidget)
        self.AceptarInfoV.setGeometry(QtCore.QRect(10, 500, 75, 23))
        self.AceptarInfoV.setObjectName("AceptarInfoV")
        self.CancelarInfoV = QtWidgets.QPushButton(self.centralwidget)
        self.CancelarInfoV.setGeometry(QtCore.QRect(90, 500, 75, 23))
        self.CancelarInfoV.setObjectName("CancelarInfoV")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 0, 241, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 239, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        Create.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Create)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 262, 26))
        self.menubar.setObjectName("menubar")
        Create.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Create)
        self.statusbar.setObjectName("statusbar")
        Create.setStatusBar(self.statusbar)

        self.retranslateUi(Create)
        QtCore.QMetaObject.connectSlotsByName(Create)

    def retranslateUi(self, Create):
        _translate = QtCore.QCoreApplication.translate
        Create.setWindowTitle(_translate("Create", "Create"))
        self.AceptarInfoV.setText(_translate("Create", "Aceptar"))
        self.CancelarInfoV.setText(_translate("Create", "Cancelar"))
