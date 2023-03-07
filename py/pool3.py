class pessoa:
	def __init__(recebe):
		recebe.nome = "maria"
		recebe.idade = 19
		recebe.sexo = "feminina"
	
	
	def imprime(recebe):
		print(f"ola meu nome e {recebe.nome} eu tenho {recebe.idade} anos e sou do\nsexo {recebe.sexo}")
		
maria = pessoa()

maria.imprime()