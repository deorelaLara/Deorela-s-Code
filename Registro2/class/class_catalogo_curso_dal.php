<?php
include('class_catalogo_curso.php');
include('class_db.php');
	class catalogo_cursos_dal extends class_db{

		function __construct(){
			parent::__construct();
		}

		function __destruct(){
			parent::__destruct();
		}


		function datos_por_id($id){
			$rfc=$this->db_conn->real_escape_string($id);
			$sql="select * from catalogo_curso where id_curso='$id'";
			$this->set_sql($sql);
			$result=mysqli_query($this->db_conn,$this->db_query) or die (mysqli_error($this->db_conn));
			$total_cursos=mysqli_num_rows($result);
			$obj_det=null;

			if ($total_cursos==1){
				$renglon=mysqli_fetch_assoc($result);
				$obj_det=new catalogo_curso($renglon["ID_CURSO"],$renglon["NOMBRE_CURSO"],$renglon["FECHA"]);

			}
			return $obj_det;
		}//end datos_por_id

	
		function obtener_lista_cursos(){
			$sql="select * from catalogo_curso";
			$this->set_sql($sql);
			$rs=mysqli_query($this->db_conn,$this->db_query) or die (mysqli_error($this->db_conn));
			$total_cursos=mysqli_num_rows($rs);
			$obj_det=null;

			if ($total_cursos>0){
				$i=0;
				while ($renglon = mysqli_fetch_assoc($rs)){
					$obj_det=new catalogo_curso(
							$renglon["ID_CURSO"],
							utf8_encode($renglon["NOMBRE_CURSO"]),
							$renglon["FECHA"]
						);

					$i++;
					$lista[$i]=$obj_det;
					unset($obj_det);


				}//end while	
					return $lista;
			}//end if	
		}//end function	


		function existe_curso($id){
			$id=$this->db_conn->real_escape_string($id);
			$sql = "select count(*) from catalogo_curso";
			$sql.=" where id_curso='$id'";

			$this->set_sql($sql);
			$rs=mysqli_query($this->db_conn,$this->db_query) or die (mysqli_error($this->db_conn));

			$renglon=mysqli_fetch_array($rs);
			$cuantos=$renglon[0];

			return $cuantos;	
		}


		function insertar_curso($obj){
			
			$fecha=date("Y-m-d H:i:s");
			$sql="insert into catalogo_curso(";
			$sql.="NOMBRE_CURSO,";
			$sql.="FECHA)";			
			$sql.=" values (";
			$sql.="'".$obj->getNOMBRECURSO()."',";
			$sql.="'".$fecha."'";
			$sql.=")";
			//echo $sql;
			$this->set_sql($sql);
			$this->db_conn->set_charset("utf8");
			mysqli_query($this->db_conn,$this->db_query) or die (mysqli_error($this->db_conn));
			if(mysqli_affected_rows($this->db_conn)==1){
				$insertado=1;
			}
			else{
				$insertado=0;
			}

			unset($obj);
        	return $insertado;
		}//end function	


		function borra_curso($obj){
			$id=$this->db_conn->real_escape_string($obj->getIDCURSO());
			$sql="delete from catalogo_curso where ID_CURSO=".$obj->getIDCURSO();
			//echo $sql;return;
			$this->set_sql($sql);
			mysqli_query($this->db_conn,$this->db_query) or die (mysqli_error($this->db_conn));
				if(mysqli_affected_rows($this->db_conn)==1){
					$borrado=1;
				}
				else{
					$borrado=0;
				}

				unset($obj);
        		return $borrado;

		}


		function actualiza_curso($obj){
/*
        echo '<pre>';
        echo print_r($obj);
        echo '</pre>';exit;
*/
        $sql = "update catalogo_curso set ";
        $sql .= "NOMBRE_CURSO="."'".$obj->getNOMBRECURSO()."'";
        $sql .= " where ID_CURSO = '".$obj->getIDCURSO()."'";

        //echo $sql;exit;
        $this->set_sql($sql);
        $this->db_conn->set_charset("utf8");
        
        mysqli_query($this->db_conn,$this->db_query) or die(mysqli_error($this->db_conn));

        if(mysqli_affected_rows($this->db_conn)==1) {
            $actualizado=1;
        }else{
            $actualizado=0;
        }
        unset($obj);
        return $actualizado;
    }

	}// end class
?>