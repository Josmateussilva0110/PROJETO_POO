import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from tela_main_ui import *#
from TELA_CADASTRO_ui import *#
from TELA_DPS_LOGIN_ui import *#
from TELA_DPS_LOGIN_FUNC_ui import *#
from TELA_ESTATISTICA_ui import *#
from TELA_GESTAO_FILMES_ui import *#
from TELA_DPS_CADASTRAR_FUNC_ui import *#
from TELA_EXCLUIR_FILME_ui import *#
from TELA_LISTA_FILMES_ui import *#
from classes.class_armazenar import *
from classes.class_pessoa import *
from classes.funcoes_aux import *
from classes.class_filme import *

dados = Armazenar()

filmes_adicionados_funcionario = [] ##Pega os filmes cadastrados
horarios_adicionados = []

# Esta função retorna a lista de filmes para cadastrados
def obter_lista_de_filmes():
    return filmes_adicionados_funcionario

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
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()

        self.tela_main_ui = Ui_Dialog()
        self.tela_main_ui.setupUi(self.stack0)

        self.TELA_CADASTRO_ui = Cadastrar()
        self.TELA_CADASTRO_ui.setupUi(self.stack1)

        self.TELA_DPS_LOGIN_ui = AposLogin()
        self.TELA_DPS_LOGIN_ui.setupUi(self.stack2)
        
        #Usa-se só para ajustar essa tela
        self.TELA_DPS_LOGIN_FUNC_ui = LOGIN_FUNC()
        self.TELA_DPS_LOGIN_FUNC_ui.setupUi(self.stack3)
        
        self.TELA_ESTATISTICA_ui = Estatistica()
        self.TELA_ESTATISTICA_ui.setupUi(self.stack4)
        
        self.TELA_GESTAO_FILMES_ui = GESTAO_FILMES()
        self.TELA_GESTAO_FILMES_ui.setupUi(self.stack5)
        
        self.TELA_DPS_CADASTRAR_FUNC_ui = Cadastrar_Filme()
        self.TELA_DPS_CADASTRAR_FUNC_ui.setupUi(self.stack6)
        
        self.TELA_EXCUIR_FILME_ui = Excluir_Filme()
        self.TELA_EXCUIR_FILME_ui.setupUi(self.stack7)
        
        self.TELA_LISTA_FILMES_ui = Tela_Lista_Filmes()
        self.TELA_LISTA_FILMES_ui.setupUi(self.stack8)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)

class Ui_Main(QMainWindow, Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)
        
        #Tela_Main(Inicio)
        self.tela_main_ui.pushButton_3.clicked.connect(self.fecharAplicacao)
        self.tela_main_ui.pushButton_4.clicked.connect(self.abrirTelaCadastro)
        self.tela_main_ui.pushButton.clicked.connect(self.botao_ok)
        
        #Tela Cadastra
        self.TELA_CADASTRO_ui.pushButton_3.clicked.connect(self.VoltarMain)
        self.TELA_CADASTRO_ui.pushButton.clicked.connect(self.botao_Cadastra)

        self.TELA_DPS_LOGIN_ui.pushButton_4.clicked.connect(self.VoltarMain)
        
        self.TELA_DPS_LOGIN_FUNC_ui.pushButton_4.clicked.connect(self.VoltarMain)
        self.TELA_DPS_LOGIN_FUNC_ui.pushButton.clicked.connect(self.Tela_Estatistica)
        self.TELA_DPS_LOGIN_FUNC_ui.pushButton_2.clicked.connect(self.TelaGestao)

        #Tela Estatistica
        self.TELA_ESTATISTICA_ui.pushButton_4.clicked.connect(self.abrirLoginFunc)
        
        #Tela_Gestao
        self.TELA_GESTAO_FILMES_ui.pushButton_4.clicked.connect(self.abrirLoginFunc)
        self.TELA_GESTAO_FILMES_ui.pushButton_3.clicked.connect(self.TelaCadastraFilme)
        self.TELA_GESTAO_FILMES_ui.pushButton_2.clicked.connect(self.TelaExcluiFilme)
        self.TELA_GESTAO_FILMES_ui.pushButton.clicked.connect(self.TelaVerTodosFilmes)
        
        #Tela_Cadastrar_Filmes
        self.TELA_DPS_CADASTRAR_FUNC_ui.pushButton_3.clicked.connect(self.TelaGestao)
        self.TELA_DPS_CADASTRAR_FUNC_ui.pushButton.clicked.connect(self.botao_cadastrar_filme)
        self.TELA_DPS_CADASTRAR_FUNC_ui.pushButton_2.clicked.connect(self.botao_cadastrar_horario)
        
        #Tela_Excluir_Filmes
        self.TELA_EXCUIR_FILME_ui.pushButton_3.clicked.connect(self.TelaGestao)
        self.TELA_EXCUIR_FILME_ui.pushButton_2.clicked.connect(self.buscar_filme)
        self.TELA_EXCUIR_FILME_ui.pushButton.clicked.connect(self.remover_filme)
        
        #Tela_Listar_Filmes
        self.TELA_LISTA_FILMES_ui.pushButton_4.clicked.connect(self.TelaGestao)
        self.filme_encontrado = None


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
            pessoa = Pessoa(cpf, nome, email, senha)
            certo_cliente = dados.armazenar(pessoa, cpf)
            if certo_cliente:
                QMessageBox.information(self, 'cadastro', 'Cadastro realizado com sucesso.')
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
        cpf = self.tela_main_ui.lineEdit_2.text()
        senha = self.tela_main_ui.lineEdit.text()
        if cpf == '' or senha == '':
            QtWidgets.QMessageBox.information(self, 'erro', 'Digite valores válidos.')
        elif dados.verificar_login_Cliente(cpf, senha):
                QtWidgets.QMessageBox.information(self, 'login', 'login cliente realizado com sucesso.')
                self.QtStack.setCurrentIndex(3)##Aqui vai mudar só para poder entre cliente e funcionario
                
        elif dados.verificar_login_Ger(cpf,senha):
            QMessageBox.information(self, 'login', 'login Gerente realizado com sucesso.')
            self.QtStack.setCurrentIndex(2)##Aqui vai mudar só para poder entre cliente e funcionario
        else:
            QMessageBox.information(self, 'erro', 'Preencha os dados corretamente.')
                
        self.tela_main_ui.lineEdit_2.setText('')
        self.tela_main_ui.lineEdit.setText('')        
            

    def fecharAplicacao(self):
        sys.exit()

    def VoltarMain(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
    
    def abrirLoginFunc(self):
        self.QtStack.setCurrentIndex(3)

    def Tela_Estatistica(self):
        self.QtStack.setCurrentIndex(4)
        
    def TelaGestao(self):
        self.QtStack.setCurrentIndex(5)
        
    def TelaCadastraFilme(self):
        self.QtStack.setCurrentIndex(6)
        
    def TelaExcluiFilme(self):
        self.QtStack.setCurrentIndex(7)
        
    def TelaVerTodosFilmes(self):
        self.QtStack.setCurrentIndex(8)
        

   #tela de cadastro de filmes
    def botao_cadastrar_filme(self):
        minimum_date = QtCore.QDate(1800, 9, 14)
        midnight_time = QtCore.QTime(0, 0, 0)
        zero_datetime = QtCore.QDateTime(minimum_date, midnight_time)
        valid = False
        id_filme = int(self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit.text())
        nome_filme = self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit_2.text()
        ano_filme = int(self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit_3.text())
        preco = float(self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit_4.text())
        classificacao = self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit_5.text()
        horario = self.TELA_DPS_CADASTRAR_FUNC_ui.dateTimeEdit.text()
        tipo_filme = self.TELA_DPS_CADASTRAR_FUNC_ui.comboBox.currentText()
        if id_filme == '' or nome_filme == '' or ano_filme == '' or preco == '' or classificacao == '':
            QtWidgets.QMessageBox.information(self, 'erro', 'Digite valores válidos.')
        else:
            filme = Filme(id_filme, nome_filme, ano_filme, preco, classificacao, horario, tipo_filme)
            certo_filme = dados.armazenar_filme(filme, id_filme)
            if certo_filme:
                QtWidgets.QMessageBox.information(self, 'Cadastro Filme', 'filme cadastrado com sucesso.')
                valid = True
            else:
                QtWidgets.QMessageBox.information(self, 'Cadastro Filme', 'Erro, Id de filme já cadastrado.')
        if valid:
            filmes_adicionados_funcionario.append(Filme(id_filme, nome_filme, ano_filme, preco, classificacao, horario, tipo_filme))
            self.QtStack.setCurrentIndex(5)
        self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit.setText('')
        self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit_2.setText('')
        self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit_3.setText('')
        self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit_4.setText('')
        self.TELA_DPS_CADASTRAR_FUNC_ui.lineEdit_5.setText('')
        self.TELA_DPS_CADASTRAR_FUNC_ui.dateTimeEdit.setDateTime(zero_datetime)
        
    def botao_cadastrar_horario(self):
        horario = self.TELA_DPS_CADASTRAR_FUNC_ui.dateTimeEdit.text()
        horarios_adicionados.append(horario)
        #print(horarios_adicionados)
        QtWidgets.QMessageBox.information(self, 'Cadastro Filme', 'Horário adicionado com sucesso.')
        
    def horarios_formatados(self):
        return [horario for horario in horarios_adicionados]



    #tela de excluir
    def buscar_filme(self):
        id = int(self.TELA_EXCUIR_FILME_ui.lineEdit_2.text())
        achado = dados.buscar_filme(id)
        if achado is not None:
            self.filme_encontrado = achado  # Armazena o filme encontrado
            filme_encontrado = self.TELA_EXCUIR_FILME_ui.listView
            modelo_filme = QStandardItemModel()
            item_filme = QStandardItem(f'ID: {achado._id} - Nome: {achado._nome} - Ano: {achado._ano} - Preço: {achado._preco} - classificação: {achado._classificacao} - Tipo: {achado._tipo}')
            item_filme.setEditable(False)  # Torna o item não editável
            modelo_filme.appendRow(item_filme)
            filme_encontrado.setModel(modelo_filme)
        else:
            self.filme_encontrado = None  # Limpa a variável de filme encontrado
            QtWidgets.QMessageBox.information(self, 'Filme', 'Erro, filme não encontrado.')
        #self.TELA_EXCUIR_FILME_ui.lineEdit_2.setText('')



    def TelaVerTodosFilmes(self):
        self.QtStack.setCurrentIndex(8)
        lista_view = self.TELA_LISTA_FILMES_ui.listView
        modelo = QStandardItemModel()
        lista_de_filmes = obter_lista_de_filmes()  # Use a função fpara obter os filmes

        for filme in lista_de_filmes:
            horarios_formatados = ', '.join(self.horarios_formatados())
            item = QStandardItem(f'ID: {filme._id} - Nome: {filme._nome} - Ano: {filme._ano} - Preço: {filme._preco} - classificação: {filme._classificacao} - Horário: {horarios_formatados} - Tipo: {filme._tipo}')
            modelo.appendRow(item)

        lista_view.setModel(modelo)
    
    def remover_filme(self):
        if self.filme_encontrado is not None:
            del dados._dados_filmes[self.filme_encontrado._id]

            # Remova o filme da lista de filmes adicionados pelo funcionário
            for filme in filmes_adicionados_funcionario:
                if filme._id == self.filme_encontrado._id:
                    filmes_adicionados_funcionario.remove(filme)

            self.filme_encontrado = None  # Limpa a variável de filme encontrado
            self.TELA_EXCUIR_FILME_ui.listView.setModel(QStandardItemModel())  # Limpa a lista de filmes na tela
            QtWidgets.QMessageBox.information(self, 'Filme excluído', f'Filme excluído com sucesso.')
