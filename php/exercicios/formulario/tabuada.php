<!DOCTYPE html>
<html>
<head>

<meta name="viewport"content="width=device-width,initial-scale=1">

<title>tabuada</title>

<style type="text/css">

body {background-color:#7304bd;}
h1 {background-color:#52c308;}
p {background-color:#f70c00;color:#10efef;}
h4 {background-color:#10fb08;color:291cad;}

</style>

</head>
<body>


<center>
<h1>tabuada 2021</h1>
</center>

<p>quer ver a tabuada de qual Numero?</p>


<form action=""  method="post" >

<input type="text" name="numero" placeholder="digite o numero" required="required" >


<input type="submit" name="ver" value="ver"  >

</form><br>

<center>
<h4>
    
<?php 

$pegar = $_POST["numero"];

for($num =1; $num <= 20; $num ++):
    $resultado = $pegar * $num;
    
    print "$pegar X $num = $resultado<br>";
   
endfor;

?>
</h4>
</center>
</body>
</html>