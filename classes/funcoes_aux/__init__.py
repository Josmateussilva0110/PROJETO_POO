import re
import smtplib
from email.message import EmailMessage
from datetime import datetime

def verificar_valor_inteiro(arg):
    try:
        if arg.isnumeric() and int(arg) >=0:
            return True
    except ValueError:
        return False

def verificar_valor_flutuante(arg):
    try:
        float_value = float(arg)
        return float_value >= 0.0
    except ValueError:
        return False



def verificar_nome(arg):
    if arg.replace(' ', '').isalpha():
        return 1
    else:
        return 0
    
def email_valido(email):
    # Padrão de expressão regular para validar um endereço de e-mail
    email_valido = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Verifica se o email corresponde ao padrão
    if re.match(email_valido, email):
        return 1
    else:
        return 0


def verificar_espacos(valor1='', valor2='', valor3='', valor4=''):
    if valor1 == '' or valor2 == '' or valor3 == '' or valor4 == '':
        return True
    else:
        return False


def lista_botoes(self):
    list_botoes = [getattr(self, f"pushButton_{i}") for i in range(3, 43)]
    return list_botoes



def lista_botoes_red(self):
    botao_and_funcao = [
        (getattr(self.TELA_LAYOUT, f"pushButton_{i}"), self.ir_tela_pagamento) for i in range(3, 43)
    ]
    return botao_and_funcao


def lista_botoes_red_02(self):
    botao_and_funcao = [
        (getattr(self.TELA_LAYOUT_02, f"pushButton_{i}"), self.ir_tela_pagamento) for i in range(3, 43)
    ]
    return botao_and_funcao

def lista_botoes_red_03(self):
    botao_and_funcao = [
        (getattr(self.TELA_LAYOUT_03, f"pushButton_{i}"), self.ir_tela_pagamento) for i in range(3, 43)
    ]
    return botao_and_funcao


def lista_botoes_tela_layout(self, tela):
    if tela == 10:
        botao = [
        getattr(self.TELA_LAYOUT, f"pushButton_{i}") for i in range(3, 43)
        ]
    
    elif tela == 13:
        botao = [
        getattr(self.TELA_LAYOUT_02, f"pushButton_{i}") for i in range(3, 43)
        ]
    
    elif tela == 14:
        botao = [
        getattr(self.TELA_LAYOUT_03, f"pushButton_{i}") for i in range(3, 43)
        ]
    return botao


def lista_de_classificacao_filme():
    lista = ['livre', '10', '12', '14', '16', '18']
    return lista


def extrair_informacoes_filme(filme_str):
    if not filme_str:
        return None
    else:
        info = {}
        # Divide a string em linhas
        linhas = filme_str.split('\n')
        for linha in linhas:
            # Verifica se a linha contém o separador ':'
            if ':' in linha:
                chave, valor = linha.split(': ', 1)
                info[chave] = valor
        return info


def tratar_retorno_filmes(filmes): 
    lista_filmes_str = filmes.split('\n\n')
    lista_filmes = [extrair_informacoes_filme(filme_str) for filme_str in lista_filmes_str]
    if lista_filmes:

        lista_filmes_formatada = [
            f"ID: {filme['ID']}\nNome: {filme['Nome']}\nAno: {filme['Ano']}\nPreço: {filme['Preço']}\nClassificação: {filme['Classificação']}\nHorário: {filme['Horário']}\nEm Cartaz: {filme['Em Cartaz']}"
            for filme in lista_filmes
        ]
        #print(f"Tratar retorno: {lista_filmes_formatada}")
        return lista_filmes_formatada
    else:
        return None

        
    
def EnviaEmail(destinatario,mensagem):
    # Configurar email e senha
    EMAIL_ADDRESS = 'cineplus.gerencia@gmail.com'
    EMAIL_PASSWORD = 'qyskmjhoyapdvjay'

    # Criar um email...
    msg = EmailMessage()
    msg['Subject'] = 'COMPROVANTE DE COMPRA'
    msg['From'] = 'cineplus.gerencia@gmail.com'
    msg['To'] = destinatario
    msg.set_content(mensagem)

    # Ecnviar email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)    


def formatar_mensagem(dados_cliente, total_compra, sala, flag=1, parcelas=1):
    # Formatar a lista de dados_cliente em uma string organizada
    formato_mensagem = "Nome cliente: {}\nNome filme: {}\nAno: {}\nClassificação: {}\nHorario: {}\nSala: {}\nTotal compra: {}\nPagamento: {}\nEmitido: {}"
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    if sala == 10:
        sala_exibir = '01'
    elif sala == 13:
        sala_exibir = '02'
    elif sala == 14:
        sala_exibir = '03'
    # Extrair os valores relevantes da lista
    nome_cliente = dados_cliente[0]
    nome_filme = dados_cliente[1]
    ano = dados_cliente[2]
    classificacao = dados_cliente[4]
    horario = dados_cliente[5]
    total = f'{total_compra:.2f}'
    total_compra_exibir = float(total)
    if flag == 1:
        pagamento = 'Pix'
    elif flag == 2:
        pagamento = 'Cartão de Debito'
    elif flag == 3:
        pagamento = f'Cartão de Credito\nDividido em {parcelas} X'
        total_compra_exibir /= int(parcelas)
    emissao = data_e_hora_em_texto
    # Criar a mensagem formatada
    mensagem_formatada = formato_mensagem.format(nome_cliente, nome_filme, ano, classificacao, horario, sala_exibir, total_compra_exibir, pagamento, emissao)

    return mensagem_formatada

            
def mudar_cor_botao_vermelho_valido(lista_botoes_todos, lista_botoes_selecionados):
    print('entrou em função mudar cor valido:')
    print(f'lista de todos: {lista_botoes_todos}')
    print(f'lista botoes selecionado: {lista_botoes_selecionados}')
    
    # Extrai números dos identificadores dos botões selecionados
    numeros_selecionados = [int(botao.split('_')[-1]) for botao in lista_botoes_selecionados.split(',')]

    for button in lista_botoes_todos:
        botao_id = button.objectName()
        print('id do botão', botao_id)
        
        # Extrai o número do identificador do botão na lista completa
        numero_botao = int(botao_id.split('_')[-1])
        
        if numero_botao in numeros_selecionados:
            print(f'Um elemento do button name: {botao_id} está igual a algum dos selecionados')
            button.setStyleSheet("background-color: red;")
            print('pintou')
        else:
            button.setStyleSheet("background-color: green;")



def processar_dados_do_botao(client_socket, tela_para_exibir, botao_id, botoes):
    print('entrou na função processar dados')
    client_socket.send('13'.encode())  # sinal para pegar a lista de botões que estão no servidor
    print('enviou o sinal 13')
    tela = str(tela_para_exibir)
    client_socket.send(tela.encode())
    try:
        mensagem = client_socket.recv(4096).decode()
    except:
        print("\nNão foi possível permanecer conectado!\n")
        client_socket.close()

    if mensagem == '1':  # encontrei os botões
        botoa_achado = client_socket.recv(4096).decode()##Botões achados no servidor com 0
        client_socket.send('14'.encode())
        print('enviou o sinal 14')
        enviar_dados = [botao_id, str(tela_para_exibir)]
        enviar_servidor = ','.join(enviar_dados)
        print(f'enviando para o servidor: {enviar_servidor}')
        client_socket.send(enviar_servidor.encode())

        resposta = client_socket.recv(4096).decode()
        if resposta == '0':
            print(f'Erro ao atualizar "validar" para 1 para o botão {botao_id}.')
        else:
            print(f'Valor de "validar" atualizado para 1 para o botão {botao_id}.')
        
        client_socket.send('15'.encode()) #sinal para pegar a lista de botoes que estão no servidor
        client_socket.send(tela.encode())
        try:
            mensagem = client_socket.recv(4096).decode()
        except:
            print("\nNão foi possível permanecer conectado!\n")
            client_socket.close()
        if mensagem == '1':  # encontrei os botões
            print('entrou aqui ?')
            botoa_achado_verificado = client_socket.recv(4096).decode()
            print(f'botoes achados verific: {botoa_achado_verificado}')
            mudar_cor_botao_vermelho_valido(botoes, botoa_achado_verificado)
            
def pintar_botao_verde_excluido(lista_botoes_todos, lista_botoes_excluidos):
    # Extrai números dos identificadores dos botões excluídos
    numeros_excluidos = [int(botao.split('_')[-1]) for botao in lista_botoes_excluidos.split(',')]

    for button in lista_botoes_todos:
        botao_id = button.objectName()
        print('id do botão', botao_id)
        
        # Extrai o número do identificador do botão na lista completa
        numero_botao = int(botao_id.split('_')[-1])
        
        if numero_botao in numeros_excluidos:
            print(f'O botão {botao_id} foi excluído do banco de dados.')
            button.setStyleSheet("background-color: green;")


def enxugar_string(partes):
    nome_filme_inicio = partes.index('Nome:') + 1
    proximo_marcador_index = partes.index('Ano:') if 'Ano:' in partes else len(partes)
    nome_filme = ' '.join(partes[nome_filme_inicio:proximo_marcador_index])
    partes[3] = nome_filme
    if len(partes) > 4:
        partes.pop(4)
    return partes
