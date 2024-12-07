import socket

class Server:

    def __init__(self):
        self.server = None

    # configuracao do servidor
    def config(self, host, port):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(10)

        return "Aguardando conexões..."
    

    # aceitar conexoes
    def accept(self):

        return self.server.accept()


class Client:

    def __init__(self):
        self.client = None

    #configuracao do cliente
    def config(self, server_ip, server_port):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((server_ip, server_port))

        return "conectado!"
    
    def send(self, message):
        
        self.client.sendall(message.encode())