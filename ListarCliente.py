# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListarCliente.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from clients import Clients

class Ui_ListarCliente(object):
    def setupUi(self, ListarCliente):
        ListarCliente.setObjectName("ListarCliente")
        ListarCliente.resize(604, 496)
        self.centralwidget = QtWidgets.QWidget(ListarCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 0, 461, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 461, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.DatosCliente = QtWidgets.QLabel(self.centralwidget)
        self.DatosCliente.setGeometry(QtCore.QRect(500, 10, 111, 51))
        self.DatosCliente.setObjectName("DatosCliente")
        self.No_ID = QtWidgets.QPushButton(self.centralwidget)
        self.No_ID.setGeometry(QtCore.QRect(500, 60, 75, 23))
        self.No_ID.setObjectName("No_ID")
        self.Nombre = QtWidgets.QPushButton(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(500, 100, 75, 23))
        self.Nombre.setObjectName("Nombre")
        self.Apellido = QtWidgets.QPushButton(self.centralwidget)
        self.Apellido.setGeometry(QtCore.QRect(500, 140, 75, 23))
        self.Apellido.setObjectName("Apellido")
        self.direccion = QtWidgets.QPushButton(self.centralwidget)
        self.direccion.setGeometry(QtCore.QRect(500, 180, 75, 23))
        self.direccion.setObjectName("direccion")
        self.Telefono = QtWidgets.QPushButton(self.centralwidget)
        self.Telefono.setGeometry(QtCore.QRect(500, 220, 75, 23))
        self.Telefono.setObjectName("Telefono")
        self.Ciudad = QtWidgets.QPushButton(self.centralwidget)
        self.Ciudad.setGeometry(QtCore.QRect(500, 260, 75, 23))
        self.Ciudad.setObjectName("Ciudad")
        self.CerrarLista = QtWidgets.QPushButton(self.centralwidget)
        self.CerrarLista.setGeometry(QtCore.QRect(500, 390, 75, 23))
        self.CerrarLista.setObjectName("CerrarLista")
        self.retranslateUi(ListarCliente)
        self.CerrarLista.clicked.connect(ListarCliente.close)
        QtCore.QMetaObject.connectSlotsByName(ListarCliente)
        ListarCliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListarCliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
        self.menubar.setObjectName("menubar")
        ListarCliente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListarCliente)
        self.statusbar.setObjectName("statusbar")
        ListarCliente.setStatusBar(self.statusbar)

        self.retranslateUi(ListarCliente)
        self.No_ID.clicked.connect(self.get_clients)
        QtCore.QMetaObject.connectSlotsByName(ListarCliente)

    def retranslateUi(self, ListarCliente):
        _translate = QtCore.QCoreApplication.translate
        ListarCliente.setWindowTitle(_translate("ListarCliente", "ListarCliente"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ListarCliente", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ListarCliente", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ListarCliente", "Apellido"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ListarCliente", "Dirección"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ListarCliente", "Teléfono"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ListarCliente", "Ciudad"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ListarCliente", "uid"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ListarCliente", "Random"))
        self.DatosCliente.setText(_translate("ListarCliente", "Ordenar Datos:"))
        self.No_ID.setText(_translate("ListarCliente", "No de ID"))
        self.Nombre.setText(_translate("ListarCliente", "Nombre"))
        self.Apellido.setText(_translate("ListarCliente", "Apellido"))
        self.direccion.setText(_translate("ListarCliente", "Direnccion"))
        self.Telefono.setText(_translate("ListarCliente", "Telefono"))
        self.Ciudad.setText(_translate("ListarCliente", "Ciudad"))
        self.CerrarLista.setText(_translate("ListarCliente", "Cerrar"))

    def get_clients(self, ListarCliente):
        clients=Clients()
        data =clients.get_all()
        row = 0
        for i in data:
            col = 0
            keys = i.keys()
            for j in keys:
                item = QtWidgets.QTableWidgetItem(str(i[j]))
                self.tableWidget.setItem(row, col, item)
                col+=1
            row +=1
