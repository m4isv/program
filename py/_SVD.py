import socket

print("\t\033[45mServidor online\033[m")

s = socket.socket()

s.bind((socket.gethostname(),12374))
s.listen(5)

while True:
        clientesocket, addres = s.accept()
        print(f"conecção de {addres} foi bem estabelecida ")
        clientesocket.send(bytes("bem vindo ao server!", "utf-8"))
        
        comando = input("sair para feixa: ")
        if(comando.lower() == "sair"):
        	s.close()
        	break

