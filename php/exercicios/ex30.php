
<?php

$velocidade = 500;

if($velocidade > 80):
    print "MULTADO voce excedeu o limite permitido que e de 80 km/h\n";
    $multa = ($velocidade - 80) * 7;
    print "vc deve pagar uma multa de R$$multa\n";

else:
    print "tenham um bom dia dirija com segurança\n";


endif;

?>
