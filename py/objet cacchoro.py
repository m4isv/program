class Animal():
	def __init__(self,tipo,nome,sexo):
		self.tipo=tipo
		self.nome=nome
		self.sexo=sexo
		
	def comer(self):
		return print(f"o {self.tipo} {self.nome} estar comendor")
		
cachorro = Animal("cachorro","rex","masculino")

print(f"{cachorro.tipo} {cachorro.nome} {cachorro.sexo} ")
cachorro.comer()
