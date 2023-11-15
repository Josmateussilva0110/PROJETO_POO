import socket

mes = 'bye'

ip = '192.168.1.6'
port = 8007
nome = 'Jose Mateus'
addr = ((ip,port))
cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(addr)
cliente_socket.send(nome.encode())

while(True):
    try:
        mensagem = int(input("Digite a mensagem: "))
        cliente_socket.send(mensagem.encode())
        print('Mensagem enviada')
        if mensagem == 0:
            print('desconectado')
            cliente_socket.close()
            break
    except:
        cliente_socket.close()
