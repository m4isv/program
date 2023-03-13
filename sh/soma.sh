set -x

echo "Digite um numero"
read numero1

echo "Digite outro Numero"
read numero2


soma=$(($numero1 + $numero2))
set +x

echo "A soma e $soma"
