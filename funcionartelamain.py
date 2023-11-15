import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QInputDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QStringListModel
from tela_main_ui import *#
from TELA_CADASTRO_ui import *#
from TELA_USUARIO import *#
from TELA_GERENCIAMENTO import *#
from TELA_ESTATISTICA_ui import *#
from TELA_EXCLUIR_FILME_ui import *
from TELA_GESTAO_FILMES_ui import *#
from TELA_CADASTRO_FILMES import *#
from TELA_LISTA_FILMES_ui import *#
from TELA_CLIENTE_VER_FILMES_ui import *
from TELA_LAYOUT import *
from TELA_PAGAMENTO import *
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
        self.stack11 = QtWidgets.QMainWindow()

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
        
        self.TELA_LAYOUT = Tela_layout()
        self.TELA_LAYOUT.setupUi(self.stack10)

        self.TELA_PAGAMENTO = Tela_pagamento()
        self.TELA_PAGAMENTO.setupUi(self.stack11)


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
        self.QtStack.addWidget(self.stack11)

class Ui_Main(QMainWindow, Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)
        self.horarios_selecionados = list()
        self.classificacao = ''
        self.dados_clienete = list()
        self.dados_cliente_final = list()
        self.saida = None
        

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
        self.TELA_CADASTRO_FILMES.pushButton_4.clicked.connect(self.adicionar_classificacao)
        
        #Tela_Excluir_Filmes
        self.TELA_EXCUIR_FILME_ui.pushButton_4.clicked.connect(self.TelaGestao)
        self.TELA_EXCUIR_FILME_ui.listView.clicked.connect(self.item_selecionado_Excluir_filmes)
        self.TELA_EXCUIR_FILME_ui.pushButton_3.clicked.connect(self.botao_buscar_tela_ecluir)
        self.TELA_EXCUIR_FILME_ui.pushButton_9.clicked.connect(self.TelaVerTodosFilmes_Tela_excluir)
        
        #Tela_Listar_Filmes
        self.TELA_LISTA_FILMES_ui.pushButton_4.clicked.connect(self.TelaGestao)
        self.TELA_LISTA_FILMES_ui.listView.clicked.connect(self.item_selecionado_lista_filmes)
        self.TELA_LISTA_FILMES_ui.pushButton_2.clicked.connect(self.botao_buscar)
        self.TELA_LISTA_FILMES_ui.pushButton_5.clicked.connect(self.carregar_lista_completa_filmes)
        
        
        ##TELA_CLIENTES
        #Tela dps de login (TELA CLIENTE)
        self.TELA_USUARIO.pushButton_4.clicked.connect(self.VoltarMain)
        self.TELA_USUARIO.pushButton.clicked.connect(self.Tela_Cliente_Ver_Filmes)
        
        ##TELA_USER_VER_FILMES
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton.clicked.connect(self.abrirTelaDPSLoginCli)
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton_2.clicked.connect(self.Tela_Cliente_botao_buscar)
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton_4.clicked.connect(self.Tela_Cliente_carregar_lista_completa_filmes_em_cartaz)
        self.TELA_CLIENTE_VER_FILMES_ui.listView.clicked.connect(self.item_selecionado_lista_filmes_cliente)

        
        #TELA_ESCOLHE_LUGAR
        buttons_and_functions = lista_botoes_red(self)
        for button, function in buttons_and_functions:
            button.clicked.connect(lambda _, btn=button: function(btn))
        
        self.TELA_LAYOUT.pushButton_2.clicked.connect(self.Tela_Cliente_Ver_Filmes)

        #TELA HORARIO
        self.TELA_PAGAMENTO.pushButton_2.clicked.connect(self.Tela_Cliente_Ver_Filmes)


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
                self.saida = dados.buscar_cliente_cpf(cpf)
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
    
    def escolhe_lugar(self):
        self.QtStack.setCurrentIndex(10)
    
    def escolher_horarios(self):
        self.QtStack.setCurrentIndex(11)
        
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
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
            
    def item_selecionado_Excluir_filmes(self, index):
        if index.isValid():
            item_selecionado = index.data()

            # Se o item for válido, você pode acessar o texto (nome do filme, neste caso)
            if item_selecionado:
                # Divida a string do item selecionado para extrair o ID
                partes = item_selecionado.split()

                # O ID do filme é a última parte da string
                filme_id = partes[1]

                # Verificar se o filme com o ID especificado está em cartaz
                if dados_filme.verificar_filme_em_cartaz(filme_id):
                    # Exiba um QMessageBox para confirmar a retirada do filme do cartaz
                    reply = QMessageBox.question(
                        self,
                        'Cartaz',
                        f'Deseja retirar o filme com ID {filme_id} do cartaz?',
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No
                    )

                    filme_id = int(filme_id)

                    if reply == QMessageBox.Yes:
                        if dados_filme.marcar_filme_em_cartaz(filme_id, 0):
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Filme com ID {filme_id} retirado como em cartaz.')
                        else:
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Erro ao retirar o filme com ID {filme_id} como em cartaz.')

                        filmes_atualizados = dados_filme.obter_todos_filmes()
                        model = QStringListModel()
                        model.setStringList(filmes_atualizados)
                        self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
                else:
                    QtWidgets.QMessageBox.information(self, 'Filme Fora de Cartaz', 'Este filme não está mais em cartaz.')
        else:
            QtWidgets.QMessageBox.information(self, 'Itens Filme', 'Nenhum item selecionado.')
                
                
    def botao_buscar_tela_ecluir(self):
        filme_id = self.TELA_EXCUIR_FILME_ui.lineEdit_4.text()

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
            
    def TelaVerTodosFilmes_Tela_excluir(self):   
        # Obtenha a lista de filmes do banco de dados
        filmes = dados_filme.obter_todos_filmes()

        if filmes:
            # Crie um modelo de lista para armazenar os nomes dos filmes
            model = QStringListModel()
            model.setStringList(filmes)

            # Associe o modelo ao QListView
            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
            
            self.QtStack.setCurrentIndex(7)
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')

    def botao_cadastrar_filme(self):
        horarios_escolhidos = list()
        valid = False
        filme = ''
        minimum_date = QtCore.QDate(1800, 9, 14)
        midnight_time = QtCore.QTime(0, 0, 0)
        zero_datetime = QtCore.QDateTime(minimum_date, midnight_time)
        nome_filme = self.TELA_CADASTRO_FILMES.lineEdit_2.text()
        ano_filme = self.TELA_CADASTRO_FILMES.lineEdit_3.text()
        preco_str = self.TELA_CADASTRO_FILMES.lineEdit_4.text()

        #converter o dicionario de horários em string
        horarios_escolhidos.extend(self.horarios_selecionados)
        horarios_str = ', '.join([f'{horario} - {tipo}' for horario, tipo in self.horarios_selecionados])
        #limpar a lista de horarios
        self.horarios_selecionados.clear()
        
        if verificar_espacos(nome_filme, ano_filme, preco_str, self.classificacao):
            QtWidgets.QMessageBox.information(self, 'erro', 'Digite valores válidos.')
        elif not horarios_escolhidos:
            QtWidgets.QMessageBox.information(self, 'erro', 'Selecione pelo menos um horário.')
        elif not verificar_valor_inteiro(ano_filme) or not verificar_valor_flutuante(preco_str):
            QtWidgets.QMessageBox.information(self, 'erro', 'Valores de ano ou preço incorretos.')
        else:
            preco = float(preco_str)
            if preco < 0.0:
                QtWidgets.QMessageBox.information(self, 'erro', 'O preço deve ser maior que zero.')
            else:
                filme = Filme(nome_filme, ano_filme, preco, self.classificacao, horarios_str)
                aux = dados_filme.armazenar_filmes(filme)
                if aux:
                    QtWidgets.QMessageBox.information(self, 'Cadastro Filme', 'Filme cadastrado com sucesso.')
                    valid = True
                else:
                    QtWidgets.QMessageBox.information(self, 'Cadastro Filme', 'Erro, filme não cadastrado.')

        if valid:
            self.QtStack.setCurrentIndex(5)
        self.TELA_CADASTRO_FILMES.lineEdit_2.setText('')
        self.TELA_CADASTRO_FILMES.lineEdit_3.setText('')
        self.TELA_CADASTRO_FILMES.lineEdit_4.setText('')
        self.TELA_CADASTRO_FILMES.dateTimeEdit.setDateTime(zero_datetime)
        self.TELA_CADASTRO_FILMES.listView.setModel(QStandardItemModel())
        self.TELA_CADASTRO_FILMES.listView_2.setModel(QStandardItemModel())
    
    def adicionar_horarios(self):
        horario = self.TELA_CADASTRO_FILMES.dateTimeEdit.text()
        tipo_filme = self.TELA_CADASTRO_FILMES.comboBox.currentText()

        if horario:
            # Adicione o par horário-tipo à lista de tuplas
            horario_tipo_tuple = (horario, tipo_filme)
            self.horarios_selecionados.append(horario_tipo_tuple)

            # Crie uma lista de strings para representar os pares horário-tipo
            horarios_strings = [f'{h} - {t}' for h, t in self.horarios_selecionados]

            # Atualize o QListView com a lista de strings
            horario_usar = self.TELA_CADASTRO_FILMES.listView
            modelo_horario = QStandardItemModel()
            for horario_str in horarios_strings:
                item_horario = QStandardItem(horario_str)
                item_horario.setEditable(False)
                modelo_horario.appendRow(item_horario)
            horario_usar.setModel(modelo_horario)
        else:
            QtWidgets.QMessageBox.information(self, 'Horário', 'Selecione um horário antes de adicionar.')

    

    def adicionar_classificacao(self):
        # Obtenha a classificação selecionada
        classificacao_selecionada = QInputDialog.getItem(
            self, 'Seleção', 'Selecione a classificação:', lista_de_classificacao_filme(), 0, False
        )

        if classificacao_selecionada[1]:
            # Se o usuário selecionou uma classificação, adicione-a ao QListView
            classificacoes_strings = [classificacao_selecionada[0]]

            # Crie um modelo para a lista de classificações
            modelo_classificacoes = QStandardItemModel()

            for classificacao_str in classificacoes_strings:
                item_classificacao = QStandardItem(classificacao_str)
                item_classificacao.setEditable(False)
                modelo_classificacoes.appendRow(item_classificacao)

            # Associe o modelo ao QListView
            classificacao_usar = self.TELA_CADASTRO_FILMES.listView_2
            classificacao_usar.setModel(modelo_classificacoes)

            # Armazene a classificação atual para uso posterior
            self.classificacao = classificacao_selecionada[0]



            
    def item_selecionado_lista_filmes(self, index):
        if index.isValid():
            item_selecionado = index.data()

            # Se o item for válido, você pode acessar o texto (nome do filme, neste caso)
            if item_selecionado:
                # Divida a string do item selecionado para extrair o ID
                partes = item_selecionado.split()

                # O ID do filme é a última parte da string
                filme_id = partes[1]

                # Verificar se o filme com o ID especificado já está em cartaz
                if not dados_filme.verificar_filme_em_cartaz(filme_id):
                    # Exiba um QMessageBox para confirmar a marcação do filme como "Em Cartaz"
                    reply = QMessageBox.question(
                        self,
                        'Cartaz',
                        f'Deseja colocar o filme com ID {filme_id} em cartaz?',
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No
                    )

                    filme_id = int(filme_id)

                    if reply == QMessageBox.Yes:
                        if dados_filme.marcar_filme_em_cartaz(filme_id, 1):
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Filme com ID {filme_id} marcado como em cartaz.')
                        else:
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Erro ao marcar o filme com ID {filme_id} como em cartaz.')

                        filmes_atualizados = dados_filme.obter_todos_filmes()
                        model = QStringListModel()
                        model.setStringList(filmes_atualizados)
                        self.TELA_LISTA_FILMES_ui.listView.setModel(model)
                else:
                    QtWidgets.QMessageBox.information(self, 'Filme em Cartaz', 'Este filme já está em cartaz.')
        else:
            QtWidgets.QMessageBox.information(self, 'Itens Filme', 'Nenhum item selecionado.')



            
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
    
     
    def carregar_lista_completa_filmes(self):
        filmes = dados_filme.obter_todos_filmes()
        if filmes:
            model = QStringListModel()
            model.setStringList(filmes)
            self.TELA_LISTA_FILMES_ui.listView.setModel(model)
        
        
    def botao_buscar(self):
        filme_id = self.TELA_LISTA_FILMES_ui.lineEdit_2.text()

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
            self.TELA_LISTA_FILMES_ui.listView.setModel(model)
        else:
            QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'Nenhum filme com o ID especificado foi encontrado.')
            
    def item_selecionado_lista_filmes_cliente(self, index):
        # Obtenha o item selecionado na QListView
        if index.isValid():
            item_selecionado = index.data()

            # Se o item for válido, você pode acessar o texto (nome do filme, neste caso)
            if item_selecionado:
                # Divida a string do item selecionado para extrair o ID
                partes = item_selecionado.split()

                # O ID do filme é a última parte da string
                filme_id = partes[1]

                # Exiba um QMessageBox ou lógica específica do cliente aqui
                reply = QMessageBox.question(
                    self,
                    'Detalhes do Filme',
                    f'Deseja selecionar esse filme?',
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )
                if reply == QMessageBox.Yes:
                    self.dados_clienete = []
                    # Obtenha os horários disponíveis para o filme
                    retorno_horarios = dados_filme.buscar_horarios_id(filme_id)
                    filme_selecionado = dados_filme.buscar_dados_filmes(filme_id)
                    self.dados_clienete.append(filme_selecionado)
                    # Converta a lista de horários em uma lista de strings
                    horarios_str = [f"{horario} " for horario in retorno_horarios]
                    # Exiba os horários para o usuário escolher usando um QInputDialog
                    horario_selecionado, ok = QInputDialog.getItem(self, 'Seleção', 'Selecione o horário:', horarios_str, 0, False)

                    if not ok:
                        QtWidgets.QMessageBox.information(self, 'Seleção', 'Compra cancelada.')
                        return

                    self.dados_clienete.append(horario_selecionado)
                    # O usuário selecionou um horário
                    reply = QtWidgets.QMessageBox.question(
                        self, 'Seleção', 'Deseja comprar o ingresso para esse filme?',
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                        QtWidgets.QMessageBox.No
                    )
                    # Verifique a resposta do usuário
                    if reply == QtWidgets.QMessageBox.Yes:
                        self.dados_clienete.append(self.saida)
                        self.dados_cliente_final.append(self.dados_clienete)
                        self.QtStack.setCurrentIndex(10)
                    else:
                        self.TELA_CLIENTE_VER_FILMES_ui.lineEdit_2.setText('')
                else:
                    QtWidgets.QMessageBox.information(self, 'Itens Filme', 'Nenhum item selecionado.')


                
    def Tela_Cliente_Ver_Filmes(self):
    # Obtenha a lista de filmes do banco de dados
        filmes = dados_filme.obter_todos_filmes()

        if filmes:
            # Filtra apenas os filmes em cartaz
            filmes_em_cartaz = [filme for filme in filmes if 'Em Cartaz: 1' in filme]
            if not filmes_em_cartaz:
                QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes em cartaz no momento.')
            else:
                # Crie um modelo de lista para armazenar os nomes dos filmes em cartaz
                model = QStringListModel()
                model.setStringList(filmes_em_cartaz)

                # Associe o modelo ao QListView na tela do cliente
                self.TELA_CLIENTE_VER_FILMES_ui.listView.setModel(model)

                self.QtStack.setCurrentIndex(9)  # Altere o índice para a tela do cliente
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes em cartaz.')
            
    def Tela_Cliente_botao_buscar(self):
        filme_id = self.TELA_CLIENTE_VER_FILMES_ui.lineEdit_2.text()

        # Verificar se o ID do filme é válido (deve ser um número inteiro)
        if not filme_id.isdigit():
            QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'ID do filme deve ser um número inteiro.')
            return

        # Verificar se o filme com o ID especificado está em cartaz
        if dados_filme.verificar_filme_em_cartaz(filme_id):
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
            QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'Nenhum filme com o ID especificado está em cartaz.')
            
    def Tela_Cliente_carregar_lista_completa_filmes_em_cartaz(self):
        filmes = dados_filme.obter_todos_filmes_em_cartaz()
        if filmes:
            model = QStringListModel()
            model.setStringList(filmes)
            self.TELA_CLIENTE_VER_FILMES_ui.listView.setModel(model)
                                

    def mudar_cor_red(self, button):
        op = QtWidgets.QMessageBox.question(
            self, 'Seleção', 'Finalizar escolha?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
        )
        if op == QtWidgets.QMessageBox.Yes:
            button.setStyleSheet("background-color: red;")
            self.QtStack.setCurrentIndex(11)

