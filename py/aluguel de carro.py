try:
	dias = int(input("\033[7;32;41m quantos dias alugado?\n\033[m"))
	
	km = float(input("\033[7;32;41m quantos km rodados\n\033[m"))
	
	pago = (dias * 60) + (km * 0.15)
	
	print(f"o total a pagar e de \033[7;31;44m {pago} \033[m")
	
except:
	print("Ocorreu um \033[1;30;41m Error \033[m ")