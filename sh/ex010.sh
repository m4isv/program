clear

figlet TABUADA

read -p "Digite um Numero Para ver sua Tabuda; " NUMERO
echo

for num in $(seq 1 10); do 
	echo "$NUMERO X $num = $(expr $NUMERO \* $num)"; 
done


