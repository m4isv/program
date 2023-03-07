def escrevar(msg):
	'''escrever adptador ao tamanho da letra, coloque escrevar('quaque coisa aqui') ele escreve com a linha do mesmo tamanho do texto'''
	
	tam = len(msg) 
	print('-' * tam)
	print(msg)
	print('-' * tam)


escrevar('ola mundo')
escrevar('curso em video')

help(escrevar)