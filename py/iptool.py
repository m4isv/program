inicio = """\033[1;32m
\033[1;30m╔══╗╔═══╗╔════╗╔═══╗╔═══╗╔╗───╔═══╗\033[m
\033[1;31m╚╣─╝║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║║║───║╔═╗║\033[m
\033[1;32m─║║─║╚═╝║╚╝║║╚╝║║─║║║║─║║║║───║╚══╗\033[m
\033[1;33m─║║─║╔══╝──║║──║║─║║║║─║║║║─╔╗╚══╗║\033[m
\033[1;34m╔╣─╗║║─────║║──║╚═╝║║╚═╝║║╚═╝║║╚═╝║\033[m
\033[1;35m╚══╝╚╝─────╚╝──╚═══╝╚═══╝╚═══╝╚═══╝\033[m
    \033[1;36m ╔╗╔╗╔══╗╔═╗╔╦╗╔══╗╔═╦╗╔══╗\033[m
    \033[1;37m ║╚╝║║╔╗║║╔╝║╔╝╚║║╝║║║║║╔═╣\033[m
    \033[1;38m ║╔╗║║╠╣║║╚╗║╚╗╔║║╗║║║║║╚╗║\033[m
    \033[1;38m ╚╝╚╝╚╝╚╝╚═╝╚╩╝╚══╝╚╩═╝╚══╝\033[m
       \033[32mFerramentas para redes\033[m"""

print(inicio)
import webbrowser
import socket,os
import requests
from time import sleep

#loopbonito la em baixo
def loopbonito():
	for n in range(50):
		sleep(0.1)
		os.system("clear")
		print("\033[1;32mBaixando...\033[m")
		for b in range(0,n):
			print(f"\033[1;32m#\033[m",flush=True,end="")


def limpa_e_inicio():
	os.system("clear")
	return print(inicio)
	
while True:
	try:
		entrada = int(input("""
		\033[1;32m
	1 ver ip de site:
	2 ver todos os host de um site: 
	3 ver o host da maquina
	4 ver o ip da minha maquina
	5 ver triplo de hostname
	6 porta de protocolo
	7 porta pra ver qual o protocolo
	8 nome do usuario conectado
	9 ver infos.. do systema
	10 salva site.html
	11 porta Scan em desevolvimento..
	12 relata bugs Ao desevolvedor
	0 sair\t\033[m"""))
	
	except ValueError:
		print("\t \033[1;31;44mocorreu um erro\033[m")
		
	else:
		if (entrada ==1):
			limpa_e_inicio()
			#ver ip da maquina
			try:
				site = input("\t digite um site: ")
		
				print(f"\t \033[1;32;44m o ip do site e {socket.gethostbyname(site)} \033[m")
			except socket.gaierror:
				print("\t\033[32mocorreu um error\n\tEndereço errado ou sem Net\033[n")
				
			
		elif (entrada == 2):
			limpa_e_inicio()
			#ver todos os host da maquina
			try:
				site = input("\t digite um site pra ver todos os host: ")
				
				print(f"\t \033[1;32;44m todos os hosts são: {socket.gethostbyname_ex(site)} \033[m")
			except socket.gaierror:
				print("\t\033[32mocorreu um error\n\tEndereço errado ou sem Net\033[n")
				
			
			
		elif (entrada == 3):
			limpa_e_inicio()
		
			print(f"\t \033[1;32;44mo host e: {socket.gethostname()} \033[m")
		
		elif (entrada == 4):
			limpa_e_inicio()
	
			print(f"\t \033[1;32;44mo ip da maquina e \033[1;31m{socket.gethostbyname(socket.gethostname())} \033[m \033[m")
			
		
		elif (entrada == 5):
			limpa_e_inicio()
			ip = input("\t digite um ip numerico: ")
		
			print(f"\t \033[1;32;44minfos: {socket.gethostbyaddr(ip)}\033[m")
		
		
		elif (entrada == 6):
			limpa_e_inicio()
			digite = input("\t digite o protocolo ex: http:ftp.. ")
			
			print(f"\t \033[1;32;44ma porta do protocolo e : {socket.getservbyname(digite)}\033[m")
		
			
		elif (entrada == 7):
			limpa_e_inicio()
			numero = int(input("\t \033[1;32;44mnumero do protocol ex 21:\033[m"))
			
			print(f"\t \033[1;32;44mo protocolo e: {socket.getservbyport(numero)}\033[m")
		    
		    
		elif (entrada ==8):
			limpa_e_inicio()	
			print(f"\t \033[1;32;44mo nome do usuario e {os.getlogin()}\033[m")
			
		elif (entrada == 9):
			print(f"\t \033[1;32;44ma versao do seu systema e\n{os.uname()}\033[m")
			
			
		elif (entrada == 10):
			url = input("\t digite um site ex: https://.. ")
			response = requests.post(url)
			file = open('arquivo.html', 'w')
			file.write(response.text)
			print("Error")
			limpa_e_inicio()
			loopbonito()
			limpa_e_inicio()
			print("\t \033[1;45mum arquivo.html do site foi Salvo\033[m")
		
			
	
		
		elif (entrada == 11):
			print("\033[45mporta scanne em desevolvimento\033[m")
			
		elif (entrada == 12):
			print("\t relate um bug")
			webbrowser.open('http://t.me/codigo9090')
		
		elif (entrada == 0):
			print("\033[1;32mvc saiu\033[m")
			break


			
