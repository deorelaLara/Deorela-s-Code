<?php
	if (class_exists('aspirantes')!=true){
		class aspirantes{
			protected $RFC;
			protected $NOMBRE;
			protected $PATERNO;
			protected $MATERNO;
			protected $EMPRESA;
			protected $TELEFONO;
			protected $EMAIL;
			protected $FECHA_REGISTRO;



		public function __construct(
			 $RFC=NULL,
			 $NOMBRE=NULL,
			 $PATERNO=NULL,
			 $MATERNO=NULL,
			 $EMPRESA=NULL,
			 $TELEFONO=NULL,
			 $EMAIL=NULL,
			 $FECHA_REGISTRO=NULL			
			){
					$this->RFC=$RFC;
					$this->NOMBRE=$NOMBRE;
					$this->PATERNO=$PATERNO;
					$this->MATERNO=$MATERNO;
					$this->EMPRESA=$EMPRESA;
					$this->TELEFONO=$TELEFONO;
					$this->EMAIL=$EMAIL;
					$this->FECHA_REGISTRO=$FECHA_REGISTRO;							
			}//END CONSTRUCTOR
				

   /**
     * @return mixed
     */
    public function getFECHAREGISTRO()
    {
        return $this->FECHA_REGISTRO;
    }

    /**
     * @param mixed $FECHA_REGISTRO
     *
     * @return self
     */
    public function setFECHAREGISTRO($FECHA_REGISTRO)
    {
        $this->FECHA_REGISTRO = $FECHA_REGISTRO;

        return $this;
    }

    /**
     * @return mixed
     */
    public function getRFC()
    {
        return $this->RFC;
    }

    /**
     * @param mixed $RFC
     *
     * @return self
     */
    public function setRFC($RFC)
    {
        $this->RFC = $RFC;

        return $this;
    }

    /**
     * @return mixed
     */
    public function getNOMBRE()
    {
        return $this->NOMBRE;
    }

    /**
     * @param mixed $NOMBRE
     *
     * @return self
     */
    public function setNOMBRE($NOMBRE)
    {
        $this->NOMBRE = $NOMBRE;

        return $this;
    }

    /**
     * @return mixed
     */
    public function getPATERNO()
    {
        return $this->PATERNO;
    }

    /**
     * @param mixed $PATERNO
     *
     * @return self
     */
    public function setPATERNO($PATERNO)
    {
        $this->PATERNO = $PATERNO;

        return $this;
    }

    /**
     * @return mixed
     */
    public function getMATERNO()
    {
        return $this->MATERNO;
    }

    /**
     * @param mixed $MATERNO
     *
     * @return self
     */
    public function setMATERNO($MATERNO)
    {
        $this->MATERNO = $MATERNO;

        return $this;
    }

    /**
     * @return mixed
     */
    public function getEMPRESA()
    {
        return $this->EMPRESA;
    }

    /**
     * @param mixed $EMPRESA
     *
     * @return self
     */
    public function setEMPRESA($EMPRESA)
    {
        $this->EMPRESA = $EMPRESA;

        return $this;
    }

    /**
     * @return mixed
     */
    public function getTELEFONO()
    {
        return $this->TELEFONO;
    }

    /**
     * @param mixed $TELEFONO
     *
     * @return self
     */
    public function setTELEFONO($TELEFONO)
    {
        $this->TELEFONO = $TELEFONO;

        return $this;
    }

    /**
     * @return mixed
     */
    public function getEMAIL()
    {
        return $this->EMAIL;
    }

    /**
     * @param mixed $EMAIL
     *
     * @return self
     */
    public function setEMAIL($EMAIL)
    {
        $this->EMAIL = $EMAIL;

        return $this;
    }

	}//end class
}//end exists
?>