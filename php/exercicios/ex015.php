
<?php
$c = 40;

$f = ((9 * $c) / 5) + 32;

$formata = number_format($f, 1, '.', '');

print "a temperatura de $c celcius corresponde a  $formata fareheit\n";

?>
