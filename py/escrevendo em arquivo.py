arq = open('arquivo.txt','w')

texto = '''
python e muito bom
foi criado por van guildo roff
a comunidade e muito boa
'''
arq.write(texto)

#escrevendo em um arquivo

arq.open('arq.txt','w')

texto = '''
python foi criado por guildo van dov
a comunidade python e muito boa
python 2020
'''
arq.write(texto)

arq.close()