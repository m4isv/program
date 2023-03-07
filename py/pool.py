class meu_objeto:
	def __init__(self):
		self.nome = "pedro"
		self.idade = 17
		print("construtir chamado com sucesso")
	def imprime(self):
		print(f"ola meu nome e {self.nome} eu tenho {self.idade} Anos")
		
pedro = meu_objeto()

pedro.imprime()