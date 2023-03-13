clear
ARTE=$(cat arte.txt)

echo -e "\033[1;455m$ARTE\033[m"

figlet MENU

MENU="ecolha uma opçao\n
1 opçao\n
2 opçao\n
3 opçao\n
4 opçao\n"

echo -e $MENU

read -p "Escolha; " ESCOLHE

#declaraçao if
if [[ $ESCOLHE = 1 ]]; then
	echo "opçao 1 escolhida"

elif [[ $ESCOLHE = 2 ]]; then
	echo "opçao 2 esolhida"

elif [[ $ESCOLHE = 3 ]]; then
	echo "opçao 3 escolhida"

elif [[ $ESCOLHE = 4 ]]; then
	echo "opçao 4 escolhida"

else "Nenhuma das Opçao escolhida"

fi
