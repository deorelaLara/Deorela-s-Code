<!DOCTYPE html>
<html>
<head>
    <title>Catálogo de Cursos</title>
    <?php include_once "inclusiones/css_y_favicon.php"; ?>
</head>
<body>
</body>
</html>
<?php
include_once "inclusiones/js_incluidos.php";
if($_POST){
	require_once 'php/funciones_php.php';

	if (isset($_POST["irfc"])) 
  		{
    		$rfc=strtoupper($_POST["irfc"]);
  		}else{
    		$rfc=null;
    		echo "no se recibio post";
    		exit;
    	}

	if (isset($_POST["inombre"])) 
  		{
    		$nombre=strtoupper($_POST["inombre"]);
  		}else{
    		$nombre=null;
    		echo "no se recibio post";
    		exit;
    	}

	if (isset($_POST["ipaterno"])) 
  		{
    		$paterno=strtoupper($_POST["ipaterno"]);
  		}else{
    		$paterno=null;
    		echo "no se recibio post";
    		exit;
    	}

	if (isset($_POST["imaterno"])) 
  		{
    		$materno=strtoupper($_POST["imaterno"]);
  		}else{
    		$materno=null;
    		echo "no se recibio post";
    		exit;
    	}

	if (isset($_POST["iempresa"])) 
  		{
    		$empresa=strtoupper($_POST["iempresa"]);
  		}else{
    		$empresa=null;
    		echo "no se recibio post";
    		exit;
    	}

	if (isset($_POST["itelefono"])) 
  		{
    		$telefono=strtoupper($_POST["itelefono"]);
  		}else{
    		$telefono=null;
    		echo "no se recibio post";
    		exit;
    	}

	if (isset($_POST["iemail"])) 
  		{
    		$email=strtoupper($_POST["iemail"]);
  		}else{
    		$email=null;
    		echo "no se recibio post";
    		exit;
    	}    	    	    	    	    	    	

	if (isset($_POST["scurso"])) 
  		{
    		$curso=strtoupper($_POST["scurso"]);
  		}else{
    		$curso=null;
    		echo "no se recibio post";
    		exit;
    	}
/*
    	echo 'hubo post:'.$rfc.'<br>nombre:'.$nombre.'<br>paterno:'.$paterno.'<br>materno:'.$materno.'<br>empresa:'.$empresa.'<br>telefono:'.$telefono.'<br>email:'.$email.'<br>curso:'.$curso;
    	*/

//validaciones lado del servidor 
//$rfc="";
//$curso="0";   	
$errores = array();
	if ($_SERVER['REQUEST_METHOD'] == 'POST') {
		if (!validaRequerido($rfc)) {
      		$errores[] = 'El campo RFC se recibió vacio.';
   		}

		if (!validaRequerido($nombre)) {
      		$errores[] = 'El campo nombre se recibió vacio.';
   		}

		if (!validaRequerido($paterno)) {
      		$errores[] = 'El campo Paterno se recibió vacio.';
   		}

		if (!validaRequerido($materno)) {
      		$errores[] = 'El campo Materno se recibió vacio.';
   		}

		if (!validaRequerido($empresa)) {
      		$errores[] = 'El campo DE EMPRESA se recibió vacio.';
   		}   		   		

		if (!validaRequerido($telefono)) {
      		$errores[] = 'El campo DE TELEFONO se recibió vacio.';
   		}

		if (!validarNumerico($telefono)) {
      		$errores[] = 'El campo DE TELEFONO DEBE SE NUMERICO.';
   		}   		

		if (!validaRequerido($email)) {
      		$errores[] = 'El campo DE EMAIL se recibió vacio.';
   		}

		if (!validaEmail($email)) {
      		$errores[] = 'El campo DE EMAIL NO ESTA FORMADO CORRECTAMENTE.';
   		}

   		if (!validaSelecthtml($curso)) {
      		$errores[] = 'No ha seleccionado un curso.';
   		}



   		if(!$errores){
   			//la logica de inserción
   			/*
   			echo 'hubo post:'.$rfc.'<br>nombre:'.$nombre.'<br>paterno:'.$paterno.'<br>materno:'.$materno.'<br>empresa:'.$empresa.'<br>telefono:'.$telefono.'<br>email:'.$email.'<br>curso:'.$curso;
			*/
   			
   			//CREAR OBJETO ASPIRANTE
   			include("class/class_aspirantes_dal.php");
			include("class/class_aspirantes_cursos_dal.php"); 
   			$obj_aspirantes=new aspirantes($rfc,$nombre,$paterno,$materno,$empresa,$telefono,$email);

   			//INSTACIAMOS ASPIRANTES_DAL PARA EJECTAR existe_aspirante($rfc)
   			$metodos_aspirantes=new aspirantes_dal;
			$cuantos=$metodos_aspirantes->existe_aspirante($rfc);

			//INSTACIAMOS ASPIRANTES_CURSOS_DAL PARA EJECTAR existe_aspirante($rfc)
			$metodos_aspirantes_cursos=new aspirantes_cursos_dal;
      		
      		//CREAMOS OBJETO TIPO ASPIRANTE CURSO
      		$obj_aspirantes_cursos=new aspirantes_cursos($rfc,$curso);

      		if ($cuantos==0){//VERIFICA si hay aspirante registrado
      			//insertar al aspirante y insertar al aspirante_curso
      			if($metodos_aspirantes->insertar_aspirante($obj_aspirantes)=="1" and 
        			($metodos_aspirantes_cursos->insertar_aspirante_curso($obj_aspirantes_cursos)=="1")){
      				/*
      				print "Registro de curso recibido correctamente. Gracias por completar estos datos que serán tomados en cuenta para contactarte.";*/
					print '<script>';
					print 'Swal.fire({
                          title: "Registro a cursos",
                          text: "¡Aspirante y Curso Ingresado Correctamente!",
                          type: "success"
                          }).then(function() {
                            window.location = "aspirantes.php";
                          });';
					print '</script>';
      			}
	      		else{
	      			print "Ocurrió un error al tratar de guardar su registro. Dicha registro no se guardó en nuestra Base de datos, vuelva a intentar";
      			}
      		}else{
      			//insertar al aspirante_curso 
       			$metodos_aspirantes_cursos=new aspirantes_cursos_dal;
        		$cuantos_cursos=$metodos_aspirantes_cursos->existeRfcCurso($rfc,$curso);
        		if ($cuantos_cursos>0){
					//print "curso ya estaba registrado ggg";
					print '<script>';
					print 'Swal.fire({
                        	title: "Ya esta Registrado el curso",
                        	text: "¡Aspirante y Curso y han sido registrados previamente, no puede haber duplicados!",
                        	type: "warning"
                        	}).then(function() {
                          		window.location = "aspirantes.php";
                        	});';
					print '</script>';

        		}
        		else{
        			//ya se inserta
        			if($metodos_aspirantes_cursos->insertar_aspirante_curso($obj_aspirantes_cursos)=="1"){

        				//print "Curso recibido correctamente. Gracias por completar estos datos que serán tomados en cuenta para contactarte.";
						print '<script>';
						print 'Swal.fire({
                          title: "Registro de curso",
                          text: "Curso fue registrado correctamente",
                          type: "success"
                          }).then(function() {
                            window.location = "aspirantes.php";
                          });';
						print '</script>';                

        			}else{
        				print "Ocurrió un error al tratar de guardar su curso. Dicho registro no se guardó en nuestra Base de datos, vuelva a intentar";
        			}

        		}

      		}

   		}
   		else{
			echo '<ul style="color: #f00;font-size:25px;">';
      		foreach ($errores as $error):
         	echo '<li>'.$error.'</li>';
      		endforeach;
   			echo '</ul>';
  		}
	}
	else{
		echo 'No se recibieron datos por el metodo post, vuelva a intentar';
	}    	

}//cuando hay post, cliek en el guardar
?>	