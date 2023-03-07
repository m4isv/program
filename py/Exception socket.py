import socket
try:
	site = input("site: ")
	print(socket.gethostbyname(site))
except socket.gaierror:
	print("ocorreu um error")
	
	