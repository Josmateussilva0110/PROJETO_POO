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
        print(f"Mensagem sinal do Cliente: {mensagem}") 
        if mensagem == '0':
            print(f"Mensagem 0 Servidor: {mensagem}") 
            conectado = False

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


        elif mensagem == '2':
            print(f"Login Gerente") 
            dados = con.recv(4096).decode()
            lista = dados.split(',')
            #print(f"lista Servidor: {lista}") 
            if dados_usuarios.verificar_login_Cliente(lista[0], lista[1]):
                con.send('1'.encode())
            elif dados_usuarios.verificar_login_Ger(lista[0], lista[1]):
                con.send('3'.encode())
            else:
                con.send('0'.encode())


        elif mensagem == '3':
            #print(f"Mensagem 3 Servidor: {mensagem}") 
            data = con.recv(4096).decode()
            partes = data.split(",")
            #print(f"Partes Servidor: {partes}") 
            index_livre = 4
            nova_string = ",".join(partes[index_livre:])
            filme = Filme(partes[0], partes[1], partes[2], partes[3], nova_string)
            aux = dados_filme.armazenar_filmes(filme)
            if aux:
                con.send('1'.encode())
            else:
                con.send('0'.encode())
        
        elif mensagem == '4':
            print("EXIBIR TODOS OS FILMES EM CARTAZ OU NÃO")
            result = dados_filme.obter_todos_filmes()
            #print(f"Result Servidor: {result}") 
            if result:
                elementos = [filme for filme in result]
                print(f"Elementos Servidor: {elementos}") 
                filmes_str = '\n\n'.join(elementos)
                print(f"filmes_str Servidor: {filmes_str}") 
                con.send(filmes_str.encode())
            else:
                con.send('0'.encode())

        elif mensagem == '5':
            print("VERIFICAR FILME EM CARTAZ clique")
            dados_filme_id = con.recv(4096).decode()
            if dados_filme.verificar_filme_em_cartaz(dados_filme_id):
                con.send('1'.encode())
            else:
                con.send('0'.encode())
        
        elif mensagem == '6':
            print('Função que marca em Cartaz')
            dados_filme_id = con.recv(4096).decode()
            print(f"Dados_filme_id: {dados_filme_id}")
            partes = dados_filme_id.split()
            print(partes[0])
            print(partes[1])
            id = int(partes[0])
            if dados_filme.marcar_filme_em_cartaz(partes[1], id):
                con.send('1'.encode())
            else:
                con.send('0'.encode())
        
        elif mensagem == '7':
            print("Função que EXCLUI do cartaz")
            result = dados_filme.obter_todos_filmes()
            print(f"Result Servidor: {result}")
            if result:
                print('Entrou result')
                elementos = [filme for filme in result]
                filmes_str = '\n\n'.join(elementos)
                print(f"Filmess_str Servidor: {filmes_str}") 
                con.send(filmes_str.encode())
            else:
                print("Nao entrou no result")
                con.send('0'.encode())
                
        elif mensagem == '8':
            print("Função que Busca um filme")
            dados_filme_id = con.recv(1024).decode()
            print(f"Dados_filme_id: {dados_filme_id}")
            partes = int(dados_filme_id)
            print(f"Partes: {type(partes)}")
            if dados_filme.buscar_filme_por_id(partes):
                filme = dados_filme.buscar_filme_por_id(partes)
                print("entrou aqui Correto")
                print(f"achei o filme em: {filme}")
                con.send('1'.encode())
                con.send(filme.encode())
            else:
                print("entrou aqui Erro")
                con.send('0'.encode())
        
        elif mensagem == '9': #EXIBIR TODOS OS FILMES EM CARTAZ
            result = dados_filme.obter_todos_filmes_em_cartaz()
            if result:
                elementos = [filme for filme in result]
                filmes_str = '\n\n'.join(elementos)
                con.send(filmes_str.encode())
            else:
                con.send('0'.encode())
    
        # buscar horarios do filme
        elif mensagem == '10':
            dados_filme_id = con.recv(4096).decode()
            result = dados_filme.buscar_horarios_id(dados_filme_id)
            if result:
                horarios = [horario for horario in result]
                horarios_str = ','.join(horarios)
                print(f'retorno servidor: {horarios_str}')
                con.send(horarios_str.encode())
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
