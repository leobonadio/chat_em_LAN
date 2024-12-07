import threading
import objetos as _

#configuracao
HOST = "0.0.0.0"
PORT = 22222

def main(conn):

    nome_cliente = conn.recv(1024).decode()

    print(f"conexão estabelecida com {nome_cliente}.")

    while True:
        
        mensagem_cliente = conn.recv(1024).decode()
        print(f"{nome_cliente}: {mensagem_cliente}")


print(_.server.config(HOST, PORT))

while True:

    conn, addr = _.server.accept()

    threading.Thread(target = main, args = (conn,)).start()
