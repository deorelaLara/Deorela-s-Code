<?php
include("class/class_catalogo_curso_dal.php");
if(isset($_POST['id'])){
   $id=  $_POST['id'];
			$metodos_cursos=new catalogo_cursos_dal;
			$obj_curso=new catalogo_curso($id,NULL);
			$cuantos=$metodos_cursos->borra_curso($obj_curso);
      echo $cuantos;
}
else{
  echo "no llego correctamente el id, error backend";
}
?>