
<?php

system("clear");


print "digite um numero para ver sua tabuada\n";

$numero = 5;

for($num=0; $num <=10;$num ++):
	$resultado = $numero * $num;
	
	print "$numero X $num = $resultado\n";

endfor;

?>
