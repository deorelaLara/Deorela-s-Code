<?php  
if ($_POST){

	$va=$_POST["a"];
	$vb=$_POST["b"];


	if ($vb!=0){	
			print "El valor de a es:".$va.' y el valor de b es:'.$vb;
			echo "<br/>"."El resultado de la division es:".($va/$vb);
		}
		else{
			echo "La division por cero no es posible";
		}

}
else{
		$i = 1;
		while ( $i <= 5 )
		{
			print("$i<br />");
			$i++; // equivalente a hacer: $i = $i + 1;
		}
}

?>
<!DOCTYPE html>
<html>
<head>
	<title>Ejercicio</title>
</head>
<body>
<h1>Operación de division</h1>
<form action="#" method="post" accept-charset="utf-8">

	<input type="text" name="a">
	<input type="text" name="b">
	<input type="submit" name="ejecuta" value="Calcuar">

</form>
</body>
</html>