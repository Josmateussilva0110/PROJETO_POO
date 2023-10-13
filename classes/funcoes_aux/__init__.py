
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
    