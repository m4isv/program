
<?php

system("clear");


print str_repeat("-" ,30)."\n";

print "converso de base numericas\n";

print str_repeat("-", 30)."\n";

print "digite um numero\n";


$opcoes = "[ 1 ] para binario\n[ 2 ] para octal\n[ 3 ] para hexdecimal\n";

print $opcoes;

$opcoes = 1;
$numero = 10;


if($opcoes == 1):
	print "$numero convertido para binario e ".decbin($numero)."\n";

elseif($opcoes == 2):
	print "$numero convertido para octal e ".decoct($numero)."\n";

elseif($opcoes == 3):
	print "$numero convertido para hexdecimal e ".$dechex($numero)."\n";

endif;



?>
