if grep "$1" /etc/passwd > /dev/null
then
	echo "O usuario existe"
else
	echo "O usurio nao existe"
fi
