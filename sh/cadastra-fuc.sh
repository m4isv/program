clear

function PESSOA(){
    read -p "Nome; " nome
    read -p "Nascimento; " nascimento

}

PESSOA



function IMPRIME(){
    echo "Seu Nome e $nome"
    echo "Seu Nascimento e $nascimento"
}


IMPRIME
