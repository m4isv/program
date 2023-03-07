import os

lista = []

for pessoa in range(0,5):
	nome = input('adicione uma oessoa na lista: ')
	
	lista.append(nome)
	os.system('clear')
	
	print('adicionado com sucesso')
	
	print('terminal limpado')

print(f'as pessoas adicionadas na lista foram {lista}')
	