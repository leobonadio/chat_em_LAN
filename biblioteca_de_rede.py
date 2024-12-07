import socket

class Server:

    # configuracao do servidor
    def config(self, host, port):

        global server

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(10)

        return "Aguardando conexões..."
    

    # aceitar conexoes
    def accept(self):

        return server.accept()


class Client:

    #configuracao do cliente
    def config(self, server_ip, server_port):

        global client

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, server_port))

        return "conectado!"
    
    def send(self, message):
        client.sendall(message.encode())