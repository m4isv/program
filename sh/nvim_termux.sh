clear

pkg update -y
pkg update --fix-missing
pkg install termux-api -y
pkg install nodejs-lts git lua54 ripgrep fd -y


#PYTHON INSTALADO ?
PYTHON="$(which python)"
if [ $? -eq 0 ]; then
  echo "PYTHON JA INSTALADO"

else
  pkg install python -y
fi



#NEOVIM INSTALADO ?
NEOVIM="(which neovim)"
if [ $? -eq 0 ]; then
  echo "NEOVIM JA INSTALADO"
  rm -rf $HOME/.local/state/nvim
  rm -rf $HOME/.local/share/nvim
  rm -rf $HOME/.config/nvim
else
  pkg install neovim -y
fi

git clone https://github.com/outragedline/neovim-termux .config/nvim

echo "Entre no nvim e digite :PackerSync"
  

  

