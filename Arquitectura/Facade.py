class Computadora(object):
    def __init__(self, **args):
        self.procesador = args.get('procesador')
        self.memoria = args.get('memoria')
        self.tarjeta_video = args.get('tarjeta_video')

        #GET & SET
    def set_procesador(self, procesador):
        self.procesador = procesador
    def get_procesador(self):
        return self.procesador
    def set_memoria(self, memoria):
        self.memoria = memoria
    def get_memoria(self):
        return self.memoria
    def set_tarjeta_video(self, tarjeta_video):
        self.tarjeta_video = tarjeta_video
    def get_tarjeta_video(self):
        return self.tarjeta_video

    def __str__(self):
        return f'#### Mi Compu #### \n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Tarjeta de Video: {self.tarjeta_video}'

    def obtener_energia(self):
        return f'Ya tengo el poder para mi procesador {self.procesador} >:D'
    def hacer_sonidito(self):
        return 'Pi pi pi pi psssssss'
    def iniciar_Sistema(self):
        return f'Pero tengo windows y mi {self.memoria} no la arma :(!'
    def carga_pantalla(self):
        return f'Windows v1000 con graficos {self.tarjeta_video}'
    def cierra_apps(self):
        return 'Cerrando apps ...'
    def cierra_sesion(self):
        return 'Usuario pepito ha abandonado!'
    def deten_componentes(self):
        return f'Apagando procesador: {self.procesador}\n Memoria: {self.memoria}\n Tarjeta de Video: {self.tarjeta_video}'
    def apagate(self):
        return 'estoy apagado'


#computadora = Computadora(procesador='Intel i7 ', memoria = '128SSD', tarjeta_video='Nvidia GEFORCE GTX')
#print(computadora)

class ComputerFacade(object):
    def __init__(self):
        self._pc = Computadora(procesador='Intel i7 ', memoria = '128SSD', tarjeta_video='Nvidia GEFORCE GTX')
    
    def prender_compu(self):
        print(self._pc.obtener_energia())
        print(self._pc.hacer_sonidito())
        print(self._pc.carga_pantalla())
        print(self._pc.iniciar_Sistema())
    def apagar_compu(self):
        print(self._pc.cierra_apps())
        print(self._pc.cierra_sesion())
        print(self._pc.deten_componentes())
        print(self._pc.apagate())

def main():
	facade = ComputerFacade()
	facade.prender_compu()
	facade.apagar_compu()


if __name__ == "__main__":
    main()