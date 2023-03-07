<?php

$aluno1 = "maria";
$aluno2 = "juliana";
$aluno3 = "bianca";


$numbers = array($aluno1, $aluno2, $aluno3);
	
shuffle($numbers);

print "a ordem de apresentação sera\n";



foreach ($numbers as $escolhido) 
    {print "[$escolhido ]";}



?>
