
<?php

print "-----------------------\n";
print "ANALIZADO DE TRIANGULO\n";
print "-----------------------\n";

$r1 = 3;
$r2 = 3;
$r3 = 3;

if($r1 < $r2 + $r3 and $r2 < $r1 + $r3 and $r3 < $r1 + $r2):
    print "Os Seguimentos acima pode FORMA UM TRIANGULO\n";


else:
    print "Os Seguimentos ACIMA nao pode forma um Triangulo\n";


endif;

?>
