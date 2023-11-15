import threading
import socket
from classes.class_armazenar import *
from classes.class_conexao_bd import *
from classes.class_pessoa import *
from classes.classe_armazena_filme import *
from classes.class_filme import *

# ip = 192.168.1.6

host = ''
porta = 8007
addr = (host, porta)

mydb = configure_mysql_connection()
db = create_database()

dados_usuarios = Armazenar(mydb)
dados_filme = Armazenar_filmes(mydb)

def menu(con, cliente):
    nome_cliente = con.recv(1024).decode()
    print(f"[CONECTADO] Cliente: {nome_cliente}")

    conectado = True

    while conectado:
        mensagem = con.recv(1024).decode()
        if mensagem == '0':
            conectado = False

        elif mensagem == '1':
            dados = con.recv(4096).decode()
            lista = dados.split(',')
            pessoa = Pessoa(lista[1], lista[0], lista[2], lista[3])
            if dados_usuarios.armazenar(pessoa):
                con.send('1'.encode())
            else:
                con.send('0'.encode())


        elif mensagem == '2':
            dados = con.recv(4096).decode()
            lista = dados.split(',')
            if dados_usuarios.verificar_login_Cliente(lista[0], lista[1]):
                con.send('1'.encode())
            elif dados_usuarios.verificar_login_Ger(lista[0], lista[1]):
                con.send('3'.encode())
            else:
                con.send('0'.encode())


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
        
        elif mensagem == '4':
            result = dados_filme.obter_todos_filmes()
            if result:
                filmes_str = '\n'.join(result)
                con.send(filmes_str.encode())
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
