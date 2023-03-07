
<?php

$ano = 1900;

if($ano % 4 == 0 and $ano % 100 !=0 or $ano % 400 ==0):
	print "o ano $ano e bisexto\n";

else:
    print "o ano $ano nao e bisesto\n";

endif

?>
