<?php

$numero_aleatorio = mt_rand(0,10);

if ($numero_aleatorio % 2==0):
	print "o numero $numero_aleatorio e par\n";

else:
    print "o numero $numero_aleatorio e impar\n";

endif;

?>
