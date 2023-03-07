<?php 

$pegar = $_POST["numero"];

for($num =1; $num <= 10; $num ++):
    $resultado = $pegar * $num;
    
    print "$pegar X $num = $resultado<br>";
   
endfor;

?>