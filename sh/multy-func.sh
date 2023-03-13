clear
read -p "Nome; " nome
read -p "idade; " idade
read -p "sexo; " sexo
read -p "signo; " signo
echo

function NOME(){
    local nome="TANAJURA"
    echo $nome
}

function IDADE(){
    echo $idade
}

function SEXO(){
    echo $sexo
}

function SIGNO(){
    echo $signo
}

NOME
IDADE
SEXO
SIGNO
