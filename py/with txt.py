"""
msg = "ola mundo"

#escreve tudo de msg with
with open('arquivo.txt', 'w') as escreva:
	escreva.write(msg)"""
	


#ler o arquivo escrito
with open('arquivo.txt', 'r') as ler:
	print(ler.read())
