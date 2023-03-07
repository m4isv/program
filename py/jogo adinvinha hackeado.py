from random import randint

from time import sleep as espera

computado = randint(0,5)
print(f"hacker activer {computado}")

print("vou pensa em um numero entrer 0 e 5 tente adivinha..")

jogador = int(input("em que numeto eu pensei?\n"))

print("processando....")
espera(4)
if jogador == computado:
	print("parabèns vc a certou...")
	
else:
	print(f"erroue eu pensei no numero {computado} e nao no {jogador}")