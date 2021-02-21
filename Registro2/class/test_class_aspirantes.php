<?php
include('class_aspirantes_dal.php');
$obj_aspi=new aspirantes_dal;
$resultado=$obj_aspi->datos_por_rfc("PETD7407148Z1");

/*prueba datos_por_id($id)*/
if ($resultado==null){
	echo 'no EXISTE aspirante';
}
else{
	echo '<pre>';
	print_r($resultado);
	echo '</pre>';
}


/*prueba obtener_lista_aspirantes()*/
$resultado2=$obj_aspi->obtener_lista_aspirantes();
if ($resultado2==null){
	echo '<br/>No se encontró lista de registros cursos';
}
else{	
	echo '<pre>';
	print_r($resultado2);
	echo '</pre>';
}

/*prueba existe_aspirante()*/
$cuantos=$obj_aspi->existe_aspirante("PETD7407148Z1");
echo "Coincidencias:".$cuantos;

/*prueba inserta ASPIRANTE()*/
/*
$obj_det= new aspirantes("JOSE010102AAy","KARLAy","SAUCEDAy","GARAYy","COCA COLAy",5,"ay@gmail.com",null);
$cuantos=$obj_aspi->insertar_aspirante($obj_det);
if ($cuantos==1){
		echo "<br>Aspirante registrado correctamente";
}
else{
		print "<br>EL Aspirante no pudo registrarse, vuelva a intentar";
}
*/

/*prueba borrado aspirantes()*/
$obj_det= new aspirantes('JOSE010102AAA');
$cuantos=$obj_aspi->borra_aspirante($obj_det);
if ($cuantos==1){
		echo "<br>Aspirante borrado correctamente";
}
else{
		print "<br>EL aspirante no pudo borrar, vuelva a intentar";
}


/*prueba update ASPIRANTE()*/

$obj_det= new aspirantes("PETD7407148Z1","DANIEL","PEREZ","TINOCO","SE",'844112','X@H.COM');
$cuantos=$obj_aspi->actualiza_aspirantes($obj_det);
if ($cuantos==1){
		echo "<br>Aspirante ACTUALIZADO correctamente";
}
else{
		print "<br>EL Aspirante no pudo ACTUALIZARSE, vuelva a intentar";
}


?>