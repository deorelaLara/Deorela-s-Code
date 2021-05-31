<?php

$temperatura=$_POST['temperatura'];//POST PARA MICRO
$humedad=$_POST['humedad'];//GET para internet
$id=$_POST['id'];
$distancia=$_POST['distancia'];
$con=mysqli_connect('localhost','root','');

if(!$con){
	echo'sin conexion';
	}

if(!mysqli_select_db($con,'sensores'))
  {
	  echo'no se encontro la base de datos';
	}
   $result = mysqli_query($con, "SELECT `id` FROM `dht11` WHERE id=$id");
   $row_cnt=mysqli_num_rows($result);
   if($row_cnt>0){
	   mysqli_query($con, "UPDATE `dht11` SET `temperatura`=$temperatura,`humedad`=$humedad,`distancia`=$distancia  WHERE id=$id");
	   echo'datos actualizados';
   }
   else{
	 $sql="INSERT INTO dht11 (`id`, `temperatura`, `humedad`,`distancia`) VALUES ('$id','$temperatura','$humedad','$distancia')";
	 if(!mysqli_query($con,$sql)){echo'   datos no insertados';
	    }
	  else{echo '   datos insertados';}
	}
?>
