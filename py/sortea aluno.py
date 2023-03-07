import random
while True:
	n1 = input("Primeiro aluno ")
	n2 = input("Segundo aluno ")
	n3 = input("Terceiro aluno ")
	n4 = input("Quarto aluno ")
	lista = [n1, n2, n3, n4 ]
	escolhido = random.choice(lista)
	print("o Aluno escolhido foi {} ".format(escolhido))