# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ESCOLA\QUARTO_PERIODO\PROGRAMAÇÃO ORIENTADA A OBJETOS II\Projetos\Projeto\PROJETO_POO\PROJETO_POO\TELA_GERENCIAMENTO.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class LOGIN_FUNC(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(800, 600))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(330, 280, 181, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 560, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(330, 91, 178, 48))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 171, 93, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(420, 210, 151, 21))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 210, 91, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "RELATORIO DE VENDAS"))
        self.pushButton_2.setText(_translate("Dialog", "GESTAO DE FILMES"))
        self.pushButton_4.setText(_translate("Dialog", "VOLTAR"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">CINEPLUS</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Gerente</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "BEM VINDO(A): "))
