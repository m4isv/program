N=1

while [ $N -lt 20 ]; do
	echo "Oi; $N"
	N=$(expr $N + 1)
done
