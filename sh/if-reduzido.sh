clear

#IF REDUZIDO EM SHELL SCRIPT

NOME1="Maria"
NOME2="Ana"


#aqui e o if
[ "$NOME1" =  "$NOME2" ] && echo "Sao iguais"


#aqui e o else
[ "$NOME1" =  "$NOME2" ] || echo "Sao Diferentes"


