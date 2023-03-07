import os

def soma(n1,n2):
	return n1+n2
	
def subtrai(n1,n2):
	return n1+n2
	
def multiplica(n1,n2):
	return n1+n2

def dividi(n1,n2):
	return n1+n2

while True:
	inicio = int(input("""\t oque voce quer faze? digite
	1 para calculadora
	2 para sair: """))
	
	#limpa inicio
	os.system("clear")
	
	if inicio == 1:
		print("\t    calculadora")
		
		num = int(input("""\t 
		digite
		1 para soma
		2 para subtrai
		3 para multiplica
		4 para dividi: """))
		
		#limpa num
		os.system("clear")
		
		if num == 1:
			print("\t soma")
		    n1 = int(input("\t numero 1: "))
			n2 = int(input("\t numero 2: "))
			
		     print(f"\t A soma é: {soma(n1,n2)}")
		