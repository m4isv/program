<?php

//system("clear");

///faça um programa que receba 3 numeros e mostre o maior e o menor deles


$numero1 = 10;
$numero2 = 100;
$numero3 = 9;

$maior = $numero1;
$menor = $numero1;

//parte maior
if($numero1 > $numero2 and $numero1 > $numero3):
	$maior = $numero1;


elseif($numero2 > $numero1 and $numero2 > $numero3):
	$maior = $numero2;


elseif($numero3 > $numero2 and $numero3 > $numero1):
	$maior = $numero3;
endif;


///parte menor

if($numero1 < $numero2 and $numero1 < $numero3):
	$menor = $numero1;


elseif($numero2 < $numero1 and $numero2 < $numero3):
	$menor = $numero2;

elseif($numero3 < $numero2 and $numero3 < $numero1):
	$menor = $numero3;

endif;


print "o maior numero digitado e o $maior\n";

print "E o menor numero digitado e o $menor\n";


?>
