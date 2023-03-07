def dobra(x):
	return x *2

valor = [1,2,3,4,5]

valor_dobrado = map(dobra, valor)

valor_dobrado = list(valor_dobrado)

print(valor_dobrado)