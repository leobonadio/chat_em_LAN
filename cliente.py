import socket
import biblioteca_de_rede.py as lan

#configuracao
SERVER_IP = "127.0.0.1"
PORT = 22222

print(lan.Client.config(SERVER_IP, PORT))

nome = input("Qual o seu nome? ")

lan.Client.send(nome)

while True:

    mensagem = ""
    mensagem = input()
    
    if mensagem:  #quando utilizamos "if {string}:" vereficamos se a string tem conteudo e retorna True se tiver.
        lan.Client.send(mensagem)