clear

read -p "Faça login no sistema; " login

[ $login = "admin" ] && echo "Bem vindo $(whoami)"

[ $login = "admin" ] || echo "Usuario invalido"
