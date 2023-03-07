numeros = list()

while True:
	n = int(input("digite um valor\n"))
	if n not in numeros:
		numeros.append(n)
	
	else:
		print("Valor duplicado nao vou adiciona")
		r = str(input("quer continuar sim ou nao\n"))
		if r in "Nn":
			break
			
numeros.sort()
print(f"vc digitou os valores {numeros}")
	