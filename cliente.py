import sys
import socket
import random
import math
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QInputDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QStringListModel
from tela_main_ui import *#
from TELA_CADASTRO_ui import *#
from TELA_DPS_LOGIN_ui import *#
from TELA_GERENCIAMENTO_ui import *#
from TELA_ESTATISTICA_ui import *#
from TELA_GESTAO_FILMES_ui import *#
from TELA_CADASTRO_FILMES import *#
from TELA_LISTA_FILMES_ui import *#
from TELA_EXCLUIR_FILME_ui import *
from TELA_EXCLUIR_RESERVA_ui import *
from TELA_CLIENTE_VER_FILMES_ui import *
from TELA_LAYOUT import *
from TELA_PAGAMENTO import *
from TELA_LAYOUT_02 import *
from TELA_LAYOUT_03 import *
from Cartao_ui import *
from classes.funcoes_aux import *


ip = '10.180.42.249'
porta = 8007
addr = ((ip,porta))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(addr)
except Exception as e:
    exit()


class Main(QtWidgets.QWidget):
    """
    Uma classe que representa a janela principal da aplicação com um layout empilhado para alternar entre diferentes telas.
    ----------

    """
    def setupUi(self, Main):
        """
        Configura a interface do usuário para a janela principal da aplicação, incluindo várias telas empilhadas.
        ----------

        """
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
        self.stack12 = QtWidgets.QMainWindow()
        self.stack13 = QtWidgets.QMainWindow()
        self.stack14 = QtWidgets.QMainWindow()
        self.stack15 = QtWidgets.QMainWindow()


        self.tela_main_ui = Ui_Dialog()
        self.tela_main_ui.setupUi(self.stack0)

        self.TELA_CADASTRO_ui = Cadastrar()
        self.TELA_CADASTRO_ui.setupUi(self.stack1)


        self.TELA_DPS_LOGIN_ui = Tela_Usuario()
        self.TELA_DPS_LOGIN_ui.setupUi(self.stack2)


        #Usa-se só para ajustar essa tela
        self.TELA_GERENCIAMENTO_ui = LOGIN_FUNC()
        self.TELA_GERENCIAMENTO_ui.setupUi(self.stack3)


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


        self.TELA_LAYOUT = Tela_layout()
        self.TELA_LAYOUT.setupUi(self.stack10)

        self.TELA_PAGAMENTO = Tela_pagamento()
        self.TELA_PAGAMENTO.setupUi(self.stack11)
        
        self.Cartao_ui = EscolheuCartao()
        self.Cartao_ui.setupUi(self.stack12)

        self.TELA_LAYOUT_02 = Tela_layout_02()
        self.TELA_LAYOUT_02.setupUi(self.stack13)

        self.TELA_LAYOUT_03 = Tela_layout_03()
        self.TELA_LAYOUT_03.setupUi(self.stack14)
        
        self.TELA_EXCLUIR_RESERVA_ui = Tela_Excluir_Reserva()
        self.TELA_EXCLUIR_RESERVA_ui.setupUi(self.stack15)
        
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
        self.QtStack.addWidget(self.stack12)
        self.QtStack.addWidget(self.stack13)
        self.QtStack.addWidget(self.stack14)
        self.QtStack.addWidget(self.stack15)


class Ui_Main(QMainWindow, Main):
    """
    Uma classe de interface do usuário para a aplicação principal, que herda de QMainWindow e Main.
    
    Attributes
    ----------
        horarios_selecionados : list
            Uma lista que recebe os horarios selecionados pelo cliente
        classificacao : str
            É um tipo string vazio que vai receber a classificação
        dados_clienete : list
            Uma lista que recebe os dados do cliente
        saida : str
            É um tipo string que vai receber a saida
        cpf_do_usuario : str
            É um tipo string que vai receber o CPF do usuario logado
        itens_filme : str
            É um tipo string que recebe o itens do filme 
        horarios_cliente : str
            É um tipo string que recebe os horarios selecionados
        resposta : str
            É um tipo string que recebe uma resposta
        total_compra : str
            É um tipo string que recebe o total da compra
        botao_id : str
            É um tipo string que recebe um id de um botão
        tela_para_exibir : str
            É um tipo string que pega a tela atual que o usuario esta usando
        frequencia_valores : dict
            É um tipo dicionario que pega a frequencia de valores na tela 1
        frequencia_valores_02 : dict
            É um tipo dicionario que pega a frequencia de valores na tela 2
        frequencia_valores_03 : dict
            É um tipo dicionario que pega a frequencia de valores na tela 3
            
    Methods
    -------
    VoltarMain
        Volta para a tela principal da aplicação.
    fecharAplicacao
        Fecha a aplicação, enviando um sinal para o socket do cliente e encerrando o programa.
    abrirTelaCadastro
        Abre a tela de cadastro da aplicação.
    abrirLoginFunc
        Abre a tela de Login do Gerente.
    TelaGestao
        Abre a tela de Gestao.
    TelaCadastraFilme
        Abre a tela de cadastro para o filme.
    escolhe_lugar
        Abre a tela de Escolher lugar.
    escolher_horarios
        Abre a tela de Escolher Horarios.
    escolheuCartao
        Abre a tela de Escolher cartão.
    botao_ok
        Confirma os dados digitados e realiza a autenticação do usuário.
        Se o login for bem-sucedido, direciona para a tela após o login correspondente
        (cliente ou gerente) e exibe as informações do usuário autenticado.
    abrirTelaDPSLoginCli
        Abre a tela correspondente aos clientes após o login.
    botao_Cadastra
        Realiza o cadastro do usuário com base nos dados fornecidos.
        Exibe mensagens de erro se os dados não forem válidos ou se o CPF já estiver cadastrado.
    botao_cadastrar_filme
        Realiza o cadastro de um filme com base nos dados fornecidos, incluindo horários e classificação.
        Exibe mensagens de erro se os dados não forem válidos ou se o cadastro do filme falhar.
    adicionar_horarios
        Adiciona os horários selecionados à lista de horários para o cadastro de filmes.
        Obtém o horário, tipo de filme e língua escolhidos pelo usuário na interface gráfica,
        cria uma tupla representando essa escolha e a adiciona à lista de horários selecionados.
        Atualiza a visualização na interface gráfica com os horários selecionados.
        Exibe uma mensagem de erro se nenhum horário for selecionado.
    adicionar_classificacao
        Adiciona a classificação na tela e mostra para o usuario escolher.
    TelaVerTodosFilmes
        Envia uma solicitação para o servidor para obter a lista de todos os filmes cadastrados
        e exibe a lista na tela correspondente. Se não houver filmes cadastrados, exibe uma mensagem informando isso.
    item_selecionado_lista_filmes(self, index)
        Método usado para o gerente adicionar um filme em cartaz
    botao_buscar(self)
        Método usado para buscar um determinado filme
    carregar_lista_completa_filmes(self)
        Método usado para exibir todos os filmes cadastrados
    carregar_filmes_em_cartaz(self)
        Método usado para exibir todos os filmes em cartaz
    item_selecionado_Excluir_filmes(self, index)
        Método usado para o gerente retirar um filme do cartaz
    botao_buscar_tela_excluir(self)
        Método usado para exibir todos os filmes em cartaz
    Tela_Cliente_Ver_Filmes(self)
        Método usado para exibir todos os filmes em cartaz para o cliente
    item_selecionado_lista_filmes_cliente(self, index)
        Método usado para o cliente selecionar um filme que deseja comprar e escolher sua poltrona
    Tela_Cliente_botao_buscar(self)
        Método usado para buscar um filme para o cliente
    ir_tela_pagamento(self, button)
    escolheuPix(self)
        Método que representa a forma de pagamento pix e faz a soma da compra além de enviar o comprovante por e-mail
    botaoconfirmartelacartao(self)
        Método que representa a forma de pagamento pix e faz a soma da compra além de enviar o comprovante por e-mail
    ir_tela_Excluir_Reserva(self)
        Método que exibe todas as poltronas para o cliente excluir
    item_selecionado_Excluir_Reserva(self, index)
        Método usado para o cliente selecionar uma poltrona e excluir sua reserva
    Tela_Estatistica(self)
        Método usado para exibir todos os dados de compra para o gerente
    """
    def __init__(self):
        
        super(Main, self).__init__(None)
        self.setupUi(self)
        self.horarios_selecionados = list()
        self.classificacao = ''
        self.dados_clienete = list()
        self.saida = None
        self.cpf_do_usuario = None
        self.itens_filme = ''
        self.horarios_cliente = ''
        self.resposta = None
        self.total_compra = None
        self.botao_id = None
        self.tela_para_exibir = None
        self.frequencia_valores = dict()
        self.frequencia_valores_02 = dict()
        self.frequencia_valores_03 = dict()

    
        #tela principal
        self.tela_main_ui.pushButton_3.clicked.connect(self.fecharAplicacao)
        self.tela_main_ui.pushButton_4.clicked.connect(self.abrirTelaCadastro)
        self.tela_main_ui.pushButton.clicked.connect(self.botao_ok)

        #tela cadastro cliente
        self.TELA_CADASTRO_ui.pushButton_3.clicked.connect(self.VoltarMain)
        self.TELA_CADASTRO_ui.pushButton.clicked.connect(self.botao_Cadastra)
        

        ##TELA_CLIENTES
        self.TELA_DPS_LOGIN_ui.pushButton_4.clicked.connect(self.VoltarMain)
        self.TELA_DPS_LOGIN_ui.pushButton.clicked.connect(self.Tela_Cliente_Ver_Filmes)
        self.TELA_DPS_LOGIN_ui.pushButton_3.clicked.connect(self.ir_tela_Excluir_Reserva)
        

        self.TELA_GERENCIAMENTO_ui.pushButton_4.clicked.connect(self.VoltarMain)
        self.TELA_GERENCIAMENTO_ui.pushButton.clicked.connect(self.Tela_Estatistica)
        self.TELA_GERENCIAMENTO_ui.pushButton_2.clicked.connect(self.TelaGestao)

        #tela estatistica
        self.TELA_ESTATISTICA_ui.pushButton_4.clicked.connect(self.abrirLoginFunc)
        
        #Tela_Gestao
        self.TELA_GESTAO_FILMES_ui.pushButton_4.clicked.connect(self.abrirLoginFunc)
        self.TELA_GESTAO_FILMES_ui.pushButton_3.clicked.connect(self.TelaCadastraFilme)
        self.TELA_GESTAO_FILMES_ui.pushButton_2.clicked.connect(self.carregar_filmes_em_cartaz)
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
        self.TELA_EXCUIR_FILME_ui.pushButton_3.clicked.connect(self.botao_buscar_tela_excluir)
        self.TELA_EXCUIR_FILME_ui.pushButton_9.clicked.connect(self.carregar_filmes_em_cartaz)


        ##TELA_USER_VER_FILMES
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton.clicked.connect(self.abrirTelaDPSLoginCli)
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton_2.clicked.connect(self.Tela_Cliente_botao_buscar)
        self.TELA_CLIENTE_VER_FILMES_ui.pushButton_4.clicked.connect(self.Tela_Cliente_Ver_Filmes)
        self.TELA_CLIENTE_VER_FILMES_ui.listView.clicked.connect(self.item_selecionado_lista_filmes_cliente)


        buttons_and_functions = lista_botoes_red(self)

        for button, function in buttons_and_functions:
            button.clicked.connect(lambda _, btn=button: function(btn))
        
        buttons_and_functions_02 = lista_botoes_red_02(self)
        for button, function in buttons_and_functions_02:
            button.clicked.connect(lambda _, btn=button: function(btn))
        
        buttons_and_functions_03 = lista_botoes_red_03(self)
        for button, function in buttons_and_functions_03:
            button.clicked.connect(lambda _, btn=button: function(btn))

            

        #tela layout
        self.TELA_LAYOUT.pushButton_2.clicked.connect(self.Tela_Cliente_Ver_Filmes)

        #tela layout_02
        self.TELA_LAYOUT_02.pushButton_2.clicked.connect(self.Tela_Cliente_Ver_Filmes)

        #tela layout_03
        self.TELA_LAYOUT_03.pushButton_2.clicked.connect(self.Tela_Cliente_Ver_Filmes)

        #TELA PAGAMENTO
        self.TELA_PAGAMENTO.pushButton_4.clicked.connect(self.Tela_Cliente_Ver_Filmes)
        self.TELA_PAGAMENTO.pushButton.clicked.connect(self.escolheuCartao)
        self.TELA_PAGAMENTO.pushButton_3.clicked.connect(self.escolheuPix)
        
        #TELA_CARTAO
        self.Cartao_ui.pushButton_2.clicked.connect(self.escolher_horarios)
        self.Cartao_ui.pushButton.clicked.connect(self.botaoconfirmartelacartao)
        
        ##TELA_CLIENTES_EXCLUIR_RESERVA
        self.TELA_EXCLUIR_RESERVA_ui.pushButton.clicked.connect(self.abrirTelaDPSLoginCli)
        self.TELA_EXCLUIR_RESERVA_ui.listView.clicked.connect(self.item_selecionado_Excluir_Reserva)
        
    
    def VoltarMain(self):
        """
        Volta para a tela principal da aplicação.
        """
        self.QtStack.setCurrentIndex(0)

    def fecharAplicacao(self):
        """
        Fecha a aplicação, enviando um sinal para o socket do cliente e encerrando o programa.
        """
        client_socket.send('0'.encode())
        sys.exit()
    
    def abrirTelaCadastro(self):
        """
        Abre a tela de cadastro da aplicação.
        """
        self.QtStack.setCurrentIndex(1)
    
    def abrirLoginFunc(self):
        """
        Abre a tela de Login do Gerente.
        """
        self.QtStack.setCurrentIndex(3)
    
    def TelaGestao(self):
        """
        Abre a tela de Gestao.
        """
        self.QtStack.setCurrentIndex(5)
    
    def TelaCadastraFilme(self):
        """
        Abre a tela de cadastro para o filme.
        """
        self.QtStack.setCurrentIndex(6)
        
    def escolhe_lugar(self):
        """
        Abre a tela de Escolher lugar.
        """
        self.QtStack.setCurrentIndex(10)
        
    def escolher_horarios(self):
        """
        Abre a tela de Escolher Horarios.
        """
        self.QtStack.setCurrentIndex(11)
        
    def escolheuCartao(self):
        """
        Abre a tela de Escolher cartão.
        """
        self.QtStack.setCurrentIndex(12)
        
    
    def botao_ok(self):
        """
        Confirma os dados digitados e realiza a autenticação do usuário.
        Se o login for bem-sucedido, direciona para a tela após o login correspondente
        (cliente ou gerente) e exibe as informações do usuário autenticado.
        """
        cpf = self.tela_main_ui.lineEdit_2.text()
        self.cpf_do_usuario = cpf
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
                client_socket.close()
            if retorno == '1':
                nome_achado = client_socket.recv(4096).decode()
                if nome_achado != None:
                    self.saida = nome_achado
                QtWidgets.QMessageBox.information(self, 'login', 'Login cliente realizado com sucesso.')
                print('cpf user:',self.cpf_do_usuario)
                client_socket.send('23'.encode())
                client_socket.send(self.cpf_do_usuario.encode())
                nome_pessoa = client_socket.recv(4096).decode()
                self.TELA_DPS_LOGIN_ui.label_4.setText(nome_pessoa)
                self.QtStack.setCurrentIndex(2)
            elif retorno == '3':
                QtWidgets.QMessageBox.information(self, 'login', 'Login gerente realizado com sucesso.')
                print('cpf user:',self.cpf_do_usuario)
                client_socket.send('23'.encode())
                client_socket.send(self.cpf_do_usuario.encode())
                nome_pessoa = client_socket.recv(4096).decode()
                self.TELA_GERENCIAMENTO_ui.label_4.setText(nome_pessoa)
                self.QtStack.setCurrentIndex(3)
            else:
                QMessageBox.information(self, 'erro', 'Preencha os dados corretamente.!')
            
        self.tela_main_ui.lineEdit_2.setText('')
        self.tela_main_ui.lineEdit.setText('')
    
    
    def abrirTelaDPSLoginCli(self):
        """
        Abre a tela correspondente aos clientes após o login.
        """
        self.QtStack.setCurrentIndex(2)
    
        
    
    def botao_Cadastra(self):
        """
        Realiza o cadastro do usuário com base nos dados fornecidos.
        Exibe mensagens de erro se os dados não forem válidos ou se o CPF já estiver cadastrado.
        """
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
        """
        Realiza o cadastro de um filme com base nos dados fornecidos, incluindo horários e classificação.
        Exibe mensagens de erro se os dados não forem válidos ou se o cadastro do filme falhar.
        """
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
        horarios_str = ', '.join([f'{horario} - {tipo} - {lingua}' for horario, tipo, lingua in self.horarios_selecionados])
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
        """
        Adiciona os horários selecionados à lista de horários para o cadastro de filmes.
        
        Obtém o horário, tipo de filme e língua escolhidos pelo usuário na interface gráfica,
        cria uma tupla representando essa escolha e a adiciona à lista de horários selecionados.
        
        Atualiza a visualização na interface gráfica com os horários selecionados.
        
        Exibe uma mensagem de erro se nenhum horário for selecionado.
        """
        horario = self.TELA_CADASTRO_FILMES.dateTimeEdit.text()
        tipo_filme = self.TELA_CADASTRO_FILMES.comboBox.currentText()
        lingua = self.TELA_CADASTRO_FILMES.comboBox_2.currentText()

        if horario:
            # Adicione o par horário-tipo à lista de tuplas
            horario_tipo_tuple = (horario, tipo_filme, lingua)
            self.horarios_selecionados.append(horario_tipo_tuple)

            # Crie uma lista de strings para representar os pares horário-tipo
            horarios_strings = [f'{h} - {t} - {u}' for h, t, u in self.horarios_selecionados]

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
        """
        Adiciona a classificação na tela e mostra para o usuario escolher.
        """
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
        """
        Envia uma solicitação para o servidor para obter a lista de todos os filmes cadastrados
        e exibe a lista na tela correspondente. Se não houver filmes cadastrados, exibe uma mensagem informando isso.
        """
        client_socket.send('4'.encode())  
        try:
            filmes = client_socket.recv(4096).decode()
        except:
            client_socket.close()

        if filmes != '0':
            model = QStringListModel()

            lista_filmes_formatada = tratar_retorno_filmes(filmes)

            model.setStringList(lista_filmes_formatada)

            self.TELA_LISTA_FILMES_ui.listView.setModel(model)

            self.QtStack.setCurrentIndex(7)
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
            
###############################################################################################################
            
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
                    client_socket.close()

                if resposta == '0':
                    # Verificar se há um filme em cartaz
                    client_socket.send('7'.encode())
                    try:
                        resposta_em_cartaz = client_socket.recv(4096).decode()
                    except:
                        client_socket.close()

                    if resposta_em_cartaz == '0':
                        # Não há filme em cartaz, pode marcar o filme selecionado
                        reply = QMessageBox.question(
                            self,
                            'Cartaz',
                            f'Deseja colocar o filme com ID {filme_id} em cartaz?',
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No
                        )

                        if reply == QMessageBox.Yes:
                            client_socket.send('6'.encode())
                            client_socket.send(f'1 {filme_id}'.encode())
                            try:
                                resposta = client_socket.recv(4096).decode()
                            except:
                                client_socket.close()

                            if resposta == '1':
                                QtWidgets.QMessageBox.information(self, 'Filmes', f'Filme com ID {filme_id} marcado como em cartaz.')
                            else:
                                QtWidgets.QMessageBox.information(self, 'Filmes', f'Erro ao marcar o filme com ID {filme_id} como em cartaz.')
                            client_socket.send('4'.encode())
                            try:
                                filmes = client_socket.recv(4096).decode()
                            except:
                                client_socket.close()

                            if filmes:
                                model = QStringListModel()
                                lista_filmes_formatada = tratar_retorno_filmes(filmes)
                                model.setStringList(lista_filmes_formatada)
                                self.TELA_LISTA_FILMES_ui.listView.setModel(model)

                    else:
                        QtWidgets.QMessageBox.information(self, 'Filme em Cartaz', 'Já existe um filme em cartaz. Não é possível marcar outro.')
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
            
            client_socket.close()
        if resposta == '1':
            filme_achado = client_socket.recv(4096).decode()
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
        if filmes:
            model = QStringListModel()

            lista_filmes_formatada = tratar_retorno_filmes(filmes)

            model.setStringList(lista_filmes_formatada)

            self.TELA_LISTA_FILMES_ui.listView.setModel(model)

            self.QtStack.setCurrentIndex(7)
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes cadastrados.')
        

    def carregar_filmes_em_cartaz(self):
        client_socket.send('7'.encode())  
        try:
            filmes = client_socket.recv(4096).decode()
        except:
            
            client_socket.close()
        if filmes == '0':
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Não há filmes em cartaz.')
        else:
            model = QStringListModel()

            lista_filmes_formatada = tratar_retorno_filmes(filmes)

            model.setStringList(lista_filmes_formatada)

            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)

            self.QtStack.setCurrentIndex(8)
    

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
                    
                    client_socket.close()
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
                            
                            client_socket.close()
                        if resposta == '1':
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Filme com ID {filme_id} retirado como em cartaz.')
                        else:
                            QtWidgets.QMessageBox.information(self, 'Filmes', f'Erro ao retirar o filme com ID {filme_id} como em cartaz.')
                        
                        client_socket.send('7'.encode())
                        try:
                            filmes = client_socket.recv(4096).decode()
                        except:
                            
                            client_socket.close()
                        if filmes != '0':

                            model = QStringListModel()
                            lista_filmes_formatada = tratar_retorno_filmes(filmes)
                            model.setStringList(lista_filmes_formatada)
                            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
                            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
                        else:
                            QtWidgets.QMessageBox.information(self, 'Itens Filme', 'Nenhum filme em cartaz.')
                            self.QtStack.setCurrentIndex(5)
                else:
                    QtWidgets.QMessageBox.information(self, 'Filme Fora de Cartaz', 'Este filme não está mais em cartaz.')
        else:
            QtWidgets.QMessageBox.information(self, 'Itens Filme', 'Nenhum item selecionado.')
            
    def botao_buscar_tela_excluir(self):
        client_socket.send('9'.encode())
        filme_id = self.TELA_EXCUIR_FILME_ui.lineEdit_4.text()
        client_socket.send(filme_id.encode())

        try:
            resposta = client_socket.recv(4096).decode()
        except:
            
            client_socket.close()
            
        if resposta == '1':
            filme_achado = client_socket.recv(4096).decode()
            model = QStringListModel()
            model.setStringList([filme_achado])
            self.TELA_EXCUIR_FILME_ui.listView.setModel(model)
        else:
            QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'Nenhum filme com o ID especificado foi encontrado.')
                
    def Tela_Cliente_Ver_Filmes(self):
    # Obtenha a lista de filmes do banco de dados
        client_socket.send('7'.encode())
        try:
            filmes = client_socket.recv(4096).decode()
        except:
            
            client_socket.close()
        if filmes != '0':
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
            if item_selecionado:
                filme_selecionado = item_selecionado.split()
                partes = enxugar_string(filme_selecionado)
                filme_id = partes[1]
                preco_inicio = partes.index('Preço:') + 1
                proximo_index = partes.index('Classificação:') if 'Classificação:' in partes else len(partes)
                preco_filme = ''.join(partes[preco_inicio:proximo_index])
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
                        
                        client_socket.close()
                    if horarios:
                        horarios_list = horarios.split(',')
                        horario_selecionado, ok = QInputDialog.getItem(self, 'Seleção', 'Selecione o horário:', horarios_list, 0, False)

                    if not ok:
                        QtWidgets.QMessageBox.information(self, 'Seleção', 'Compra cancelada.')
                        return
                    
                    meia = QtWidgets.QMessageBox.question(
                    self, 'Seleção', 'meia entrada?',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
                    )
                    if meia == QtWidgets.QMessageBox.Yes:
                        meia_entrada = float(preco_filme)
                        self.total_compra = meia_entrada / 2
                    else:
                        self.total_compra = float(preco_filme)
                        

                    # O usuário selecionou um horário
                    reply1 = QtWidgets.QMessageBox.question(
                        self, 'Seleção', 'Deseja comprar o ingresso para esse filme?',
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                        QtWidgets.QMessageBox.No
                    )
                    # Verifique a resposta do usuário
                    if reply1 == QtWidgets.QMessageBox.Yes:
                        if horario_selecionado == horarios_list[0]:
                            self.tela_para_exibir = 10
                        elif horario_selecionado == horarios_list[1]:
                            self.tela_para_exibir = 13
                        elif horario_selecionado == horarios_list[2]:
                            self.tela_para_exibir = 14

                        self.itens_filme = partes
                        self.horarios_cliente = horario_selecionado
                        client_socket.send('15'.encode()) #sinal para pegar a lista de botoes que estão no servidor
                        tela = str(self.tela_para_exibir)
                        client_socket.send(tela.encode()) 
                        try:
                            mensagem = client_socket.recv(4096).decode()
                        except:
                            
                            client_socket.close()
                        if mensagem == '1': # encontrei os botoes
                            botoa_achado = client_socket.recv(4096).decode()
                            botoes_tela_lay = lista_botoes_tela_layout(self, self.tela_para_exibir)
                            mudar_cor_botao_vermelho_valido(botoes_tela_lay, botoa_achado) # esta em funções aux.py
                        if self.tela_para_exibir == 10:
                            self.QtStack.setCurrentIndex(10)
                        elif self.tela_para_exibir == 13:
                            self.QtStack.setCurrentIndex(13)
                        elif self.tela_para_exibir == 14:
                            self.QtStack.setCurrentIndex(14)
                else:
                    QtWidgets.QMessageBox.information(self, 'Itens Filme', 'Nenhum item selecionado.')
            else:
                QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Nenhum filme selecionado.')
    
    def Tela_Cliente_botao_buscar(self):
        client_socket.send('9'.encode())
        filme_id = self.TELA_CLIENTE_VER_FILMES_ui.lineEdit_2.text()
        client_socket.send(filme_id.encode())

        try:
            resposta = client_socket.recv(4096).decode()
        except:
            
            client_socket.close()
            
        if resposta == '1':
            filme_achado = client_socket.recv(4096).decode()
            model = QStringListModel()
            model.setStringList([filme_achado])
            self.TELA_CLIENTE_VER_FILMES_ui.listView.setModel(model)
        else:
            QtWidgets.QMessageBox.information(self, 'Buscar Filme', 'Nenhum filme com o ID especificado foi encontrado.')      
    
            
    def ir_tela_pagamento(self, button):
        op = QtWidgets.QMessageBox.question(
            self, 'Seleção', 'Finalizar escolha?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
        )
        if op == QtWidgets.QMessageBox.Yes:
            if self.tela_para_exibir == 10:
                self.botao_id = button.objectName() 
                client_socket.send('12'.encode())
                client_socket.send(self.botao_id.encode())
                # self.soma_tela_1 += self.total_compra
            elif self.tela_para_exibir == 13:
                self.botao_id = button.objectName() 
                client_socket.send('16'.encode())
                client_socket.send(self.botao_id.encode())
                # self.soma_tela_2 += self.total_compra
            elif self.tela_para_exibir == 14:
                self.botao_id = button.objectName() 
                client_socket.send('18'.encode())
                client_socket.send(self.botao_id.encode())
            try:
                resposta = client_socket.recv(4096).decode()
            except:
                
                client_socket.close()   
                
            if resposta == '2':
                  QtWidgets.QMessageBox.information(self, 'Compra', 'Acento ja escolhido.')
            else:
                self.QtStack.setCurrentIndex(11)#TELA PAGAMENTO

            
    def escolheuPix(self):
        cpf = self.cpf_do_usuario
        client_socket.send('11'.encode())
        client_socket.send(cpf.encode())
        email = client_socket.recv(4096).decode()
        # Gerar um número aleatório de 10 dígitos para simular um número de Pix
        numero_pix = str(random.randint(10**9, 10**10 - 1))

        info_dialog = QMessageBox()
        info_dialog.setIcon(QMessageBox.Information)
        info_dialog.setText("Escolheu Pix!")
        info_dialog.setInformativeText(f"Você escolheu a opção de pagamento Pix.\nChave Pix: {numero_pix}")
        info_dialog.setWindowTitle("Pagamento Pix")
        info_dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)


        # Exiba o QMessageBox
        result = info_dialog.exec_()

        # Após a confirmação, vá para a próxima tela
        if result == QMessageBox.Ok:
            self.dados_clienete.append(self.saida)
            self.dados_clienete.append(self.itens_filme[3])
            self.dados_clienete.append(self.itens_filme[5])
            self.dados_clienete.append(self.itens_filme[7])
            self.dados_clienete.append(self.itens_filme[9])
            self.dados_clienete.append(self.horarios_cliente)
            mensagem = formatar_mensagem(self.dados_clienete, self.total_compra, self.tela_para_exibir)
                
            EnviaEmail(email,mensagem)
            QtWidgets.QMessageBox.information(self, 'Opção de Pagamento', f'Obrigado pela compra, comprovante enviado por email')
            self.dados_clienete.clear()
            botoes_tela_lay = lista_botoes_tela_layout(self, self.tela_para_exibir)
            processar_dados_do_botao(client_socket, self.tela_para_exibir, self.botao_id, botoes_tela_lay)
            chave = self.total_compra
            atualizar_frequencia(self, chave, self.tela_para_exibir)
            valores = list()
            total = total_02 = total_03 = 0.0
            for i, v in self.frequencia_valores.items():
                total += i * v["frequencia"]
            for i, v in self.frequencia_valores_02.items():
                total_02 += i * v["frequencia"]
            for i, v in self.frequencia_valores_03.items():
                total_03 += i * v["frequencia"]
            valores.append(str(total))
            valores.append(str(total_02))
            valores.append(str(total_03))
            enviar = ','.join(valores)
            client_socket.send('22'.encode())
            client_socket.send(enviar.encode())
            
            
        self.QtStack.setCurrentIndex(2)
        
        
    def botaoconfirmartelacartao(self):
        valid = cancelou = False
        nome_cliente = self.Cartao_ui.lineEdit.text()
        numero_cartao = self.Cartao_ui.lineEdit_5.text()
        cvv = self.Cartao_ui.lineEdit_3.text()
        minimum_date = QtCore.QDate(1800, 9, 14)
        if nome_cliente == '' or numero_cartao == '' or cvv == '':
            QtWidgets.QMessageBox.information(self, 'Cartão', 'digite valores validos.')
        elif not verificar_nome(nome_cliente):
            QtWidgets.QMessageBox.information(self, 'Cartão', 'nome invalido.')
        elif not verificar_valor_inteiro(numero_cartao) or not verificar_valor_inteiro(cvv):
            QtWidgets.QMessageBox.information(self, 'Cartão', 'numero de cartão ou cvv invalido.')
        else:
            opc_cartao = None
            cpf = self.cpf_do_usuario
            client_socket.send('11'.encode())
            client_socket.send(cpf.encode())
            email = client_socket.recv(4096).decode()
            parcelas = 1
            op = self.Cartao_ui.comboBox.currentText()
            if op == 'DEBITO':
                opc_cartao = 2
            if op == 'CREDITO':
                opc_cartao = 3
                valores = list()
                max_parcelas = 3  # Quantidade máxima de parcelas
                for parcela in range(1, min(max_parcelas, math.ceil(self.total_compra / 20)) + 1):
                    valores.append(parcela)
                parcelas, ok = QInputDialog.getItem(self, 'Seleção', 'selecione a parcela', [str(valor) for valor in valores], 0, False)
                valor_parcelado = self.total_compra / float(parcelas)
                escolha = QMessageBox.question(
                self,
                'Compra',
                f'Compra dividido em {parcelas}X ficou {valor_parcelado:.2f} reais',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
                )
                if escolha == QtWidgets.QMessageBox.No: 
                    cancelou = True
            if not cancelou:
                op1 = QtWidgets.QMessageBox.question(
                self, 'Seleção', f'Tem Certeza que deseja fazer a compra no {op}?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
                )
                if op1 == QtWidgets.QMessageBox.Yes:    
                    self.dados_clienete.append(self.saida)
                    self.dados_clienete.append(self.itens_filme[3])
                    self.dados_clienete.append(self.itens_filme[5])
                    self.dados_clienete.append(self.itens_filme[7])
                    self.dados_clienete.append(self.itens_filme[9])
                    self.dados_clienete.append(self.horarios_cliente)  
                    mensagem = formatar_mensagem(self.dados_clienete, self.total_compra, self.tela_para_exibir, opc_cartao, parcelas)
                    EnviaEmail(email,mensagem)  
                    self.dados_clienete.clear()
                    QtWidgets.QMessageBox.information(self, 'Opção de Pagamento', f'Obrigado pela compra, comprovante enviado por email')
                    valid = True
                    botoes_tela_lay = lista_botoes_tela_layout(self, self.tela_para_exibir)
                    processar_dados_do_botao(client_socket, self.tela_para_exibir, self.botao_id, botoes_tela_lay)
                    chave = self.total_compra
                    atualizar_frequencia(self, chave, self.tela_para_exibir)
                    valores = list()
                    total = total_02 = total_03 = 0.0
                    for i, v in self.frequencia_valores.items():
                        total += i * v["frequencia"]
                    for i, v in self.frequencia_valores_02.items():
                        total_02 += i * v["frequencia"]
                    for i, v in self.frequencia_valores_03.items():
                        total_03 += i * v["frequencia"]
                    valores.append(str(total))
                    valores.append(str(total_02))
                    valores.append(str(total_03))
                    enviar = ','.join(valores)
                    client_socket.send('22'.encode())
                    client_socket.send(enviar.encode())
        if valid:  
            self.QtStack.setCurrentIndex(2)
            self.Cartao_ui.lineEdit.setText('')
            self.Cartao_ui.lineEdit_5.setText('')
            self.Cartao_ui.lineEdit_3.setText('')
            self.Cartao_ui.dateEdit.setDate(minimum_date)
      
    ##Direciona para a tela de excluir_Reserva          
    def ir_tela_Excluir_Reserva(self):
        client_socket.send('19'.encode())
        tela = str(self.tela_para_exibir)
        lista_dados = [self.cpf_do_usuario, tela]
        dados = ','.join(lista_dados)
        client_socket.send(dados.encode())
        botoes = client_socket.recv(4096).decode()
        
        if botoes != '0':
            lista_botoes = botoes.split(',')  # Converta a string de botões em uma lista

            # Crie um modelo para armazenar os dados do QListView
            model = QStandardItemModel()

            # Adicione itens ao modelo, dividindo-os pela sala
            current_sala = None
            for botao in lista_botoes:
                if botao.startswith('Sala'):
                    current_sala = QStandardItem(botao)
                    model.appendRow(current_sala)
                else:
                    if current_sala is not None:
                        current_sala.appendRow(QStandardItem(botao))

            # Configure o modelo no QListView
            self.TELA_EXCLUIR_RESERVA_ui.listView.setModel(model)
            self.QtStack.setCurrentIndex(15)  # Altere o índice para a tela do cliente
        else:
            QtWidgets.QMessageBox.information(self, 'Lista de Filmes', 'Sem Dados.')

        
        
    
    def item_selecionado_Excluir_Reserva(self, index):
        # Obtenha o item selecionado
        selected_index = index.row()

        # Verifique se há um item selecionado
        if selected_index >= 0:
            
            item_selecionado = index.data()
            # Exiba um diálogo de confirmação
            resposta = QtWidgets.QMessageBox.question(
                self,
                'Confirmação',
                f'Deseja Remover sua reserva para essa cadeira?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No
            )

            # Verifique a resposta do usuário
            if resposta == QtWidgets.QMessageBox.Yes:
                lista_dados = list()
                client_socket.send('21'.encode())
                str_botao = str(item_selecionado)
                botao_servidor = str_botao[9:]
                client_socket.send(str_botao.encode())
                tela = client_socket.recv(4096).decode()
                int_tela = int(tela)
                botoes_tela_lay = lista_botoes_tela_layout(self, int_tela)
                pintar_botao_verde_excluido(botoes_tela_lay,botao_servidor)
                client_socket.send('20'.encode())
                str_tela = str(tela)
                lista_dados.append(str_botao)
                lista_dados.append(str_tela)
                dados = ','.join(lista_dados)
                client_socket.send(dados.encode())
                desatualizar_frequencia(self, str_tela, botao_servidor)
                print("Tela estatistica")
                valores = list()
                total = total_02 = total_03 = 0.0
                for i, v in self.frequencia_valores.items():
                    total -= i * v["frequencia"]
                for i, v in self.frequencia_valores_02.items():
                    total_02 -= i * v["frequencia"]
                for i, v in self.frequencia_valores_03.items():
                    total_03 -= i * v["frequencia"]
                valores.append(str(total))
                valores.append(str(total_02))
                valores.append(str(total_03))
                enviar = ','.join(valores)
                client_socket.send('22'.encode())
                client_socket.send(enviar.encode())
                self.QtStack.setCurrentIndex(2)
            else:
                QtWidgets.QMessageBox.warning(self, 'Aviso', 'Nenhum item selecionado.')
            
    def Tela_Estatistica(self):
        print("Tela estatistica")
        client_socket.send('17'.encode())
        try:
            retorno = client_socket.recv(4096).decode()

            # Quebra os dados na vírgula para obter uma lista
            lista_todos = retorno.split(',')

            # Faça o que for necessário com a lista
            cont_cliente = lista_todos[0]
            cont_filmes = lista_todos[1]
            cont_filmes_cartaz = lista_todos[2]
            total_lucro = lista_todos[3]
            total_lucro_02 = lista_todos[4]
            total_lucro_03 = lista_todos[5]
            

            # Remova caracteres indesejados
            cont_cliente = cont_cliente.strip(" '[]")
            cont_filmes = cont_filmes.strip(" '[]")
            cont_filmes_cartaz = cont_filmes_cartaz.strip(" '[]")
            total_lucro = total_lucro.strip(" '[]")
            total_lucro_02 = total_lucro_02.strip(" '[]")
            total_lucro_03 = total_lucro_03.strip(" '[]")
        
           
            renda_total = float(total_lucro) + float(total_lucro_02) + float(total_lucro_03)
            
            
            self.TELA_ESTATISTICA_ui.lineEdit.setText(f"{cont_cliente}")
            self.TELA_ESTATISTICA_ui.lineEdit_4.setText(f"{cont_filmes}")
            self.TELA_ESTATISTICA_ui.lineEdit_2.setText(f"{cont_filmes_cartaz}")
            self.TELA_ESTATISTICA_ui.lineEdit_3.setText(f"{float(total_lucro)}")
            self.TELA_ESTATISTICA_ui.lineEdit_5.setText(f"{float(total_lucro_02):.2f}")
            self.TELA_ESTATISTICA_ui.lineEdit_6.setText(f"{float(total_lucro_03):.2f}")
            self.TELA_ESTATISTICA_ui.lineEdit_7.setText(f"{float(renda_total):.2f}")
            

        except Exception as e:
            print(f"\nNão foi possível permanecer conectado! Erro: {e}\n")

        
        self.QtStack.setCurrentIndex(4)
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Ui_Main()
    sys.exit(app.exec_())
