
<?php

print "apenas pares de 1 a 50\n";

for($num=1; $num <= 50; $num ++):
	if($num % 2 ==0):
		print  "$num,";
		;
	endif;

endfor;



?>
