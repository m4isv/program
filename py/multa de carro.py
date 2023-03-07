velocidade = float(input("qual a velocidade\n"))

if velocidade > 80:
	print("multado")
	
	multa = (velocidade - 80) * 7
	
	print(f"vc deve pagar uma multa de {multa}R$")

print("tenham um bom dia! dirijam com segurança")