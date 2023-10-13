import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from tela_main_ui import *
from TELA_CADASTRO_ui import *
from tela_login_ui import *
from classes.class_armazenar import *
from classes.class_pessoa import *

dados = Armazenar()

class Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()#Função da biblioteca
        
        #quantidade de telas
        self.stack0 =QtWidgets.QMainWindow()
        self.stack1 =QtWidgets.QMainWindow()
        self.stack2 =QtWidgets.QMainWindow()
        
        #Fazendo a chamada de cada uma individualmente
        self.tela_main_ui=Ui_Dialog()
        self.tela_main_ui.setupUi(self.stack0)

        self.TELA_CADASTRO_ui=Cadastrar()
        self.TELA_CADASTRO_ui.setupUi(self.stack1)

        self.tela_login_ui = Login()
        self.tela_login_ui.setupUi(self.stack2)
        
        #Fazendo Funcionar
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QMainWindow, Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)
        
        #Tela main
        self.tela_main_ui.pushButton_3.clicked.connect(self.fecharAplicacao) #FECHA O APP PELO BOTAO
        self.tela_main_ui.pushButton.clicked.connect(self.abrirTelaCadastro) # TELA CADASTRO
        self.tela_main_ui.pushButton_2.clicked.connect(self.abrirLogin) #TELA LOGIN 
        
        #tela Login
        self.tela_login_ui.pushButton_3.clicked.connect(self.VoltarMain) #Volta Menu Inicial
        self.tela_login_ui.pushButton_2.clicked.connect(self.abrirTelaCadastro) #Abre direto na tela cadastro
        self.tela_login_ui.pushButton.clicked.connect(self.botao_ok) #abre a telinha de confirmação
        
        #tela Cadastro
        self.TELA_CADASTRO_ui.pushButton_3.clicked.connect(self.VoltarMain) #Volta Menu Inicial
        self.TELA_CADASTRO_ui.pushButton_2.clicked.connect(self.abrirLogin) #Entra Direto no Login
        self.TELA_CADASTRO_ui.pushButton.clicked.connect(self.botao_Cadastra) #abre a telinha de confirmação de cadastro
        
    def botao_Cadastra(self):
        nome = self.TELA_CADASTRO_ui.lineEdit.text()
        cpf = self.TELA_CADASTRO_ui.lineEdit_2.text()
        email = self.TELA_CADASTRO_ui.lineEdit_3.text()
        senha = self.TELA_CADASTRO_ui.lineEdit_4.text()
        pessoa = Pessoa(cpf, nome, email, senha)
        dados.armazenar(pessoa)
        dados.exibir_pessoa()
        self.QtStack.setCurrentIndex(0)
    
    def botao_ok(self): #responsavel por abrir a tela de confirmação
        QtWidgets.QMessageBox.information(self, 'login', 'login realizado com sucesso.')
    

    def botao_confirmacao(self): #responsavel por abrir a tela de confirmação de cadastro
        QtWidgets.QMessageBox.information(self, 'cadastro', 'pessoa cadastrada com sucesso.')

    def fecharAplicacao(self): #Função responsavel por fechar 
        sys.exit()
    
    def VoltarMain(self):
        self.QtStack.setCurrentIndex(0)
    
    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
    
    def abrirLogin(self):
        self.QtStack.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
