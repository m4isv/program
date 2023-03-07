clear
figlet MEDIA

read -p "Primeira Nota; " nota1
read -p "Segunda Nota; " nota2

MEDIA=$(expr $nota1 + $nota2 / 2)

echo "A media entre $nota1  e $nota2 e $MEDIA"

