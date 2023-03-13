case "$1" in
	[0-9])
	echo "O parametro e um numero"
	;;

        [A-Z])
	echo "O parametro e uma letra Maiusula"
	;;

	[a-z])
	echo "O parametro e uma letra minuscula"
	;;

	*)
	echo "O parametro e um carectere "
esac
