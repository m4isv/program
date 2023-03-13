clear

frutas=("banana" "maça" "pera" "mamao" "melao" "abacate")


for pecorre in "${frutas[@]}"; do
	echo "$pecorre"
done



echo "--------------while-----------------"

contador=0

while [[ $contador -lt ${#frutas[@]} ]]; do
	echo $contador
	contador=$(( $contador + 1 ))
done


echo "total de items $contador"
