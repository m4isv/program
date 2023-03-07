
<?php

print "-------jogo do adivinha---------\n";
print "----em qual numero eu pensei?---\n\n";

$computador = rand(0, 10);

$jogado = 5;

if($jogado == $computador):
    print "ACERTOU eu pensei no numero $computador e vc digitou o $jogado\n";

else:
    print "ERROU eu pensei no numero $computador e vc digitou o $jogado\n";

endif;

?>
