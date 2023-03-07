def ajuda(com):
	help(com)


#programa principal
comando = ' '
while True:
	comando = str(input("Função ou biblioteca "))
	if comando.upper() == "FIM":
		break
	else:
		ajuda(comando)