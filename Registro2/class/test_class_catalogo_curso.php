<?php
include('class_catalogo_curso_dal.php');
$obj_curso=new catalogo_cursos_dal;
$resultado=$obj_curso->datos_por_id(1);

/*prueba datos_por_id($id)*/
if ($resultado==null){
	echo 'no hay resutados';
}
else{
	echo '<pre>';
	print_r($resultado);
	echo '</pre>';
}


/*prueba obtener_lista_cursos()*/
$resultado2=$obj_curso->obtener_lista_cursos();
if ($resultado2==null){
	echo '<br/>No se encontró lista de registros cursos';
}
else{	
	echo '<pre>';
	print_r($resultado2);
	echo '</pre>';
}

/*prueba existe_cursos()*/
$cuantos=$obj_curso->existe_curso(6);
echo "Coincidencias:".$cuantos;

/*prueba inserta curso()*/
/*
$obj_det= new catalogo_curso(1,"Progra 1",null);
$cuantos=$obj_curso->insertar_curso($obj_det);
if ($cuantos==1){
		echo "<br>Curso registrado correctamente";
}
else{
		print "<br>EL curso no pudo registrarse, vuelva a intentar";
}
*/


/*prueba borrado curso()*/
$obj_det= new catalogo_curso(6);
$cuantos=$obj_curso->borra_curso($obj_det);
if ($cuantos==1){
		echo "<br>Curso borrado correctamente";
}
else{
		print "<br>EL curso no pudo borrar, vuelva a intentar";
}

?>