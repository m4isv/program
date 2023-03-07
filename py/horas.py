from time import sleep
print ('''HORAS AM | PM : 
[ 0 ] DAS 00:00 ÁS 05:59 
[ 1 ] DAS 06:00 ÁS 12:59
[ 2 ] DAS 13:00 ÁS 18:59
[ 3 ] DAS 19:00 ÁS 23:59''')
hora = int (input ('Selecione uma opção de acordo com a sua hora: '))
if hora == 0:
    print ()
    print ('BOA MADRUGADA !!!')
elif hora == 1:
    print ()
    print ('BOM DIA !!!')
elif hora == 2:
    print ()
    print ('BOA TARDE !!!')
elif hora == 3:
    print ()
    print ('BOA NOITE !!!')
elif hora > 3:
    print ()
    print ('OPÇÃO INVÁLIDA !!!')
sleep (0.5)
print ('''Voce está bem?
[ 0 ] ESTOU MUITO BEM
[ 1 ] ESTOU BEM
[ 2 ] NÃO MUITO
[ 3 ] NAO ESTOU BEM''')
humor = int (input ('Selecione a opção de acordo com seu humor: '))
if humor == 0:
    print ('MAS QUE BOM!!!')
if humor == 1:
    print ('MAS QUE BOM!!!')
if humor == 2:
    print ('TENTE PROCURAR FAZER ALGUMA COISA QUE TE FAÇA MELHOR!!!')
if humor == 3:
    print ('PROCURE A AJUDA DE ALGUÉM E TENTE FAZER ALGUMA COISA PARA SE SENTIR MELHOR!!!')
if humor > 3:
    print ('OPÇÃO INVALIDA!!!')
print ()
print ('ESPERO TER AJUDADO EM ALGO!!!')