# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ESCOLA\QUARTO_PERIODO\PROGRAMAÇÃO ORIENTADA A OBJETOS II\Projetos\Projeto\PROJETO_POO\PROJETO_POO\TELA_LISTA_FILMES.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Lista_Filmes(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(739, 561)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 510, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(10, 120, 721, 371))
        self.listView.setObjectName("listView")
        
        # Defina a edição para NoEditTriggers
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 90, 117, 16))
        self.label_2.setObjectName("label_2")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 10, 178, 48))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_4.setText(_translate("Dialog", "VOLTAR"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">FILMES</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">CINEPLUS</span></p></body></html>"))

