<?php

$cateto_oposto = 2;
$cateto_adjacente = 2.5;

$hipotenusa = ($cateto_oposto ** 2 + $cateto_adjacente ** 2) ** (1/2);

$formata = number_format($hipotenusa, 2, '.', '');


print "a hipotenusa vai medir $formata\n";

?>
