<?php

$nome = "maria da silva";

function exibinome()
    {global $nome;
    print "$nome\n";}
    

exibinome();




function soma(){
    $numero1 = 10;
    $numero2 = 20;
    $total = $numero1 + $numero2;
    
    print $total;}

soma();



?>