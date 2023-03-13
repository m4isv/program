clear

NUM=1

while [ $NUM -lt 30 ]; do
    echo $NUM; 
	NUM=$(expr $NUM + 1 ); 
done
