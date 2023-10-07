# Criando CHAT de Mensagens 
import os

mensagens = []

nome = input("Nome: ")

while True:
    # limpando terminal
    os.system('cls')
    
    if len(mensagens) > 0:
        for m in mensagens:
            print (m['nome'], "-", m['texto'])
            
    print("_____________________")

    # obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    # adicionando mensage na lista
    mensagens.append ({
        "nome": nome,
        "texto": texto
})

