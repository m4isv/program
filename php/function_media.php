
<?php
system("clear");


function calcula_media($nome, $nota1, $nota2, $nota3, $nota4){
    
	$media = ($nota1 + $nota2 + $nota3 + $nota4) / 4;

	if($media >= 7):
	    print "aluno $nome APROVADO com nota $media\n";


	else:
	    print "aluno $nome REPROVADO com nota $media\n";


	endif;

}



calcula_media("maria", 5,9,9,10);
calcula_media("joao", 5,5,5,5);


?>
