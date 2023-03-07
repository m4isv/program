class pessoa:
	def __init__(self):
		self.nome = "maria"
		self.idade = 19
		self.sexo = "feminina"
	
	
	def imprime(self):
		print(f"ola meu nome e {self.nome} eu tenho {self.idade} anos e sou do\nsexo {self.sexo}")
		
maria = pessoa()

maria.imprime()