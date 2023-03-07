
<?php

$dia = 3;
$km = 350;

$pago = ($dia * 60) + ($km * 0.15);

$real = number_format($pago, 2, '.', '');

print " total a pagar e de R$ $real\n";

?>
