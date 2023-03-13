clear

figlet PROCURA-CPF


arquivo=$(cat pessoa.json)

MY_RE=$(egrep "[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}" pessoa.json | cut -d'"' -f4)

echo $MY_RE

