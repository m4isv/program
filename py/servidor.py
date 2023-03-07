import socket
print("\t\033[45mservidor online\033[m")
servidor = socket.socket()

ip = "127.0.0.1"
porta = 666

try:
	servidor.bind((ip,porta))
	servidor.listen(5)
	print(f"escutando em {ip} {porta} ")
	
	(client_socket, endereco)=servidor.accepet()
	print(f"recebido de {endereco}")
	
	while True:
		dados = client_socket.recv(1024)
		print(dados)
		#cliente_socket.send()
	servidor.close()
		
except Exception as error:
	print(f"error ")