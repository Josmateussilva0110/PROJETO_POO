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

def lista_botoes_tela_layout(self): #retorno todos os botoes que preciso
    botao_and_funcao = [
        getattr(self.TELA_LAYOUT, f"pushButton_{i}") for i in range(3, 43)
    ]
    return botao_and_funcao

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


def formatar_mensagem(dados_cliente, total_compra, flag=1, parcelas=1):
    # Formatar a lista de dados_cliente em uma string organizada
    formato_mensagem = "Nome cliente: {}\nNome filme: {}\nAno: {}\nPreço: {}\nClassificação: {}\nHorario: {}\nPagamento: {}\nTotal compra: {}\nEmitido: {}"
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    # Extrair os valores relevantes da lista
    nome_cliente = dados_cliente[0]
    nome_filme = dados_cliente[1]
    ano = dados_cliente[2]
    preco = dados_cliente[3]
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
    mensagem_formatada = formato_mensagem.format(nome_cliente, nome_filme, ano, preco, classificacao, horario, pagamento, total_compra_exibir, emissao)

    return mensagem_formatada

                
def mudar_cor_botao_vermelho(lista_botoes_todos, lista_botoes_selecionados):
    print('entrou em função mudar cor:')
    print(f'lista de todos os botoes: {lista_botoes_todos}')
    print(f'lista de botoes selecionados: {lista_botoes_selecionados}')

    # Itera sobre todos os botões na lista de todos os botões
    for button in lista_botoes_todos:
        botao_id = button.objectName()
        print('id do botão', botao_id)

        # Verifica se o nome do botão está na lista de botões selecionados
        if botao_id in lista_botoes_selecionados:
            print(f'Um elemetno do button name: {botao_id} esta igual a {lista_botoes_selecionados}')
            button.setStyleSheet("background-color: red;")
            print('pintou')
            
def mudar_cor_botao_vermelho_valido(lista_botoes_todos, lista_botoes_selecionados):
    print('entrou em função mudar cor:')
    print(f'lista de todos os botoes: {lista_botoes_todos}')
    print(f'lista de botoes selecionados: {lista_botoes_selecionados}')

    # Itera sobre todos os botões na lista de todos os botões
    for button in lista_botoes_todos:
        botao_id = button.objectName()
        print('id do botão', botao_id)

        # Verifica se o nome do botão está na lista de botões selecionados
        if botao_id in lista_botoes_selecionados:
            print(f'Um elemetno do button name: {botao_id} esta igual a {lista_botoes_selecionados}')
            button.setStyleSheet("background-color: red;")
            print('pintou')
            


