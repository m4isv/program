echo "digite seu nome"
read nome

echo -n "Seu nome e "
sleep 2

echo "$nome" | tr a-z A-Z
