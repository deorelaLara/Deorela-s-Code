<?php
include("class/class_aspirantes_dal.php");
if(isset($_POST['rfc'])){

   $rfc=  $_POST['rfc'];
   //echo $rfc;
      $output='';      
      $metodos_aspirantes=new aspirantes_dal;

      $busca_aspirantes=$metodos_aspirantes->existe_aspirante($rfc);
      if ($busca_aspirantes==0){
        echo 0;
        exit;
      }

      
      $result_aspirantes=$metodos_aspirantes->datos_por_rfc($rfc);

        $arreglo=array(
        "nombrex"=>$result_aspirantes->getNombre(),
        "paternox"=>$result_aspirantes->getPaterno(),
        "maternox"=>$result_aspirantes->getMaterno(),
        "empresax"=>$result_aspirantes->getEmpresa(),
        "telefonox"=>$result_aspirantes->getTelefono(),
        "emailx"=>$result_aspirantes->getEmail()
        );

      $arreglo = array_map('utf8_encode',$arreglo);
      echo json_encode($arreglo,JSON_UNESCAPED_UNICODE);
}
else{
  echo "no llego correctamente el id, error backend,ver id de egreso en modal";
  exit;  
}
?>