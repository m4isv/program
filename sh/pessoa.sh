clear
cat pessoa.json | grep nome | cut -d":" -f2 | cut -d'"' -f2
cat pessoa.json | grep cpf | cut -d":" -f2 | cut -d'"' -f2
cat pessoa.json | grep mae | cut -d":" -f2 | cut -d'"' -f2
cat pessoa.json | grep pai | cut -d":" -f2 | cut -d'"' -f2

