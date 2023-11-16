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
from TELA_ESTATISTICA_ui import *#
from TELA_GERENCIAMENTO import *#
from TELA_GESTAO_FILMES_ui import *#
from TELA_CADASTRO_FILMES import *#
from TELA_LISTA_FILMES_ui import *#
from TELA_EXCLUIR_FILME_ui import *
from TELA_CLIENTE_VER_FILMES_ui import *
from classes.funcoes_aux import *

ip = '10.180.42.115'
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
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()


        self.tela_main_ui = Ui_Dialog()
        self.tela_main_ui.setupUi(self.stack0)

        self.TELA_CADASTRO_ui = Cadastrar()
        self.TELA_CADASTRO_ui.setupUi(self.stack1)


        self.TELA_USUARIO = Tela_usuario()
        self.TELA_USUARIO.setupUi(self.stack2)


        #Usa-se só para ajustar essa tela
        self.TELA_DPS_LOGIN_FUNC_ui = LOGIN_FUNC()
        self.TELA_DPS_LOGIN_FUNC_ui.setupUi(self.stack3)


        #tela estatistica
        self.TELA_ESTATISTICA_ui = Estatistica()
        self.TELA_ESTATISTICA_ui.setupUi(self.stack4)

        #tela gerenciamento
        self.TELA_GESTAO_FILMES_ui = GESTAO_FILMES()
        self.TELA_GESTAO_FILMES_ui.setupUi(self.stack5)

        self.TELA_CADASTRO_FILMES = Cadastrar_filme()
        self.TELA_CADASTRO_FILMES.setupUi(self.stack6)


        self.TELA_LISTA_FILMES_ui = Tela_Lista_Filmes()
        self.TELA_LISTA_FILMES_ui.setupUi(self.stack7)

        self.TELA_EXCUIR_FILME_ui = Excluir_Filme()
        self.TELA_EXCUIR_FILME_ui.setupUi(self.stack8)

        self.TELA_CLIENTE_VER_FILMES_ui = TELA_VER_FILMES()
        self.TELA_CLIENTE_VER_FILMES_ui.setupUi(self.stack9)


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
        self.TELA_USUARIO.pushButton_4.clicked.connect(self.VoltarMain)
        self.TELA_USUARIO.pushButton.clicked.connect(self.Tela_Cliente_Ver_Filmes)

        self.TELA_DPS_LOGIN_FUNC_ui.pushButton_4.clicked.connect(self.VoltarMain)
        self.TELA_DPS_LOGIN_FUNC_ui.pushButton.clicked.connect(self.Tela_Estatistica)
        self.TELA_DPS_LOGIN_FUNC_ui.pushButton_2.clicked.connect(self.TelaGestao)

        #tela estatistica
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


        #Tela_Listar_Filmes
        self.TELA_LISTA_FILMES_ui.pushButton_4.clicked.connect(self.TelaGestao)
        self.TELA_LISTA_FILMES_ui.listView.clicked.connect(self.item_selecionado_lista_filmes)
        self.TELA_LISTA_FILMES_ui.pushButton_2.clicked.connect(self.botao_buscar)
        self.TELA_LISTA_FILMES_ui.pushButton_5.clicked.connect(self.carregar_lista_completa_filmes)

        #Tela_Excluir_Filmes
        self.TELA_EXCUIR_FILME_ui.pushButton_4.clicked.connect(self.TelaGestao)
        self.TELA_EXCUIR_FILME_ui.listView.clicked.connect(self.item_selecionado_Excluir_filmes)
        self.TELA_EXCUIR_FILME_ui.pushButton_3.clicked.connect(self.botao_buscar_tela_ecluir)
        self.TELA_EXCUIR_FILME_ui.pushButton_9.clicked.connect(self.TelaVerTodosFilmes_Tela_excluir)


        ##TELA_USER_VER_FILMES
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton.clicked.connect(self.abrirTelaDPSLoginCli)
        #self.TELA_CLIENTE_VER_FILMES_ui.pushButton_2.clicked.connect(self.Tela_Cliente_botao_buscar)
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton_4.clicked.connect(self.Tela_Cliente_Ver_Filmes)
        self.TELA_CLIENTE_VER_FILMES_ui.listView.clicked.connect(self.item_selecionado_lista_filmes_cliente)
    
    def VoltarMain(self):
        self.QtStack.setCurrentIndex(0)

    def fecharAplicacao(self):
        client_socket.send('0'.encode())
        sys.exit()
    
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
            preco = preco_str
            if preco <= '0':
                QtWidgets.QMessageBox.information(self, 'erro', 'O preço deve ser maior que zero.')
            else:
                client_socket.send('3'.encode())
                lista_dados = list()
                lista_dados.append(nome_filme)
                lista_dados.append(ano_filme)
                lista_dados.append(preco)
                lista_dados.append(self.classificacao)
                lista_dados.append(horarios_str)
                dados = ",".join(lista_dados)
                client_socket.send(dados.encode())
                try:
                    retorno = client_socket.recv(4096).decode()
                except:
                    print("\nNao foi possivel permanecer conectado!\n")
                    client_socket.close()
                if retorno == '1':
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
    

        # Cliente
    def TelaVerTodosFilmes(self): 
        client_socket.send('4'.encode())  
        try:
            filmes = client_socket.recv(4096).decode()
        except:
            print("\nNão foi possível permanecer conectado!\n")
            client_socket.close()

        if filmes:
            model = QStringListModel()

            lista_filmes_formatada = tratar_retorno_filmes(filmes)

            model.setStringList(lista_filmes_formatada)

            self.TELA_LISTA_FILMES_ui.listView.setModel(model)

            self.QtStack.setCurrentIndex(7)
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
            
    def item_selecionado_lista_filmes(self, index):
        if index.isValid():
            item_selecionado = index.data()

            # Se o item for válido, você pode acessar o texto (nome do filme, neste caso)
            if item_selecionado:
                client_socket.send('5'.encode())
                partes = item_selecionado.split()

                filme_id = partes[1]
                client_socket.send(f'{filme_id}'.encode())
                try:
                    resposta = client_socket.recv(4096).decode()
                except:
                    print("\nNão foi possível permanecer conectado!\n")
                    client_socket.close()
                #print(f'retorno do servidor: {resposta}')
                if resposta == '0':
                    # Exiba um QMessageBox para confirmar a marcação do filme como "Em Cartaz"
                    reply = QMessageBox.question(
                        self,
                        'Cartaz',
                        f'Deseja colocar o filme com ID {filme_id} em cartaz?',
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No
                    )

                    #filme_id = int(filme_id)

                    if reply == QMessageBox.Yes:
                        client_socket.send('6'.encode())
                        client_socket.send(f'1 {filme_id}'.encode())
                        try:
                            resposta = client_socket.recv(4096).decode()
                        except:
                            print("\nNão foi possível permanecer conectado!\n")
                            client_socket.close()
                        if resposta == '1':
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Filme com ID {filme_id} marcado como em cartaz.')
                        else:
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Erro ao marcar o filme com ID {filme_id} como em cartaz.')
                        client_socket.send('4'.encode())
                        try:
                            filmes = client_socket.recv(4096).decode()
                        except:
                            print("\nNão foi possível permanecer conectado!\n")
                            client_socket.close()
                        if filmes:

                            model = QStringListModel()

                            lista_filmes_formatada = tratar_retorno_filmes(filmes)
                            model.setStringList(lista_filmes_formatada)
                            self.TELA_LISTA_FILMES_ui.listView.setModel(model)

                else:
                    QtWidgets.QMessageBox.information(self, 'Filme em Cartaz', 'Este filme já está em cartaz.')
        else:
            QtWidgets.QMessageBox.information(self, 'Itens Filme', 'Nenhum item selecionado.')
            
    def botao_buscar(self):
        client_socket.send('8'.encode())
        filme_id = self.TELA_LISTA_FILMES_ui.lineEdit_2.text()
        client_socket.send(filme_id.encode())

        try:
            resposta = client_socket.recv(4096).decode()
        except:
            print("\nNão foi possível permanecer conectado!\n")
            client_socket.close()
        if resposta == '1':
            print('Achou algo')
            filme_achado = client_socket.recv(4096).decode()
            #print(f"Achei esse oh: {filme_achado}")
            # Verificar se o filme foi encontrado
            if filme_achado:
                # Criar um modelo de lista
                model = QStringListModel()

                # Adicionar o nome do filme ao modelo
                model.setStringList([filme_achado])

                # Associar o modelo ao QListView
                self.TELA_LISTA_FILMES_ui.listView.setModel(model)
            else:
                QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'Nenhum filme com o ID especificado foi encontrado.')
        
    def carregar_lista_completa_filmes(self):
        client_socket.send('4'.encode())
        filmes = client_socket.recv(4096).decode()
        #print('Achei isso',filmes)
        if filmes:
            model = QStringListModel()

            lista_filmes_formatada = tratar_retorno_filmes(filmes)

            model.setStringList(lista_filmes_formatada)

            self.TELA_LISTA_FILMES_ui.listView.setModel(model)

            self.QtStack.setCurrentIndex(7)
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
        

    def TelaExcluiFilme(self):
        client_socket.send('7'.encode())  
        try:
            filmes = client_socket.recv(4096).decode()
            print('TELA CLI: ',filmes)
        except:
            print("\nNão foi possível permanecer conectado!\n")
            client_socket.close()
        if filmes == '0':
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
        else:
            if filmes:
                model = QStringListModel()

                lista_filmes_formatada = tratar_retorno_filmes(filmes)

                model.setStringList(lista_filmes_formatada)

                self.TELA_EXCUIR_FILME_ui.listView.setModel(model)

                self.QtStack.setCurrentIndex(8)
            else:
                QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
    

    def item_selecionado_Excluir_filmes(self, index):
        if index.isValid():
            item_selecionado = index.data()

            # Se o item for válido, você pode acessar o texto (nome do filme, neste caso)
            if item_selecionado:
                client_socket.send('5'.encode())
                # Divida a string do item selecionado para extrair o ID
                partes = item_selecionado.split()
                filme_id = partes[1]
                client_socket.send(f'{filme_id}'.encode())
                try:
                    resposta = client_socket.recv(4096).decode()
                except:
                    print("\nNão foi possível permanecer conectado!\n")
                    client_socket.close()
                #print(f'resposta do servidor: {resposta}')
                if resposta == '1':
                    reply = QMessageBox.question(
                        self,
                        'Cartaz',
                        f'Deseja retirar o filme com ID {filme_id} do cartaz?',
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No
                    )
                    if reply == QMessageBox.Yes:
                        client_socket.send('6'.encode())
                        client_socket.send(f'0 {filme_id}'.encode())
                        try:
                            resposta = client_socket.recv(4096).decode()
                        except:
                            print("\nNão foi possível permanecer conectado!\n")
                            client_socket.close()
                        if resposta == '1':
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Filme com ID {filme_id} retirado como em cartaz.')
                        else:
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Erro ao retirar o filme com ID {filme_id} como em cartaz.')
                        
                        client_socket.send('7'.encode())
                        try:
                            filmes = client_socket.recv(4096).decode()
                        except:
                            print("\nNão foi possível permanecer conectado!\n")
                            client_socket.close()
                        if filmes:

                            model = QStringListModel()

                            lista_filmes_formatada = tratar_retorno_filmes(filmes)
                            model.setStringList(lista_filmes_formatada)
                            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
                            
                        self.TELA_EXCUIR_FILME_ui.listView.setModel(model)

                else:
                    QtWidgets.QMessageBox.information(self, 'Filme Fora de Cartaz', 'Este filme não está mais em cartaz.')
        else:
            QtWidgets.QMessageBox.information(self, 'Itens Filme', 'Nenhum item selecionado.')
            
    def botao_buscar_tela_ecluir(self):
        client_socket.send('8'.encode())
        filme_id = self.TELA_EXCUIR_FILME_ui.lineEdit_4.text()
        client_socket.send(filme_id.encode())

        try:
            resposta = client_socket.recv(4096).decode()
        except:
            print("\nNão foi possível permanecer conectado!\n")
            client_socket.close()
            
        if resposta == '1':
            print('Achou algo')
            filme_achado = client_socket.recv(4096).decode()
            #print(f"Achei esse oh: {filme_achado}")
            # Verificar se o filme foi encontrado
            if filme_achado:
                # Criar um modelo de lista
                model = QStringListModel()

                # Adicionar o nome do filme ao modelo
                model.setStringList([filme_achado])

                # Associar o modelo ao QListView
                self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
            else:
                QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'Nenhum filme com o ID especificado foi encontrado.')
                
    def TelaVerTodosFilmes_Tela_excluir(self):
        client_socket.send('4'.encode())
        # Obtenha a lista de filmes do banco de dados
        filmes = client_socket.recv(4096).decode()
        #print('Achei isso',filmes)
        if filmes:
            model = QStringListModel()

            lista_filmes_formatada = tratar_retorno_filmes(filmes)

            model.setStringList(lista_filmes_formatada)

            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)

            self.QtStack.setCurrentIndex(8)
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
    

    def Tela_Cliente_Ver_Filmes(self):
    # Obtenha a lista de filmes do banco de dados
        client_socket.send('9'.encode())
        try:
            filmes = client_socket.recv(4096).decode()
        except:
            print("\nNão foi possível permanecer conectado!\n")
            client_socket.close()
        if filmes:
            model = QStringListModel()
            lista_filmes_formatada = tratar_retorno_filmes(filmes)
            model.setStringList(lista_filmes_formatada)
            self.TELA_CLIENTE_VER_FILMES_ui.listView.setModel(model)
            self.QtStack.setCurrentIndex(9)  # Altere o índice para a tela do cliente
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes em cartaz.')
    

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
                    client_socket.send('10'.encode())
                    client_socket.send(f'{filme_id}'.encode())
                    try:
                        horarios = client_socket.recv(4096).decode()
                    except:
                        print("\nNão foi possível permanecer conectado!\n")
                        client_socket.close()
                    if horarios:
                        horarios_list = horarios.split(',')
                        horario_selecionado, ok = QInputDialog.getItem(self, 'Seleção', 'Selecione o horário:', horarios_list, 0, False)

                    if not ok:
                        QtWidgets.QMessageBox.information(self, 'Seleção', 'Compra cancelada.')
                        return

                    '''self.dados_clienete.append(horario_selecionado)
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
                    QtWidgets.QMessageBox.information(self, 'Itens Filme', 'Nenhum item selecionado.')'''
            else:
                QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Nenhum filme selecionado.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Ui_Main()
    sys.exit(app.exec_())
