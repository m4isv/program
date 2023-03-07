def leiaint(msg):
	while True:
		try:
			n = int(input(msg))
		except (ValueError, TypeError):
			print("\033[31mError, por favor digite um numero inteiro valido\033[m")
			continue
		except(KeyboardInterrupt):
			print("entrada de dados enterrompida  pelo usuario")
		else:
			return n
num = leiaint("digite um valor ")
print(f"O valor digitado foi {num}")