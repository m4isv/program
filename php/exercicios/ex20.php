<?php


$aluno1 = "maria";
$aluno2 = "julia";
$aluno3 = "gabriela";

$todos = array($aluno1, $aluno2, $aluno3);

$escolhido = array_rand($todos, 2);


print "O ALUNO ESCOLHIDO FOI:".$todos[$escolhido[1]]."\n";



?>
