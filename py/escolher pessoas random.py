import random
p1 = input("primeiro aluno\n")
p2 = input("segundo aluno\n")
p3 = input("terceiro aluno\n")
p4 = input("quarto aluno\n")

lista = [p1,p2,p3,p4]
escolhido = random.choice(lista)
print(f"o aluno escolhido foi {escolhido}")
