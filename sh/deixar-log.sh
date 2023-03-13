clear

figlet LOG

DATAHORA=$(date +%H:%M)
LOG="/home/masv/sh/aut.log"

echo "iniciando o script: $DATAHORA" >> $LOG

for n in $(seq 1 10); do
	echo $n
done

echo "Finalizando o script $DATAHORA" >> $LOG
