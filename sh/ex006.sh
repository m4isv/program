clear
figlet CONVERSOR-MEDIDA

read -p "Uma Distancia em metro; " medida

CM=$(expr $medida \* 100)
MM=$(expr $medida \* 1000)

echo "A medida de $medida corresponde a $CM CM e $MM MM"

