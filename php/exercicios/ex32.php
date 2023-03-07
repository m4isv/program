
<?php

$distancia = 500;

print "vc esta preste a começa uma viagem de $distancia km\n";

if($distancia <=200):
	$preco = $distancia * 0.50;


else:
    $preco = $distancia * 0.45;

print "e o preço da sua passagem sera de R$$preco\n ";


endif;

?>
