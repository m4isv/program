echo -e "\033[;45mDIGITE SEU NOME\033[m"

read NOME

echo -n "Seu Nome em maiuscula e "
echo -e "$NOME\n" | tr a-z A-Z

echo -n "e em minusculo "
echo -e "$NOME\n" | tr A-Z a-z
