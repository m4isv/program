clear
figlet GET-PROXY

DATAHORA=$(date)
LOG="/home/masv/sh/ex/proxy/aut.log"

echo "iniciando Programa; $DATAHORA" >> $LOG

URL="https://www.proxy-list.download/api/v1/get?type=http"
curl -n $URL >> proxy.txt

echo "Salvo em Proxy.txt"
echo "Log; criado em aut.log"

echo "Finalizando Programa; $DATAHORA" >> $LOG
