<?php
	if (class_exists('catalogo_curso')!=true){
		class catalogo_curso{
			protected $ID_CURSO;
			protected $NOMBRE_CURSO;
			protected $FECHA_ALTA;

			public function __construct($id_curso=NULL,$nombre_curso=NULL,$fecha_alta=NULL){
				$this->ID_CURSO=$id_curso;
				$this->NOMBRE_CURSO=$nombre_curso;
				$this->FECHA_ALTA=$fecha_alta;
			}

			/*GETTERS Y SETTERS*/


	


     function getIDCURSO()
    {
        return $this->ID_CURSO;
    }

    
   function setIDCURSO($id_curso)
    {
        $this->ID_CURSO = $id_curso;
    }

    
     function getNOMBRECURSO()
    {
        return $this->NOMBRE_CURSO;
    }

    
     function setNOMBRECURSO($nombre_curso)
    {
        $this->NOMBRE_CURSO = $nombre_curso;
    }

    
     function getFECHAALTA()
    {
        return $this->FECHA_ALTA;
    }

    
    function setFECHAALTA($fecha_alta)
    {
        $this->FECHA_ALTA = $fecha_alta;
    }


	}//end class
}//end redefinition

?>