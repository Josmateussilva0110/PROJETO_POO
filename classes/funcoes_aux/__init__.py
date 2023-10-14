import re

def ler_int(arg):
    if arg >= 0:
        return 1
    elif(arg == ValueError or arg == TypeError):
        return 0
    elif arg == KeyboardInterrupt:
        return 0

def verificar_nome(arg):
    if arg.replace(' ', '').isalpha():
        return 1
    elif arg == KeyboardInterrupt:
        return 0
    
def email_valido(email):
    # Padrão de expressão regular para validar um endereço de e-mail
    email_valido = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Verifica se o email corresponde ao padrão
    if re.match(email_valido, email):
        return 1
    else:
        return 0