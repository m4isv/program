
<?php

$salario = 1000;

if($salario <= 1250):
    $novo = $salario + ($salario * 15 / 100);
    $formata = number_format($novo, 2, ',', ' ');


else:
    $novo = $salario + ($salario * 10 / 100);
    $formata = $number_format($novo, 2, ',', '');


endif;


print "quem ganhava $salario passa a ganha R$ $formata\n";
?>
