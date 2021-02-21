var pattern = /^[a-zA-Z]{4}(\d{6})(([a-zA-Z0-9]){3})?$/;
var pattern2 = /^[a-zA-Z]{3,30}?$/;


function valida_forma(){
	var var_rfc = document.getElementById("irfc").value.trim();
	var var_nombre = document.getElementById("inombre").value.trim();
	var var_paterno = document.getElementById("ipaterno").value.trim();
	var var_materno = document.getElementById("imaterno").value.trim();
	var var_empresa = document.getElementById("iempresa").value.trim();
	var var_telefono = document.getElementById("itelefono").value.trim();
	var var_email = document.getElementById("iemail").value.trim();
	var var_cursos = document.getElementById("scurso").value;

	//var var_estatus = document.getElementById("estatus").textContent;
	//alert(var_estatus);

	if (var_rfc.length==0){
		alert("Error: El campo RFC es obligatorio, verificar");
		return false;
	}
	else if (!pattern.test(rfc)){
		//alert("Error: El RFC esta mal formado, verificar");

		Swal.fire({
		  icon: 'error',
		  title: 'Error:RFC',
		  text: 'El RFC esta mal formado, verificar!',
		  footer: 'Verificar por favor'
		});

		return false;
	}

	else if (var_nombre.length==0){
		alert("Error: El campo nombre es obligatorio, verificar");
		return false;
	}
	else if (!pattern2.test(var_nombre)){
		alert("Error: El nombre no permite números, verificar");
		return false;
	}
	else if (var_paterno.length==0){
		alert("Error: El campo paterno es obligatorio, verificar");
		return false;
	}	
	else if (var_materno.length==0){
		alert("Error: El campo materno es obligatorio, verificar");
		return false;
	}	
	else if (var_empresa.length==0){
		alert("Error: El campo empresa es obligatorio, verificar");
		return false;
	}
	else if (var_telefono.length==0){
		alert("Error: El campo telefono es obligatorio, verificar");
		return false;
	}
	else if (var_email.length==0){
		alert("Error: El campo email es obligatorio, verificar");
		return false;
	}
	else if (var_cursos=="0"){
		//alert("Error: El campo cursos es obligatorio, verificar");
		Swal.fire({
		  icon: 'error',
		  title: 'Error:Cursos',
		  text: 'El campo cursos es obligatorio!',
		  footer: 'Verificar por favor'
		});
		return false;
	}	
	

}

function validaRFC(){
   //pattern = /^[a-zA-Z]{4}(\d{6})(([a-zA-Z0-9]){3})?$/;
   rfc = document.getElementById("irfc").value;
  document.getElementById("estatus").innerHTML = pattern.test(rfc);
  return pattern.test(rfc);
}

function validaRFC2(){
   //alert("hola");
   
   //pattern = /^[a-zA-Z]{4}(\d{6})(([a-zA-Z0-9]){3})?$/;
	rfc = document.getElementById("irfc").value;
   	document.getElementById("estatus").innerHTML = (pattern.test(rfc)) ? "Formato OK" : "Hay errores de formato";
   	return pattern.test(rfc);
}

function valida_nombre_full(valnom,ctl){
	//valnom= document.getElementById("inombre").value;
	if (ctl=='n'){
			document.getElementById("estatus_nom").innerHTML = (pattern2.test(valnom)) ? "OK" : "Errors_nom";
		}
	else if (ctl=='p'){
			document.getElementById("estatus_pat").innerHTML = (pattern2.test(valnom)) ? "OK" : "Errors_pat";
		}
	else if (ctl=='m'){
			document.getElementById("estatus_mat").innerHTML = (pattern2.test(valnom)) ? "OK" : "Errors_mat";
		}
}

function IsEmail(email) {
  var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  if(!regex.test(email)) {
    return false;
  }else{
    return true;
  }
}
/*relizar un funcion reutilizable, para nombre, paterno y materno*/