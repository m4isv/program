clear

read -p "whats your name?; " name

if [[ $name = maria ]]; then
	echo "Welcome, maria "

else 
        figlet ERROR
fi
