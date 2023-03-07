ls /home/$1 > /dev/null 2>&1 || { echo "Usuari inexistente"; exit 1; }
USERID=$(grep $1 /etc/passwd|cut -d":" -f3)
DESC=$(grep $1 /etc/passwd|cut -d":" -f5 | tr -d ,)
USOHOME=$(du -sh /home/$1|cut -f1)

clear
echo "======================================="
echo "Relatorio do usuario; $1"
echo

echo "UID; $USEID"
echo "Nome ou Descriçao: $DESC"
echo

echo "Total usado no /home$1; $USOHOME"
echo

echo "Ultimo Login;"
lastlog -u $1
echo "======================================="
exit 0
