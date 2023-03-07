def dobra(lista):
	pos = 0
	while pos < len(lista):
		lista[pos] *= 2
		pos += 1


valores = [10, 20, 30, 40, 50]
dobra(valores)
print(valores)