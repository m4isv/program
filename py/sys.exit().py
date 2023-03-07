import sys

pessoas = []

while True:
	try:
		p = input('digite um Nome: ').strip().title()
		pessoas.append(p)
		r = input('quer adiciona mais pessoas sim ou nao?: ').strip()
		if r[0].upper() == 'N':
			print(f'as pessoas adicionadas foram\n{pessoas}')
			sys.exit()
		
	except Exception as error:
		print(f'ocorreu um error do tipo {error} ')