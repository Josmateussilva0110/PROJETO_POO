import threading
import socket
from classes.class_armazenar import *
from classes.class_conexao_bd import *
from classes.class_pessoa import *
from classes.classe_armazena_filme import *
from classes.class_filme import *
from classes.funcoes_aux import *
from classes.class_armazenar_botoes import *
from classes.class_armazenar_botao_02 import *
from classes.class_armazenar_botao_03 import *
from classes.class_armazenar_lucros import *
from classes.class_amazenar_lucro_02 import *
from classes.class_armazenar_lucro_03 import *


host = ''
porta = 8007
addr = (host, porta)

mydb = configure_mysql_connection()
db = create_database()

dados_usuarios = Armazenar(mydb)
dados_filme = Armazenar_filmes(mydb)
dados_botoes = Armazenar_botoes(mydb)
dados_botoes_02 = Armazenar_botoes_02(mydb)
dados_botoes_03 = Armazenar_botoes_03(mydb)
lucros = Armazenar_lucros(mydb)
lucros_02 = Armazenar_lucros_02(mydb)
lucros_03 = Armazenar_lucros_03(mydb)


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

        # sinal para armazenar clientes
        elif mensagem == '1':
            print(f"Mensagem 1 Servidor: {mensagem}")
            dados = con.recv(4096).decode()
            lista = dados.split(',')
            pessoa = Pessoa(lista[1], lista[0], lista[2], lista[3])
            if dados_usuarios.armazenar(pessoa):
                con.send('1'.encode())
            else:
                con.send('0'.encode())

        # sinal para verificar o login
        elif mensagem == '2':
            print(f"Login")
            dados = con.recv(4096).decode()
            lista = dados.split(',')
            if dados_usuarios.verificar_login_Cliente(lista[0], lista[1]):
                nome = dados_usuarios.buscar_cliente_cpf(lista[0])
                con.send('1'.encode())
                con.send(nome.encode())
            elif dados_usuarios.verificar_login_Ger(lista[0], lista[1]):
                con.send('3'.encode())
            else:
                con.send('0'.encode())

        # sinal para armazenar filmes
        elif mensagem == '3':
            data = con.recv(4096).decode()
            partes = data.split(",")
            print(f'partes: {partes}')
            index_livre = 4
            nova_string = ",".join(partes[index_livre:])
            print(f'nova string: {nova_string}')

            filme = Filme(partes[0], partes[1], partes[2],
                          partes[3] ,nova_string)
            aux = dados_filme.armazenar_filmes(filme)
            if aux:
                con.send('1'.encode())
            else:
                con.send('0'.encode())

        # exibe todos os filmes
        elif mensagem == '4':
            result = dados_filme.obter_todos_filmes()
            if result:
                elementos = [filme for filme in result]
                filmes_str = '\n\n'.join(elementos)
                con.send(filmes_str.encode())
            else:
                con.send('0'.encode())

        # verifica se o filme esta em cartaz
        elif mensagem == '5':
            dados_filme_id = con.recv(4096).decode()
            if dados_filme.verificar_filme_em_cartaz(dados_filme_id):
                con.send('1'.encode())
            else:
                con.send('0'.encode())

        # marca o filme como em cartaz
        elif mensagem == '6':
            dados_filme_id = con.recv(4096).decode()
            partes = dados_filme_id.split()
            id = int(partes[0])
            if dados_filme.marcar_filme_em_cartaz(partes[1], id):
                con.send('1'.encode())
            else:
                con.send('0'.encode())

        # exibe todos os filmes em cartaz
        elif mensagem == '7':
            result = dados_filme.obter_todos_filmes_em_cartaz()
            if result:
                elementos = [filme for filme in result]
                filmes_str = '\n\n'.join(elementos)
                con.send(filmes_str.encode())
            else:
                con.send('0'.encode())

        # busca todos os filmes por id
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

        # busca filmes em cartaz por id
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
            print(f'o que o servidor recebeu: {dados_filme_id}')
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
                con.send(retorno.encode())

        elif mensagem == '12':
            botao = con.recv(4096).decode()
            print(f'Recebido do cliente: {botao}')
            
            # Buscar o botão no banco de dados
            validar = dados_botoes.buscar_botao(botao)
            print('Saída do buscar:', validar)
            
            print('Saída do buscar--->', validar["validar"] if validar else None)

            if validar is None:
                con.send('1'.encode())
                # Armazenar o botão no banco de dados

                if dados_botoes.armazenar_botao(botao):
                    print(f'Botão {botao} armazenado com sucesso no servidor.')
                else:
                    print(f'Erro ao armazenar o botão {botao} no servidor.')
            elif validar["validar"] == 0:
                print('Entrou aqui rapá')
                con.send('0'.encode())
                print(f'Botão {botao} já armazenado no servidor, mas é inválido (validar == 0).')
                # Adicione aqui a lógica específica para tratar o caso de validar == 0
            elif validar["validar"] == 1:
                con.send('2'.encode())
                print(f'Botão {botao} já armazenado no servidor e é válido (validar == 1).')
            else:
                print('Ta errado')
        
        #sinal para retornar para o cliente a lista de todos os botoes que foram clicados
        elif mensagem == '13':
            tela = con.recv(4096).decode()
            print(f'tela que recebi do cliente sinal 13: {tela}')
            if tela == '10':
                lista_botoes = dados_botoes.obter_todos_botoes()
                print('lista com todos os botões1',lista_botoes)
                if lista_botoes != None:
                    con.send('1'.encode())
                    lista_botoes_str = ','.join(lista_botoes)
                    con.send(lista_botoes_str.encode())
                else:
                    con.send('0'.encode())
            elif tela == '13':
                lista_botoes = dados_botoes_02.obter_todos_botoes_02()
                print('lista com todos os botões1',lista_botoes)
                if lista_botoes != None:
                    con.send('1'.encode())
                    lista_botoes_str = ','.join(lista_botoes)
                    con.send(lista_botoes_str.encode())
                else:
                    con.send('0'.encode())
            
            elif tela == '14':
                lista_botoes = dados_botoes_03.obter_todos_botoes_03()
                print('lista com todos os botões1',lista_botoes)
                if lista_botoes != None:
                    con.send('1'.encode())
                    lista_botoes_str = ','.join(lista_botoes)
                    con.send(lista_botoes_str.encode())
                else:
                    con.send('0'.encode())
                
        elif mensagem == '14':
            lista_botoes = con.recv(4096).decode().split(',')  # Supondo que os botões estejam separados por vírgula
            print(f'recebido do cliente sinal 14: {lista_botoes}')
            botao = lista_botoes[0]
            # Verificar se há pelo menos um botão na lista
            if botao:
                ultimo_botao = botao
                if lista_botoes[1] == '10':
                    # Atualizar o valor de 'validar' para 1 apenas para o último botão no banco de dados
                    if dados_botoes.atualizar_valido(ultimo_botao):
                        if dados_botoes.atualizar_cpf(cpf):
                            print(f'Valor de "validar" atualizado para 1 para o último botão {ultimo_botao}.')
                            # Enviar confirmação ao cliente
                            con.send('1'.encode())
                    else:
                        print(f'Erro ao atualizar "validar" para 1 para o último botão {ultimo_botao}.')
                        # Enviar informação de erro ao cliente
                        con.send('0'.encode())
                elif lista_botoes[1] == '13':
                    # Atualizar o valor de 'validar' para 1 apenas para o último botão no banco de dados
                    if dados_botoes_02.atualizar_valido_02(ultimo_botao):
                        if dados_botoes_02.atualizar_cpf_02(cpf):
                            print(f'Valor de "validar" atualizado para 1 para o último botão {ultimo_botao}.')
                            # Enviar confirmação ao cliente
                            con.send('1'.encode())
                    else:
                        print(f'Erro ao atualizar "validar" para 1 para o último botão {ultimo_botao}.')
                        # Enviar informação de erro ao cliente
                        con.send('0'.encode())
                    
                elif lista_botoes[1] == '14':
                    # Atualizar o valor de 'validar' para 1 apenas para o último botão no banco de dados
                    if dados_botoes_03.atualizar_valido_03(ultimo_botao):
                        if dados_botoes_03.atualizar_cpf_03(cpf):
                            print(f'Valor de "validar" atualizado para 1 para o último botão {ultimo_botao}.')
                            # Enviar confirmação ao cliente
                            con.send('1'.encode())
                    else:
                        print(f'Erro ao atualizar "validar" para 1 para o último botão {ultimo_botao}.')
                        # Enviar informação de erro ao cliente
                        con.send('0'.encode())
                
                elif lista_botoes[1] == '14':
                    # Atualizar o valor de 'validar' para 1 apenas para o último botão no banco de dados
                    if dados_botoes_03.atualizar_valido_03(ultimo_botao):
                        print(f'Valor de "validar" atualizado para 1 para o último botão {ultimo_botao}.')
                        # Enviar confirmação ao cliente
                        con.send('1'.encode())
                    else:
                        print(f'Erro ao atualizar "validar" para 1 para o último botão {ultimo_botao}.')
                        # Enviar informação de erro ao cliente
                        con.send('0'.encode())
            else:
                print('Lista de botões vazia. Nenhum botão atualizado.')
                # Enviar informação de erro ao cliente
                con.send('0'.encode())
            
            
        elif mensagem == '15':
            print('entrou no 15')
            tela = con.recv(4096).decode()
            print(f'tela que recebi do cliente sinal 15: {tela}')
            if tela == '10':
                print('entrou no if 10')
                lista_botoes_validos = dados_botoes.obter_botoes_validos()
                print('lista com todos os botões',lista_botoes_validos)
                if lista_botoes_validos != None:
                    con.send('1'.encode())
                    lista_botoes_str = ','.join(lista_botoes_validos)
                    con.send(lista_botoes_str.encode())
                else:
                    con.send('0'.encode())
            elif tela == '13':
                print('entrou no if 13')
                lista_botoes_validos = dados_botoes_02.obter_botoes_validos_02()
                print('lista com todos os botões',lista_botoes_validos)
                if lista_botoes_validos != None:
                    con.send('1'.encode())
                    lista_botoes_str = ','.join(lista_botoes_validos)
                    con.send(lista_botoes_str.encode())
                else:
                    con.send('0'.encode())
            
            elif tela == '14':
                print('entrou no if 14')

                lista_botoes_validos = dados_botoes_03.obter_botoes_validos_03()
                print('lista com todos os botões',lista_botoes_validos)
                if lista_botoes_validos != None:
                    con.send('1'.encode())
                    lista_botoes_str = ','.join(lista_botoes_validos)
                    con.send(lista_botoes_str.encode())
                else:
                    con.send('0'.encode())
        
        elif mensagem == '16':
            botao = con.recv(4096).decode()
            print(f'Recebido do cliente: {botao}')
            
            # Buscar o botão no banco de dados
            validar = dados_botoes_02.buscar_botao_02(botao)
            
            print('Saída do buscar--->', validar["validar"] if validar else None)

            if validar is None:
                con.send('1'.encode())
                # Armazenar o botão no banco de dados

                if dados_botoes_02.armazenar_botao_02(botao):
                    print(f'Botão {botao} armazenado com sucesso no servidor.')
                else:
                    print(f'Erro ao armazenar o botão {botao} no servidor.')
            elif validar["validar"] == 0:
                print('Entrou aqui rapá')
                con.send('0'.encode())
                print(f'Botão {botao} já armazenado no servidor, mas é inválido (validar == 0).')
                # Adicione aqui a lógica específica para tratar o caso de validar == 0
            elif validar["validar"] == 1:
                con.send('2'.encode())
                print(f'Botão {botao} já armazenado no servidor e é válido (validar == 1).')
            else:
                print('Ta errado')
                
        elif mensagem == '17':
            lista_todos = []
            cont_cliente = dados_usuarios.contar_pessoas_cadastradas()
            cont_filmes = dados_filme.contar_filmes_cadastrados()
            cont_filmes_cartaz = dados_filme.contar_filmes_em_cartaz()  # Adicionado para contar filmes em cartaz
            cont_cliente = str(cont_cliente)
            cont_filmes = str(cont_filmes)
            cont_filmes_cartaz = str(cont_filmes_cartaz)  # Convertido para string
            lista_todos.append(cont_cliente)
            lista_todos.append(cont_filmes)
            lista_todos.append(cont_filmes_cartaz)  # Adicionado o contador de filmes em cartaz
            print(lista_todos)
            con.send(','.join(lista_todos).encode())  # Enviando a lista como uma string separada por vírgulas
        

        elif mensagem == '18':
            botao = con.recv(4096).decode()
            print(f'Recebido do cliente: {botao}')
            
            # Buscar o botão no banco de dados
            validar = dados_botoes_03.buscar_botao_03(botao)
            print('Saída do buscar:', validar)
            
            print('Saída do buscar--->', validar["validar"] if validar else None)

            if validar is None:
                con.send('1'.encode())
                # Armazenar o botão no banco de dados

                if dados_botoes_03.armazenar_botao_03(botao):
                    print(f'Botão {botao} armazenado com sucesso no servidor.')
                else:
                    print(f'Erro ao armazenar o botão {botao} no servidor.')
            elif validar["validar"] == 0:
                print('Entrou aqui rapá')
                con.send('0'.encode())
                print(f'Botão {botao} já armazenado no servidor, mas é inválido (validar == 0).')
                # Adicione aqui a lógica específica para tratar o caso de validar == 0
            elif validar["validar"] == 1:
                con.send('2'.encode())
                print(f'Botão {botao} já armazenado no servidor e é válido (validar == 1).')
            else:
                print('Ta errado')
        
        elif mensagem == '19':
            print('ta no 19')
            lista_completas_botoes = list()
            dados = con.recv(4096).decode()
            dados_lista = dados.split(',')
            cpf = int(dados_lista[0])
            botoes_associados = dados_botoes.obter_botoes_por_cpf(cpf)
            botoes_associados_02 = dados_botoes_02.obter_botoes_por_cpf_02(cpf)
            botoes_associados_03 = dados_botoes_03.obter_botoes_por_cpf_03(cpf)

            lista_completas_botoes = []

            if botoes_associados is not None:
                lista_completas_botoes.extend(botoes_associados)

            if botoes_associados_02 is not None:
                lista_completas_botoes.extend(botoes_associados_02)
            
            if botoes_associados_03 is not None:
                lista_completas_botoes.extend(botoes_associados_03)

            if not lista_completas_botoes:
                con.send('0'.encode())
            else:
                enviar_lista = ','.join(map(str, lista_completas_botoes))
                print(f'Botoes associados: {enviar_lista}')
                con.send(enviar_lista.encode())
                # Faça aqui o que desejar com a lista de botões associados
                
        elif mensagem == '20':
            print(f'sinal 20')
            dados = con.recv(4096).decode()
            print(f'DADOS RECEBIDOS: {dados}')
            dados_partes = dados.split(',')
            print(f'dados_partes[0]: {dados_partes[0]}')
            print(f'dados_partes[1]: {dados_partes[1]}')
            # Verificar se há pelo menos um botão na lista
            if dados_partes[0]:
                botao = dados_partes[0]
                if dados_partes[1] == '10':
                    if dados_botoes.Exclui_Reserva(botao):
                        print(f'EXCLUIDO TELA 10')
                elif dados_partes[1] == '13':
                    if dados_botoes_02.Exclui_Reserva_02(botao):
                        print(f'EXCLUIDO TELA 13')
                elif dados_partes[1] == '14':
                    if dados_botoes_03.Exclui_Reserva_03(botao):
                        print('EXCLUIDO TELA 14')
        
        elif mensagem == '21':
            botao = con.recv(4096).decode()
            str_botao = str(botao)
            print(f'BOTAO RECEBIDO DO CLIENTE: {str_botao}')
            aux = dados_botoes.buscar_botao(str_botao)
            aux_01 = dados_botoes_02.buscar_botao_02(str_botao)
            aux_02 = dados_botoes_03.buscar_botao_03(str_botao)
            
            if aux != None:
                print('achei o botao tela 10!!!')
                con.send('10'.encode())
            elif aux_01 != None:
                print('achei o botao tela 13!!!')
                con.send('13'.encode())
            elif aux_02 != None:
                print('achei botao tela 14!!!')
                con.send('14'.encode())
            
        elif mensagem == '22':
            lista = list()
            receber = con.recv(4096).decode()
            valores_partes = receber.split(',')
            valor = valores_partes[0]
            valor_02 = valores_partes[1]
            valor_03 = valores_partes[2]
            lucros.armazenar_lucro(valor)
            lucros_02.armazenar_lucro_02(valor_02)
            lucros_03.armazenar_lucro_03(valor_03)
            total_lucro = lucros.obter_lucro_total()
            total_lucro_02 = lucros_02.obter_lucro_total_02()
            total_lucro_03 = lucros_03.obter_lucro_total_03()
            lista.append(str(total_lucro))
            lista.append(str(total_lucro_02))
            lista.append(str(total_lucro_03))
            enviar_cliente = ','.join(lista)
            con.send(enviar_cliente.encode())
            
            

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
    try:
        main()
    finally:
        dados_botoes.drop_tabela_botoes()
