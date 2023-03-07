list = []

while True:
	numero = int(input("digite um numero\n"))
	
	list.append(numero)
	
	resposta = input("quer Continuar [S/N]\n")
	if resposta in "Ss":
		print("Continue")
		continue
	
	elif resposta in "Nn":
		print("acabou")
		break

print(f"os numeros quer vc digitou foram {list} ")

print(f"O Maior numero digitado foi {max(list)} e o Menor Foi {min(list)}")