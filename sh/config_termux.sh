clear

echo -e "EXCUTE ESSE ESSE SCRIOT NO $HOME DO TERMUX\n\nATUALIZANDO TUDO AGUARDE...\n\n"

#saida padrao 2> para saida de error &1 e tudo para null
pkg update --fix-missing -y  #> /dev/null 2>&1
pkg update -y             #> /dev/null 2>&1
pkg upgrade -y            #> /dev/null 2>&1
apt list --upgradable     $> /dev/null 2>&1


echo "iINSTALANDO PYTHON E NEOVIM..."
#python instalado ?
[ ! -x "$(which python3)" ] && pkg install python3 -y > /dev/null 2>&1
#neovim instalado ?
[ ! -x "$(which nvim)" ] && pkg install neovim -y > /dev/null 2>&1
clear
echo "AGUARDE..."
sleep(10)

pkg install git -y > /dev/null 2>&1
echo "INSTALANDO CURL..."
pkg install curl -y > /dev/null 2&1

echo "BAIXADO O SPACE VIM PARA EDITA CODIGO NO NVIM com autocomplete"
curl -sLf https://spacevim.org/install.sh | bash


echo "BAIXANDO AUTOCOMPLETE PARA O TERMINAL"

git clone --recursive https://github.com/akinomyoga/ble.sh.git

cd ble.sh && make 

chmod a+x out/ble.sh

cd 

echo "source ble.sh/out/ble.sh" > .bashrc
