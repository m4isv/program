clear
figlet TABUADA

NUMERO=5

for n in $(seq 1 10); do
	echo "$n X $NUMERO = $(expr $n \* $NUMERO)"
done
