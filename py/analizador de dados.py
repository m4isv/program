sexo=str(input("informe seu sexo: [M/F]\n")).strip().upper()[0]
while sexo not in "MmFf":
	sexo=str(input("dados invalidos: por favor informe seu sexo\n")).strip().upper()[0]
print("sexo {} registrado com sucesso".format(sexo))