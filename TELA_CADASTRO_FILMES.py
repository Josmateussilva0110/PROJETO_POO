# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TELA_CADASTRO_FILMES.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Cadastrar_filme(object):
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 110, 128, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(330, 60, 178, 48))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 560, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 540, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(350, 380, 111, 22))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(200, 440, 411, 91))
        self.listView.setObjectName("listView")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(199, 300, 201, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listView_2 = QtWidgets.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(418, 300, 191, 31))
        self.listView_2.setObjectName("listView_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 180, 409, 24))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 220, 409, 24))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 260, 409, 24))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(200, 340, 201, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 337, 171, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 410, 111, 22))
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CADASTRAR FILMES</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">CINEPLUS</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Dialog", "VOLTAR"))
        self.pushButton.setText(_translate("Dialog", "CADASTRAR"))
        self.comboBox.setCurrentText(_translate("Dialog", "2D"))
        self.comboBox.setItemText(0, _translate("Dialog", "2D"))
        self.comboBox.setItemText(1, _translate("Dialog", "3D"))
        self.pushButton_4.setText(_translate("Dialog", "selecione a classificação"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Nome do Filme"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Ano do Filme"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Preço"))
        self.pushButton_2.setText(_translate("Dialog", "Adicionar"))
        self.comboBox_2.setCurrentText(_translate("Dialog", "2D"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Dublado"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Legendado"))
