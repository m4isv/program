<?php

$real = 100;

$dolar = ($real / 5.37);

$formata = number_format($dolar, 2, '.', '');

print "com R$ $real reais  você pode compra U$ $formata dolares americano\n";

?>
