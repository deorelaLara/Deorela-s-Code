<?php include("class/class_catalogo_curso_dal.php"); ?>
<!DOCTYPE html>
<html>
<head>
	<?php include_once "inclusiones/meta_tags.php"; ?>
	<title>Registro de Aspirantes</title>
	<?php include_once "inclusiones/css_y_favicon.php"; ?>
	<link rel="stylesheet" type="text/css" href="css/styles.css">
</head>
<body>

<!--menu principal-->
<div class="container-fluid">
	<div class="row">
	<?php
		include_once "inclusiones/menu_horizontal_superior.php"
	?>
	</div>
</div>



<div class="container" style="margin-top: 60px;">

<h2>Ingrese sus datos para el pre-registro a los cursos</h2>
<p>Completar los datos requeridos, esta pantalla esta adaptada para operar en dispositivos móviles</p>


	<form action="inserta_aspirante.php" method="post" accept-charset="utf-8" onsubmit="return valida_forma();">
	<div class="row">
		<div class="col-25">
			<label for="lrfc">R.F.C</label>
			<label id="estatus"></label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="irfc" id="irfc" maxlength="13" size="20"  placeholder="Ingrese su RFC" required onkeyup="validaRFC2();" oninvalid="this.setCustomValidity('Ingrese su RFC')"
 oninput="setCustomValidity('')" >
		</div>
		</div>
	


	<div class="row">	
		<div class="col-25">	
			<label for="lnom">Nombre</label>
			<label id="estatus_nom"></label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="inombre" id="inombre" maxlength="30" size="40"  placeholder="Ingrese su Nombre" required oninvalid="this.setCustomValidity('Nombre no puede ir vacío')"
 oninput="setCustomValidity('')" onkeyup="valida_nombre_full(document.getElementById('inombre').value,'n');" >
		</div>
	</div>

	<div class="row">
		<div class="col-25">	
			<label for="lpat">Paterno</label>
			<label id="estatus_pat"></label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="ipaterno" id="ipaterno" maxlength="30" size="40"  placeholder="Ingrese su Apellido Paterno" required oninvalid="this.setCustomValidity('Paterno es obligatorio')"
 oninput="setCustomValidity('')" onkeyup="valida_nombre_full(document.getElementById('ipaterno').value,'p');" >
		</div>
	</div>


	<div class="row">
		<div class="col-25">
			<label for="lmat">Materno</label>
			<label id="estatus_mat"></label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="imaterno" id="imaterno" maxlength="30" size="40"  placeholder="Ingrese su Apellido Materno" required="true" onkeyup="valida_nombre_full(document.getElementById('imaterno').value,'m');">
		</div>
	</div>	

	<div class="row">
		<div class="col-25">	
			<label for="lemp">Empresa</label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="iempresa" id="iempresa" maxlength="30" size="40"  placeholder="Ingrese su el nombre de su empresa" required oninvalid="this.setCustomValidity('Rellene el campo de empresa')"
 oninput="setCustomValidity('')">
		</div>
	</div>

	<div class="row">
		<div class="col-25">
			<label for="ltel">Teléfono</label>
		</div>
		<div class="col-75">
			<input type="tel" pattern="[0-9]{10}" name="itelefono" id="itelefono" maxlength="10" size="15"  placeholder="Ingrese su el telefono a 10 dígitos" required oninvalid="this.setCustomValidity('Debe llenar un número telefónico')"
 oninput="setCustomValidity('')">
		</div>
	</div>

	<div class="row">
		<div class="col-25">
			<label for="lmail">Email</label>
		</div>
		<div class="col-75">
			<input type="email" name="iemail" id="iemail" maxlength="60" size="80"  placeholder="Ingrese su corro electrónico" required oninvalid="this.setCustomValidity('Llene el campo correo electrónico')"
 oninput="setCustomValidity('')">
		</div>
	</div>

	<div class="row">

<?php
$obj_lista_cursos=new catalogo_cursos_dal;
$lista_cursos=$obj_lista_cursos->obtener_lista_cursos();
/*
echo '<pre>';
print_r($lista_cursos);
echo '</pre>';
return;
*/
if ($lista_cursos==NULL){
	print "<section><h2>no se encontraron resultados de cursos</h2></section>";
}
else{
?>


		<div class="col-25">
			<label for="lcur">Cursos disponibles</label>
		</div>
		<div class="col-75">
			<select name="scurso" id="scurso" required oninvalid="this.setCustomValidity('Seleccione un curso')"
 oninput="setCustomValidity('')">
		<option value="0">Seleccione</option>
				
<?php 
foreach ($lista_cursos as $key => $value) {
?>
		<option value="<?=$value->getIDCURSO(); ?>"><?=utf8_encode($value->getNOMBRECURSO()); ?></option>


<?php } ?>

			</select>
		</div>
<?php } ?>
	</div>

	<div class="row2">
	<div class="boton">
		<input type="submit" name="btn_registro" value="Registrar">
	</div>
	</div>
	</form>	

</div><!-- cierre container -->

<?php include_once "inclusiones/js_incluidos.php"; ?>
<script src="js/mis_funciones.js" type="text/javascript"></script>

</body>
</html>

<script type="text/javascript">
$(document).ready(function() {

	$("#irfc").blur(function() {
		var rfc=$('#irfc').val();

		$.ajax({
			url:"fetch_aspirante.php",
			method:"POST",
			data:{rfc:rfc},
			dataType:"json",
			success:function(data){
				//alert(JSON.stringify(data));
				if (data!=0){
					$("#inombre").attr('readonly',true);
					$("#ipaterno").attr('readonly',true);
					$("#imaterno").attr('readonly',true);
					$("#iempresa").attr('readonly',true);
					$("#itelefono").attr('readonly',true);
					$("#iemail").attr('readonly',true);

					$('#inombre').val(data.nombrex);
					$('#ipaterno').val(data.paternox);
					$('#imaterno').val(data.maternox);
					$('#iempresa').val(data.empresax);
					$('#itelefono').val(data.telefonox);
					$('#iemail').val(data.emailx);																														
				}
			},
			error:function(request,status,error){
				var val=request.responseText;
				alert("Error:"+val);
			}

		});//end ajax
	});//end blur
	
});//end ready function	

</script>