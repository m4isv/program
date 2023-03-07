clear

figlet SUCESSOR
date +%d/%m/%Y

read -p "Digite um Numero; " numero

echo "O Numero Digitado Foi $numero"

SUCESSOR=$(expr $numero + 1)
ANTECESSOR=$(expr $numero - 1)


echo "o Sucessor e $SUCESSOR "
echo "o Antecessor e $ANTECESSOR"


