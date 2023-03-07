from random import randint as aleatorio
import os

def abre_cor(a = "\033[1;34;31m"):
	print(a)
	
def feixa_cor(b = "\033[m"):
	print(b)

while True:
	try:
		print("\t \033[7;32;44m tente adivinha o numero de 0 A 10 \033[m")
		maquina = int(aleatorio(0,2))
		
		numero = int(input("\t Numero: "))
		os.system("clear")
		
		if numero == maquina:
			abre_cor()
			print(f"\t \033[1;34;43m acertou Mizeravel foi o {maquina} \033[m")
			feixa_cor()
			
			if numero == maquina:
				resposta = input("\t quer continua jogando sim ou nao? ").strip()
				os.system("clear")
				if resposta[0].upper() in "N":
					print("\t terminou")
					break
			
		else:
			abre_cor()
			print(f"\t errou foi o \033[1;34m{maquina}\033[m  \033[1;34;31mnao o\033[m  \033[1;33m{numero}\033[m")
			feixa_cor()
	
	except:
		print("\t \033[1;34;31mocorreu um error\033[m")

