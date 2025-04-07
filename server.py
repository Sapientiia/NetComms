import socket
import threading
import requests

# Configuração do servidor
SERVER_HOST = '127.0.0.1'  # Escuta todas as interfaces de rede
SERVER_PORT = 12345      # Porta em que o servidor está escutando

clients = []  # Lista para armazenar os clientes conectados

# Função para enviar mensagens a todos os clientes conectados
def broadcast(message, client):
    for c in clients:
        if c != client:
            try:
                c.send(message)
            except:
                clients.remove(c)

# Função para tratar mensagens de cada cliente
def handle_client(client, client_name):
    while True:
        try:
            message = client.recv(1024)
            if message:
                formatted_message = f"{client_name}: {message.decode()}"
                broadcast(formatted_message.encode(), client)
        except:
            clients.remove(client)
            print(f"[-] {client_name} saiu do chat.")
            broadcast(f"{client_name} saiu do chat.".encode(), client)
            break

# Função para aceitar novas conexões de clientes
def receive_connections():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen(5)
    print(f"Servidor está escutando na porta {SERVER_PORT}...")

    while True:
        client, address = server.accept()
        client_ip, client_port = address

        # Solicitar o nome do cliente
        client.send("Digite seu nome:".encode())
        client_name = client.recv(1024).decode().strip()

        print(f"[+] {client_name} entrou no chat!")

        clients.append(client)
        client.send(f"Bem-vindo ao chat, {client_name}!".encode())
        
        threading.Thread(target=handle_client, args=(client, client_name)).start()

# Iniciar o servidor
receive_connections()
