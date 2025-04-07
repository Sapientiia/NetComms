import socket
import threading

# Configuração 
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# receber mensagens do servidor
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024)
            print(message.decode())
        except:
            print("Erro ao receber mensagem.")
            break

#  enviar mensagens ao servidor
def send_message(client):
    while True:
        message = input()
        client.send(message.encode())

# Criar a conexão com o servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))

# Iniciar as threads para enviar e receber mensagens
threading.Thread(target=receive_messages, args=(client,)).start()
threading.Thread(target=send_message, args=(client,)).start()
