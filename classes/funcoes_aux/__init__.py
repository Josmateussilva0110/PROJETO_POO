import re
import smtplib
from email.message import EmailMessage

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
        (getattr(self.TELA_LAYOUT, f"pushButton_{i}"), self.mudar_cor_red) for i in range(3, 43)
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


def formatar_mensagem(dados_cliente):
    # Formatar a lista de dados_cliente em uma string organizada
    formato_mensagem = "Nome cliente: {}\nNome filme: {}\nAno: {}\nPreço: {}\nClassificação: {}\nHorario: {}\nPagamento: {}"

    # Extrair os valores relevantes da lista
    print('dentro da função formatar:')
    print(f'dados cliente: {dados_cliente}')

    nome_cliente = dados_cliente[0]

    print(f'nome cliente: {nome_cliente}')

    info_filme = dados_cliente[1].split()

    print(f'info filme = {info_filme}')

    nome_filme = info_filme[3]

    print(f'nome filme: {nome_filme}')

    ano = info_filme[5]
    print(f'ano = {ano}')
    preco = info_filme[9]

    print(f'preco: {preco}')

    classificacao = info_filme[7]
    print(f'classificacao: {classificacao}')

    horario = dados_cliente[2]
    print(f'horario: {horario}')
    pagamento = "pix"

    # Criar a mensagem formatada
    mensagem_formatada = formato_mensagem.format(nome_cliente, nome_filme, ano, preco, classificacao, horario, pagamento)

    return mensagem_formatada
