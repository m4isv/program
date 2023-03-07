clear

figlet ARITMETICA
echo -e "\033[1;45mDIA DE HOJe\033[m" 

date +%d/%m/%Y
echo 

read -p "Digite um Numero; " numero

DOBRO=$(expr $numero \* 2)
TRIPLO=$(expr $numero \* 3)
RAIZ=$(bc <<< "scale=0; sqrt($numero)")


echo "O dobro de $numero e $DOBRO"
echo "O triplo de $numero e $TRIPLO"
echo "O raiz de $numero e $RAIZ"

