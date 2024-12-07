
import socket
import threading
import biblioteca_de_rede as lan

#configuracao
HOST = "0.0.0.0"
PORT = 22222

def main(conn):

    nome_cliente = conn.recv(1024).decode()

    print(f"conexão estabelecida com {nome_cliente}.")

    while True:
        
        mensagem_cliente = conn.recv(1024).decode()
        print(f"{nome_cliente}: {mensagem_cliente}")


print(lan.Server.config(HOST, PORT))

while True:

    conn, addr = lan.Server.accept()

    threading.Thread(target = main, args = (conn,)).start()
