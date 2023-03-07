<?php

$items = array("pedra", "papel", "tesoura");

$computador = rand(0,2);

$jogador = 0;

$escolhe_computado = $items[$computador];

$escolhe_usuario = $items[$jogador];

print "O computador jogou $escolhe_computado\n";

print "O jogado jogou $escolhe_usuario\n";


if($escolhe_computado ===  $escolhe_computado || $escolhe_usuario): 
    if($escolhe_usuario ===   $escolhe_computado ):
        print "EMPATE\n";
 
    elseif($escolhe_usuario !==  $escolhe_computado):
        print "JOGADO VENCE\n";
 
    elseif($escolhe_usuario !==  $escolhe_computado):
        print "COMPUTADOR VENCE\n";
 
    else:
        print "JOGADA INVALIDA\n";
    endif;

endif;

?>