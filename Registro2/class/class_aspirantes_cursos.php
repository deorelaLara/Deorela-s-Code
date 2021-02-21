<?php
if(class_exists('class_aspirantes_cursos') != true){

	class aspirantes_cursos{
		//variables de instancia
		protected $RFC;
		protected $ID_CURSO;

		public function __construct($rfc=NULL,$id_curso=NULL)
  		{
		   $this->RFC=$rfc;
		   $this->ID_CURSO=$id_curso;
  		}

	public function getRFC(){return $this->RFC;}
	public function setRFC($rfc){$this->RFC=$rfc;}

	public function getID_CURSO(){return $this->ID_CURSO;}
	public function setID_CURSO($id_curso){$this->ID_CURSO=$id_curso;}

	}//end class
}//end class exists
?>