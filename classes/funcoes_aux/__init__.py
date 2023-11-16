import re

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

    lista_filmes_formatada = [
        f"ID: {filme['ID']}\nNome: {filme['Nome']}\nAno: {filme['Ano']}\nPreço: {filme['Preço']}\nClassificação: {filme['Classificação']}\nHorário: {filme['Horário']}\nEm Cartaz: {filme['Em Cartaz']}"
        for filme in lista_filmes
    ]
    #print(f"Tratar retorno: {lista_filmes_formatada}")
    return lista_filmes_formatada
