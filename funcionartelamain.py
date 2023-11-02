import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QStringListModel
from tela_main_ui import *#
from TELA_CADASTRO_ui import *#
from TELA_USUARIO import *#
from TELA_GERENCIAMENTO import *#
from TELA_ESTATISTICA_ui import *#
from TELA_GESTAO_FILMES_ui import *#
from TELA_CADASTRO_FILMES import *#
from TELA_EXCLUIR_FILME_ui import *#
from TELA_LISTA_FILMES_ui import *#
from TELA_CLIENTE_VER_FILMES_ui import *
from TELA_ESCOLHE_LUGAR_ui import *
from classes.class_armazenar import *
from classes.class_pessoa import *
from classes.funcoes_aux import *
from classes.class_filme import *
from classes.class_conexao_bd import *
from classes.classe_armazena_filme import *

mydb = configure_mysql_connection()
db = create_database()

dados = Armazenar(mydb)
dados_filme = Armazenar_filmes(mydb)

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
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()

        self.tela_main_ui = Ui_Dialog()
        self.tela_main_ui.setupUi(self.stack0)

        self.TELA_CADASTRO_ui = Cadastrar()
        self.TELA_CADASTRO_ui.setupUi(self.stack1)

        self.TELA_USUARIO = AposLogin()
        self.TELA_USUARIO.setupUi(self.stack2)
        
        #Usa-se só para ajustar essa tela
        self.TELA_DPS_LOGIN_FUNC_ui = LOGIN_FUNC()
        self.TELA_DPS_LOGIN_FUNC_ui.setupUi(self.stack3)
        
        self.TELA_ESTATISTICA_ui = Estatistica()
        self.TELA_ESTATISTICA_ui.setupUi(self.stack4)
        
        self.TELA_GESTAO_FILMES_ui = GESTAO_FILMES()
        self.TELA_GESTAO_FILMES_ui.setupUi(self.stack5)
        
        self.TELA_CADASTRO_FILMES = Cadastrar_filme()
        self.TELA_CADASTRO_FILMES.setupUi(self.stack6)
        
        self.TELA_EXCUIR_FILME_ui = Excluir_Filme()
        self.TELA_EXCUIR_FILME_ui.setupUi(self.stack7)
        
        self.TELA_LISTA_FILMES_ui = Tela_Lista_Filmes()
        self.TELA_LISTA_FILMES_ui.setupUi(self.stack8)
        
        self.TELA_CLIENTE_VER_FILMES_ui = TELA_VER_FILMES()
        self.TELA_CLIENTE_VER_FILMES_ui.setupUi(self.stack9)
        
        self.TELA_ESCOLHE_LUGAR_ui = Escolhe_Lugar()
        self.TELA_ESCOLHE_LUGAR_ui.setupUi(self.stack10)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)

class Ui_Main(QMainWindow, Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)
        self.horarios_selecionados = list()
        

        #Tela_Main(Inicio)
        self.tela_main_ui.pushButton_3.clicked.connect(self.fecharAplicacao)
        self.tela_main_ui.pushButton_4.clicked.connect(self.abrirTelaCadastro)
        self.tela_main_ui.pushButton.clicked.connect(self.botao_ok)
        
        #Tela Cadastra pessoa
        self.TELA_CADASTRO_ui.pushButton_3.clicked.connect(self.VoltarMain)
        self.TELA_CADASTRO_ui.pushButton.clicked.connect(self.botao_Cadastra)
        
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
        self.TELA_CADASTRO_FILMES.pushButton_3.clicked.connect(self.TelaGestao)
        self.TELA_CADASTRO_FILMES.pushButton.clicked.connect(self.botao_cadastrar_filme)
        self.TELA_CADASTRO_FILMES.pushButton_2.clicked.connect(self.adicionar_horarios)
        
        #Tela_Excluir_Filmes
        self.TELA_EXCUIR_FILME_ui.pushButton_3.clicked.connect(self.TelaGestao)
        self.TELA_EXCUIR_FILME_ui.pushButton.clicked.connect(self.TelaExcluiFilme)
        self.TELA_EXCUIR_FILME_ui.pushButton_2.clicked.connect(self.botao_buscar)
        self.TELA_EXCUIR_FILME_ui.pushButton_4.clicked.connect(self.carregar_lista_completa_filmes_quando_exclui)
        
        #Tela_Listar_Filmes
        self.TELA_LISTA_FILMES_ui.pushButton_4.clicked.connect(self.TelaGestao)
        
        
        ##TELA_CLIENTES
        #Tela dps de login (TELA CLIENTE)
        self.TELA_USUARIO.pushButton_4.clicked.connect(self.VoltarMain)
        self.TELA_USUARIO.pushButton.clicked.connect(self.Tela_Cliente_Ver_Filmes)
        
        ##TELA_USER_VER_FILMES
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton.clicked.connect(self.abrirTelaDPSLoginCli)
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton_3.clicked.connect(self.botao_selecionar)
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton_2.clicked.connect(self.Tela_Cliente_botao_buscar)
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton_4.clicked.connect(self.Tela_Cliente_carregar_lista_completa_filmes)
        
        #TELA_ESCOLHE_LUGAR
        self.TELA_ESCOLHE_LUGAR_ui.pushButton.clicked.connect(self.Tela_Cliente_Ver_Filmes) 


    def botao_Cadastra(self):
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
            pessoa = Pessoa(cpf, nome, email, senha)
            if dados.armazenar(pessoa):
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

    def botao_ok(self):
        cpf = self.tela_main_ui.lineEdit_2.text()
        senha = self.tela_main_ui.lineEdit.text()
        if cpf == '' or senha == '':
            QtWidgets.QMessageBox.information(self, 'erro', 'Digite valores válidos.')
        elif dados.verificar_login_Cliente(cpf, senha):
                QtWidgets.QMessageBox.information(self, 'login', 'login cliente realizado com sucesso.')
                self.QtStack.setCurrentIndex(2)##Aqui vai mudar só para poder entre cliente e funcionario
                
        elif dados.verificar_login_Ger(cpf,senha):
            QMessageBox.information(self, 'login', 'login Gerente realizado com sucesso.')
            self.QtStack.setCurrentIndex(3)##Aqui vai mudar só para poder entre cliente e funcionario
        else:
            QMessageBox.information(self, 'erro', 'Preencha os dados corretamente.!')
                
        self.tela_main_ui.lineEdit_2.setText('')
        self.tela_main_ui.lineEdit.setText('')        
        dados.db_connection.consume_results()

    def fecharAplicacao(self):
        sys.exit()

    def VoltarMain(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)
        
    def abrirTelaDPSLoginCli(self):
        self.QtStack.setCurrentIndex(2)
    
    def abrirLoginFunc(self):
        self.QtStack.setCurrentIndex(3)

    def Tela_Estatistica(self):
        self.QtStack.setCurrentIndex(4)
        
    def TelaGestao(self):
        self.QtStack.setCurrentIndex(5)
        
    def TelaCadastraFilme(self):
        self.QtStack.setCurrentIndex(6)
        

   #tela de cadastro de filmes
    def botao_cadastrar_filme(self):
        horarios_escolhidos = list()
        minimum_date = QtCore.QDate(1800, 9, 14)
        midnight_time = QtCore.QTime(0, 0, 0)
        zero_datetime = QtCore.QDateTime(minimum_date, midnight_time)
        valid = False
        nome_filme = self.TELA_CADASTRO_FILMES.lineEdit_2.text()
        ano_filme = int(self.TELA_CADASTRO_FILMES.lineEdit_3.text())
        preco_str = float(self.TELA_CADASTRO_FILMES.lineEdit_4.text())
        classificacao = self.TELA_CADASTRO_FILMES.lineEdit_5.text()

        horarios_escolhidos.extend(self.horarios_selecionados)
        horarios_str = ', '.join(horarios_escolhidos)

        tipo_filme = self.TELA_CADASTRO_FILMES.comboBox.currentText()
        
        if nome_filme == '' or ano_filme == '' or preco_str == '' or classificacao == '':
            QtWidgets.QMessageBox.information(self, 'erro', 'Digite valores válidos.')
        elif not horarios_escolhidos:
            QtWidgets.QMessageBox.information(self, 'erro', 'Selecione pelo menos um horário.')
        else:
            preco = round(float(preco_str), 2)
            filme = Filme(nome_filme, ano_filme, preco, classificacao, horarios_str, tipo_filme)
            if dados_filme.armazenar_filmes(filme):
                QtWidgets.QMessageBox.information(self, 'Cadastro Filme', 'Filme cadastrado com sucesso.')
                valid = True
            else:
                QtWidgets.QMessageBox.information(self, 'Cadastro Filme', 'Erro, filme não cadastrado.')

        if valid:
            self.QtStack.setCurrentIndex(5)
        self.TELA_CADASTRO_FILMES.lineEdit_2.setText('')
        self.TELA_CADASTRO_FILMES.lineEdit_3.setText('')
        self.TELA_CADASTRO_FILMES.lineEdit_4.setText('')
        self.TELA_CADASTRO_FILMES.lineEdit_5.setText('')
        self.TELA_CADASTRO_FILMES.dateTimeEdit.setDateTime(zero_datetime)

    
    def adicionar_horarios(self):
        horario = self.TELA_CADASTRO_FILMES.dateTimeEdit.text()
        if horario:
            self.horarios_selecionados.append(horario)
            horario_usar = self.TELA_CADASTRO_FILMES.listView
            modelo_horario = QStandardItemModel()
            for horario in self.horarios_selecionados:
                item_horario = QStandardItem(f'HORÁRIOS: {horario}')
                item_horario.setEditable(False)
                modelo_horario.appendRow(item_horario)
            horario_usar.setModel(modelo_horario)
        else:
            QtWidgets.QMessageBox.information(self, 'Horário', 'Selecione um horário antes de adicionar.')
            
    def TelaVerTodosFilmes(self):   
        # Obtenha a lista de filmes do banco de dados
        filmes = dados_filme.obter_todos_filmes()

        if filmes:
            # Crie um modelo de lista para armazenar os nomes dos filmes
            model = QStringListModel()
            model.setStringList(filmes)

            # Associe o modelo ao QListView
            self.TELA_LISTA_FILMES_ui.listView.setModel(model)
            
            self.QtStack.setCurrentIndex(8)
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
    
     
    def carregar_lista_completa_filmes_quando_exclui(self):
        filmes = dados_filme.obter_todos_filmes()
        if filmes:
            model = QStringListModel()
            model.setStringList(filmes)
            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
        
        
    def botao_buscar(self):
        filme_id = self.TELA_EXCUIR_FILME_ui.lineEdit_2.text()

        # Verificar se o ID do filme é válido (deve ser um número inteiro)
        if not filme_id.isdigit():
            QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'ID do filme deve ser um número inteiro.')
            return
        # Chamar a função para buscar o filme no banco de dados
        filme_nome = dados_filme.buscar_filme_por_id(filme_id)

        # Verificar se o filme foi encontrado
        if filme_nome:
            # Criar um modelo de lista
            model = QStringListModel()

            # Adicionar o nome do filme ao modelo
            model.setStringList([filme_nome])

            # Associar o modelo ao QListView
            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
        else:
            QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'Nenhum filme com o ID especificado foi encontrado.')
        
    def TelaExcluiFilme(self):    
        # Obtenha a lista de filmes do banco de dados
        filmes = dados_filme.obter_todos_filmes()
        
        if filmes:
            # Crie um modelo de lista para armazenar os nomes dos filmes
            model = QStringListModel()
            model.setStringList(filmes)

            # Associe o modelo ao QListView
            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
            
            self.QtStack.setCurrentIndex(7)
            
            filme_id = self.TELA_EXCUIR_FILME_ui.lineEdit_2.text()
            if filme_id:
                # Verificar se o filme com o ID especificado existe no banco de dados
                if dados_filme.verificar_filme(filme_id):
                    # O filme foi encontrado, agora você pode removê-lo do banco de dados
                    if dados_filme.excluir_filmes(filme_id):
                        # Atualize a lista de filmes após a exclusão
                        filmes_atualizados = dados_filme.obter_todos_filmes()
                        model.setStringList(filmes_atualizados)
                        self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
                        self.QtStack.setCurrentIndex(7)
                        QtWidgets.QMessageBox.information(self, 'Excluir Filme', 'Filme removido com sucesso.')
                    else:
    
                        QtWidgets.QMessageBox.information(self, 'Erro', 'Erro ao excluir o filme.')
                else:

                    QtWidgets.QMessageBox.information(self, 'Excluir Filme', 'Nenhum filme com o ID especificado foi encontrado.')
                    
                # Limpar o campo de entrada do ID
                self.TELA_EXCUIR_FILME_ui.lineEdit_2.setText('')
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
            
    def Tela_Cliente_Ver_Filmes(self):
        # Obtenha a lista de filmes do banco de dados
        filmes = dados_filme.obter_todos_filmes()

        if filmes:
            # Crie um modelo de lista para armazenar os nomes dos filmes
            model = QStringListModel()
            model.setStringList(filmes)

            # Associe o modelo ao QListView na tela do cliente
            self.TELA_CLIENTE_VER_FILMES_ui.listView.setModel(model)
            
            self.QtStack.setCurrentIndex(9)  # Altere o índice para a tela do cliente
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
            
    def Tela_Cliente_botao_buscar(self):
        filme_id = self.TELA_CLIENTE_VER_FILMES_ui.lineEdit_2.text()

        # Verificar se o ID do filme é válido (deve ser um número inteiro)
        if not filme_id.isdigit():
            QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'ID do filme deve ser um número inteiro.')
            return
        # Chamar a função para buscar o filme no banco de dados
        filme_nome = dados_filme.buscar_filme_por_id(filme_id)

        # Verificar se o filme foi encontrado
        if filme_nome:
            # Criar um modelo de lista
            model = QStringListModel()

            # Adicionar o nome do filme ao modelo
            model.setStringList([filme_nome])

            # Associar o modelo ao QListView
            self.TELA_CLIENTE_VER_FILMES_ui.listView.setModel(model)
        else:
            QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'Nenhum filme com o ID especificado foi encontrado.')
            
    def Tela_Cliente_carregar_lista_completa_filmes(self):
        filmes = dados_filme.obter_todos_filmes()
        if filmes:
            model = QStringListModel()
            model.setStringList(filmes)
            self.TELA_CLIENTE_VER_FILMES_ui.listView.setModel(model)
            
    def botao_selecionar(self):
        reply = QtWidgets.QMessageBox.question(self, 'Seleção', 'Deseja comprar o ingresso para esse filme?',
                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        # Verifique a resposta do usuário
        if reply == QtWidgets.QMessageBox.Yes:
            self.QtStack.setCurrentIndex(10)
        else:
            self.TELA_CLIENTE_VER_FILMES_ui.lineEdit_2.setText('')
            
    def escolhe_lugar(self):
        self.QtStack.setCurrentIndex(10)
        
