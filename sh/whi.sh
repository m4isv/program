NUMERO=1

while [ $NUMERO -lt 10 ]; do
    echo $NUMERO
    NUMERO=$(expr $NUMERO + 1)

done
