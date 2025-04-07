# NetComms
Um simples chat em tempo real baseado em sockets, desenvolvido com Python.

## 🚀 Funcionalidades

- Comunicação em tempo real via rede local (`localhost`).
- Suporte a múltiplos usuários conectados simultaneamente.
- Notificação quando um usuário entra ou sai do chat.
- Interface via terminal (leve e rápida).

## 📦 Requisitos

- Python 3.x

Nenhuma biblioteca externa é necessária.

## 🛠️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/Sapientiia/NetComms.git
cd NetComms
```
### 2. Inicie o servidor

```bash
python server.py
```
### 3. Inicie o cliente (em outro terminal ou máquina)

```bash
python client.py
```
🖼️ Exemplo de uso

![image](https://github.com/user-attachments/assets/2dd7463f-519b-45f7-9c0c-e66143b3b816)


🧠 Estrutura
server.py: gerencia conexões, mensagens e difusão para todos os clientes.

client.py: conecta ao servidor e permite enviar/receber mensagens.

🧪 Melhorias futuras
Interface gráfica (GUI) com Tkinter ou PyQt.

Suporte a mensagens privadas.

Histórico de mensagens.

Deploy em rede externa ou pela internet.

💡 Dica: Para acessar de fora do localhost (ex: outro dispositivo ou internet), você pode usar ferramentas como:

ngrok → ngrok tcp 12345;

LocalTunnel ou alternativas.

