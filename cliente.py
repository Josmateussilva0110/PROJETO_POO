import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QInputDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QStringListModel
from tela_main_ui import *#
from TELA_CADASTRO_ui import *#
from TELA_USUARIO import *#
from TELA_GERENCIAMENTO import *#
from classes.funcoes_aux import *

ip = '192.168.1.6'
porta = 8007
nome ='Mateus'
addr = ((ip,porta))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(addr)
    client_socket.send(nome.encode())
except Exception as e:
    print(f'Ocorreu uma exceção: {e}')
    exit()


class Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()


        self.tela_main_ui = Ui_Dialog()
        self.tela_main_ui.setupUi(self.stack0)

        self.TELA_CADASTRO_ui = Cadastrar()
        self.TELA_CADASTRO_ui.setupUi(self.stack1)


        self.TELA_USUARIO = Tela_usuario()
        self.TELA_USUARIO.setupUi(self.stack2)


        #Usa-se só para ajustar essa tela
        self.TELA_DPS_LOGIN_FUNC_ui = LOGIN_FUNC()
        self.TELA_DPS_LOGIN_FUNC_ui.setupUi(self.stack3)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)


class Ui_Main(QMainWindow, Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)
        self.horarios_selecionados = list()
        self.classificacao = ''
        self.dados_clienete = list()
        self.dados_cliente_final = list()
        self.saida = None
    
        #tela principal
        self.tela_main_ui.pushButton_3.clicked.connect(self.fecharAplicacao)
        self.tela_main_ui.pushButton_4.clicked.connect(self.abrirTelaCadastro)
        self.tela_main_ui.pushButton.clicked.connect(self.botao_ok)

        #tela cadastro cliente
        self.TELA_CADASTRO_ui.pushButton_3.clicked.connect(self.VoltarMain)
        self.TELA_CADASTRO_ui.pushButton.clicked.connect(self.botao_Cadastra)

        ##TELA_CLIENTES
        #Tela dps de login (TELA CLIENTE)
        self.TELA_USUARIO.pushButton_4.clicked.connect(self.VoltarMain)
        #self.TELA_USUARIO.pushButton.clicked.connect(self.Tela_Cliente_Ver_Filmes)

        self.TELA_DPS_LOGIN_FUNC_ui.pushButton_4.clicked.connect(self.VoltarMain)
        #self.TELA_DPS_LOGIN_FUNC_ui.pushButton.clicked.connect(self.Tela_Estatistica)
        #self.TELA_DPS_LOGIN_FUNC_ui.pushButton_2.clicked.connect(self.TelaGestao)
    
    def VoltarMain(self):
        self.QtStack.setCurrentIndex(0)

    def fecharAplicacao(self):
        client_socket.send('0'.encode())
        sys.exit()
    
    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
    

    def botao_ok(self):
        cpf = self.tela_main_ui.lineEdit_2.text()
        senha = self.tela_main_ui.lineEdit.text()
        if cpf == '' or senha == '':
            QtWidgets.QMessageBox.information(self, 'erro', 'Digite valores válidos.')
        else:
            client_socket.send('2'.encode())
            lista_dados = [cpf, senha]
            dados = ",".join(lista_dados)
            client_socket.send(dados.encode())
            try:
                retorno = client_socket.recv(4096).decode()
            except:
                print("\nNão foi possível permanecer conectado!\n")
                client_socket.close()

            print(retorno)
            if retorno == '1':
                QtWidgets.QMessageBox.information(self, 'login', 'Login cliente realizado com sucesso.')
                self.QtStack.setCurrentIndex(2)
            elif retorno == '3':
                QtWidgets.QMessageBox.information(self, 'login', 'Login gerente realizado com sucesso.')
                self.QtStack.setCurrentIndex(3)
            else:
                QMessageBox.information(self, 'erro', 'Preencha os dados corretamente.!')
            
        self.tela_main_ui.lineEdit_2.setText('')
        self.tela_main_ui.lineEdit.setText('')
     
        
    
    def botao_Cadastra(self):
        self.dados_clienete = list()
        valid = False
        nome = self.TELA_CADASTRO_ui.lineEdit.text()
        cpf = self.TELA_CADASTRO_ui.lineEdit_2.text()
        email = self.TELA_CADASTRO_ui.lineEdit_3.text()
        senha = self.TELA_CADASTRO_ui.lineEdit_4.text()

        if nome == '' or cpf == '' or email == '' or senha == '':
            QtWidgets.QMessageBox.information(self, 'Erro', 'Digite valores válidos.')
        elif not verificar_nome(nome):
            QtWidgets.QMessageBox.information(self, 'Erro', 'Nome inválido. Digite apenas letras.')
        elif not cpf.isdigit():
            QtWidgets.QMessageBox.information(self, 'Erro', 'CPF inválido. Digite apenas números.')
        elif not email_valido(email):
            QtWidgets.QMessageBox.information(self, 'Erro', 'Email inválido.')
        else:
            client_socket.send('1'.encode())
            lista_dados = list()
            lista_dados.append(nome)
            lista_dados.append(cpf)
            lista_dados.append(email)
            lista_dados.append(senha)
            dados = ",".join(lista_dados)
            client_socket.send(dados.encode())
            try:
                retorno = client_socket.recv(4096).decode()
            except:
                print("\nNao foi possivel permanecer conectado!\n")
                client_socket.close()
            if retorno == '1':
                QtWidgets.QMessageBox.information(self, 'Cadastro', 'Cadastro realizado com sucesso.')
                valid = True
            else:
                QtWidgets.QMessageBox.information(self, 'Erro', 'CPF já cadastrado.')

        self.TELA_CADASTRO_ui.lineEdit.setText('')
        self.TELA_CADASTRO_ui.lineEdit_2.setText('')
        self.TELA_CADASTRO_ui.lineEdit_3.setText('')
        self.TELA_CADASTRO_ui.lineEdit_4.setText('')

        if valid:
            self.QtStack.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Ui_Main()
    sys.exit(app.exec_())
