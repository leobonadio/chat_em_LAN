import objetos as _

#configuracao
SERVER_IP = "127.0.0.1"
PORT = 22222

print(_.client.config(SERVER_IP, PORT))

nome = input("Qual o seu nome? ")

_.client.send(nome)

while True:

    mensagem = ""
    mensagem = input()
    
    if mensagem:  #quando utilizamos "if {string}:" vereficamos se a string tem conteudo e retorna True se tiver.
        _.client.send(mensagem)