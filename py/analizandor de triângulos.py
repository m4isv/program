r1 = float(input("\033[7;32;41m primeiro segmento\n\033[m"))

r2 = float(input("\033[7;32;41msegundo segmento\n\033[m"))

r3 = float(input("\033[7;32;41mterceiro segmento\n\033[m"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print("os segmentos acima \033[1;31;43mpodem forma triangulos\033[m")
	
else:
	print("Os segmentos \033[1;31;41mnao podem forma triangulos\033[m")