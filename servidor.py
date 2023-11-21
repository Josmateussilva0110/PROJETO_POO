import threading
import socket
from classes.class_armazenar import *
from classes.class_conexao_bd import *
from classes.class_pessoa import *
from classes.classe_armazena_filme import *
from classes.class_filme import *
from classes.funcoes_aux import *
from classes.class_armazenar_botoes import *

# ip = 192.168.1.6

host = ''
porta = 8007
addr = (host, porta)

mydb = configure_mysql_connection()
db = create_database()

dados_usuarios = Armazenar(mydb)
dados_filme = Armazenar_filmes(mydb)
dados_botoes = Armazenar_botoes(mydb)

def menu(con, cliente):
    nome_cliente = con.recv(1024).decode()
    print(f"[CONECTADO] Cliente: {nome_cliente}")
    

    conectado = True

    while conectado:
        mensagem = con.recv(1024).decode()
        print(f"Mensagem sinal do Cliente: {mensagem}") 
        if mensagem == '0':
            print(f"Mensagem 0 Servidor: {mensagem}") 
            conectado = False

        #sinal para armazenar clientes 
        elif mensagem == '1':
            print(f"Mensagem 1 Servidor: {mensagem}")
            dados = con.recv(4096).decode()
            lista = dados.split(',')
            #print(f"lista Servidor: {lista}") 
            pessoa = Pessoa(lista[1], lista[0], lista[2], lista[3])
            #print(f"Pessoa Servidor: {pessoa}") 
            if dados_usuarios.armazenar(pessoa):
                con.send('1'.encode())
            else:
                con.send('0'.encode())


        #sinal para verificar o login
        elif mensagem == '2':
            print(f"Login") 
            dados = con.recv(4096).decode()
            lista = dados.split(',')
            #print(f"lista Servidor: {lista}") 
            if dados_usuarios.verificar_login_Cliente(lista[0], lista[1]):
                con.send('1'.encode())
            elif dados_usuarios.verificar_login_Ger(lista[0], lista[1]):
                con.send('3'.encode())
            else:
                con.send('0'.encode())

        #sinal para armazenar filmes 
        elif mensagem == '3':
            data = con.recv(4096).decode()
            partes = data.split(",")
            index_livre = 4
            nova_string = ",".join(partes[index_livre:])
            filme = Filme(partes[0], partes[1], partes[2], partes[3], nova_string)
            aux = dados_filme.armazenar_filmes(filme)
            if aux:
                con.send('1'.encode())
            else:
                con.send('0'.encode())
        
        #exibe todos os filmes 
        elif mensagem == '4':
            result = dados_filme.obter_todos_filmes()
            if result:
                elementos = [filme for filme in result]
                filmes_str = '\n\n'.join(elementos)
                con.send(filmes_str.encode())
            else:
                con.send('0'.encode())
        
        #verifica se o filme esta em cartaz
        elif mensagem == '5':
            dados_filme_id = con.recv(4096).decode()
            if dados_filme.verificar_filme_em_cartaz(dados_filme_id):
                con.send('1'.encode())
            else:
                con.send('0'.encode())
        
        #marca o filme como em cartaz
        elif mensagem == '6':
            dados_filme_id = con.recv(4096).decode()
            partes = dados_filme_id.split()
            id = int(partes[0])
            if dados_filme.marcar_filme_em_cartaz(partes[1], id):
                con.send('1'.encode())
            else:
                con.send('0'.encode())
        
        #exibe todos os filmes em cartaz
        elif mensagem == '7':
            result = dados_filme.obter_todos_filmes_em_cartaz()
            if result:
                elementos = [filme for filme in result]
                filmes_str = '\n\n'.join(elementos)
                con.send(filmes_str.encode())
            else:
                con.send('0'.encode())

        #busca todos os filmes por id     
        elif mensagem == '8':
            dados_filme_id = con.recv(1024).decode()
            partes = int(dados_filme_id)
            if dados_filme.buscar_filme_por_id(partes):
                filme = dados_filme.buscar_filme_por_id(partes)
                con.send('1'.encode())
                con.send(filme.encode())
            else:
                print("entrou aqui Erro")
                con.send('0'.encode())
        
        #busca filmes em cartaz por id
        elif mensagem == '9':
            dados_filme_id = con.recv(1024).decode()
            print(f"Dados_filme_id: {dados_filme_id}")
            partes = int(dados_filme_id)
            print(f"Partes: {type(partes)}")
            if dados_filme.buscar_filme_em_cartaz_por_id(partes):
                filme = dados_filme.buscar_filme_em_cartaz_por_id(partes)
                con.send('1'.encode())
                con.send(filme.encode())
            else:
                con.send('0'.encode())
        
    
        # buscar horarios do filme
        elif mensagem == '10':
            dados_filme_id = con.recv(4096).decode()
            result = dados_filme.buscar_horarios_id(dados_filme_id)
            if result:
                horarios = [horario for horario in result]
                horarios_str = ','.join(horarios)
                con.send(horarios_str.encode())
            else:
                con.send('0'.encode())
                
        elif mensagem == '11':
            cpf = con.recv(4096).decode()
            if dados_usuarios.buscar_email_cpf(cpf):
                retorno = dados_usuarios.buscar_email_cpf(cpf)
                print(retorno)
                con.send(retorno.encode())
        
        elif mensagem == '12':
            botao = con.recv(4096).decode()
            print(f'recebido do servidor: {botao}')
            saida = dados_botoes.buscar_botao(botao)
            if saida == None:
                dados_botoes.armazenar_botoes(botao)
                con.send('1'.encode())
            else:
                con.send('0'.encode())
        


    print(f"[DESCONECTADO] Cliente: {nome_cliente}")
    con.close()
    print("[INICIADO] Aguardando conexão...")

def main():
    print("[INICIADO] Aguardando conexão...")
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen()

    while True:
        con, cliente = serv_socket.accept()
        thread = threading.Thread(target=menu, args=(con, cliente))
        thread.start()

if __name__ == "__main__":
    main()
