import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from tela_main_ui import *
from TELA_CADASTRO_ui import *
from TELA_DPS_LOGIN_ui import *
from TELA_DPS_LOGIN_FUNC_ui import *
from TELA_ESTATISTICA_ui import *
from TELA_GESTAO_FILMES_ui import *
from classes.class_armazenar import *
from classes.class_pessoa import *
from classes.funcoes_aux import *

dados = Armazenar()

class Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()

        self.tela_main_ui = Ui_Dialog()
        self.tela_main_ui.setupUi(self.stack0)

        self.TELA_CADASTRO_ui = Cadastrar()
        self.TELA_CADASTRO_ui.setupUi(self.stack1)

        self.TELA_DPS_LOGIN_ui = AposLogin()
        self.TELA_DPS_LOGIN_ui.setupUi(self.stack2)
        
        self.TELA_DPS_LOGIN_FUNC_ui = LOGIN_FUNC()
        self.TELA_DPS_LOGIN_FUNC_ui.setupUi(self.stack3)
        
        self.TELA_ESTATISTICA_ui = Estatistica()
        self.TELA_ESTATISTICA_ui.setupUi(self.stack4)
        
        self.TELA_GESTAO_FILMES_ui = GESTAO_FILMES()
        self.TELA_GESTAO_FILMES_ui.setupUi(self.stack5)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)

class Ui_Main(QMainWindow, Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.tela_main_ui.pushButton_3.clicked.connect(self.fecharAplicacao)
        self.tela_main_ui.pushButton_4.clicked.connect(self.abrirTelaCadastro)
        self.tela_main_ui.pushButton.clicked.connect(self.botao_ok)

        self.TELA_CADASTRO_ui.pushButton_3.clicked.connect(self.VoltarMain)
        self.TELA_CADASTRO_ui.pushButton.clicked.connect(self.botao_Cadastra)

        self.TELA_DPS_LOGIN_ui.pushButton_4.clicked.connect(self.VoltarMain)
        
        self.TELA_DPS_LOGIN_FUNC_ui.pushButton_4.clicked.connect(self.VoltarMain)
        self.TELA_DPS_LOGIN_FUNC_ui.pushButton.clicked.connect(self.Tela_Estatistica)
        self.TELA_DPS_LOGIN_FUNC_ui.pushButton_2.clicked.connect(self.TelaGestao)

        # Adicione a função de configuração da combobox
        self.configurar_combobox()

        #Tela Estatistica
        self.TELA_ESTATISTICA_ui.pushButton_4.clicked.connect(self.abrirLoginFunc)
        
        #Tela_Gestao
        self.TELA_GESTAO_FILMES_ui.pushButton_4.clicked.connect(self.abrirLoginFunc)

    def botao_Cadastra(self):
        valid = False
        nome = self.TELA_CADASTRO_ui.lineEdit.text()
        cpf = self.TELA_CADASTRO_ui.lineEdit_2.text()
        email = self.TELA_CADASTRO_ui.lineEdit_3.text()
        senha = self.TELA_CADASTRO_ui.lineEdit_4.text()

        if nome == '' or cpf == '' or email == '' or senha == '':
            QtWidgets.QMessageBox.information(self, 'erro', 'Digite valores válidos.')
        elif not verificar_nome(nome):
            QtWidgets.QMessageBox.information(self, 'erro', 'Nome inválido. Digite apenas letras.')
        elif not cpf.isdigit():
            QtWidgets.QMessageBox.information(self, 'erro', 'CPF inválido. Digite apenas números.')
        elif not email_valido(email):
            QtWidgets.QMessageBox.information(self, 'erro', 'Email inválido.')
        else:
            #Seleciona o tipo
            tipo_selecionado = self.TELA_CADASTRO_ui.comboBox.currentText()
            if tipo_selecionado == "Cliente":
                pessoa = Pessoa(cpf, nome, email, senha)
                certo_cliente = dados.armazenar(pessoa, cpf)
                if certo_cliente:
                    QMessageBox.information(self, 'cadastro', 'Cadastro Cliente realizado com sucesso.')
                    valid = True
                else:
                    QMessageBox.information(self, 'cadastro', 'erro, cpf ja tem cadastro.')
            elif tipo_selecionado == "Funcionário":
                funcionario = Pessoa(cpf, nome, email, senha)
                certo_funcionario = dados.armazena_func(funcionario, cpf)
                if certo_funcionario:
                    QMessageBox.information(self, 'cadastro', 'Cadastro Funcionario realizado com sucesso.')
                    valid = True
                else:
                    QMessageBox.information(self, 'cadastro', 'erro, cpf ja tem cadastro.')
        self.TELA_CADASTRO_ui.lineEdit.setText('')
        self.TELA_CADASTRO_ui.lineEdit_2.setText('')
        self.TELA_CADASTRO_ui.lineEdit_3.setText('')
        self.TELA_CADASTRO_ui.lineEdit_4.setText('')
            
        if valid:
            self.QtStack.setCurrentIndex(0)

    def botao_ok(self):
        valid = 0
        cpf = self.tela_main_ui.lineEdit_2.text()
        senha = self.tela_main_ui.lineEdit.text()
        if cpf == '' or senha == '':
            QtWidgets.QMessageBox.information(self, 'erro', 'Digite valores válidos.')
        elif dados.verificar_login(cpf, senha) or dados.verificar_login_func(cpf,senha):
            tipo_selecionado = self.TELA_CADASTRO_ui.comboBox.currentText()
            if tipo_selecionado == "Cliente":
                QtWidgets.QMessageBox.information(self, 'login', 'login cliente realizado com sucesso.')
                valid = 1
                self.tela_main_ui.lineEdit_2.setText('')
                self.tela_main_ui.lineEdit.setText('')
                self.QtStack.setCurrentIndex(2)
                
            elif tipo_selecionado == "Funcionário":
                QMessageBox.information(self, 'login', 'login funcionario realizado com sucesso.')
                valid = 2
                self.tela_main_ui.lineEdit_2.setText('')
                self.tela_main_ui.lineEdit.setText('')
                
        else:
            QtWidgets.QMessageBox.information(self, 'Erro', 'Login ou senha inválidos.')
            self.tela_main_ui.lineEdit_2.setText('')
            self.tela_main_ui.lineEdit.setText('')

        if valid == 1:
            self.QtStack.setCurrentIndex(2)
        elif valid == 2:
           self.QtStack.setCurrentIndex(3)

    def fecharAplicacao(self):
        sys.exit()

    def VoltarMain(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
    
    def abrirLoginFunc(self):
        self.QtStack.setCurrentIndex(3)

    def configurar_combobox(self):
        opcoes = ["Cliente", "Funcionário"]
        self.TELA_CADASTRO_ui.comboBox.clear()
        self.TELA_CADASTRO_ui.comboBox.addItems(opcoes)
        self.TELA_CADASTRO_ui.comboBox.currentIndexChanged.connect(self.selecionar_tipo)
    
    def selecionar_tipo(self, index):
        tipo_selecionado = self.TELA_CADASTRO_ui.comboBox.itemText(index)
        if tipo_selecionado == "Cliente":
            QMessageBox.information(self, 'Tipo selecionado', 'Você selecionou Cliente.')
        elif tipo_selecionado == "Funcionário":
            QMessageBox.information(self,'Tipo selecionado', 'Você selecionou Funcionário')

    def Tela_Estatistica(self):
        self.QtStack.setCurrentIndex(4)
        
    def TelaGestao(self):
        self.QtStack.setCurrentIndex(5) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Ui_Main()
    sys.exit(app.exec_())
