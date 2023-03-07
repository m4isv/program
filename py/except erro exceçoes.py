try:
	a = int(input("numerodo: "))
	
	b = int(input("denominado: "))
	r = a / b 
	
except:
	print("infelizmente tivemos um problema")
	
else:
	print(f"o resultado e {r}")

finally:
	print("volte sempre muito obrigado")