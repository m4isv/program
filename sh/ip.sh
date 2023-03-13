echo "Seu ip e \n"

curl 'https://api.ipify.org?format=json' -s | cut -d'"' -f4
