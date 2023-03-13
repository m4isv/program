clear

while true
do
	read -p "Qual seu nome?; " nome

	if [[ $nome = "maria" ]]; then
		echo "Bem vinda maria de volta"
		break
	fi

done
