"""
        CLASES Y OBJETOS

    def __init__(self, nombre, tipo, descripcion):

    def __init__(self, *args):
    print(args)
    sys.exit(0)
"""
import sys
class Organizacion(object):
    """docstring for organizacion"""
    def __init__(self, **args):
        #print(args)
        #sys.exit(0)
        self.nombre=args.get('nombre')
        #self.nombre = args['nombre']
        self.tipo = args['tipo']
        self.descripcion = args['descripcion']

    def set_nombre(self, nombre):
        self.nombre=nombre
    def get_nombre(self):
        return self.nombre
    def set_tipo(self, tipo):
        self.tipo=tipo
    def get_tipo(self):
        return self.tipo
    def set_descripcion(self, descripcion):
        self.descripcion=descripcion
    def get_descripcion(self):
        return self.descripcion
    #protected
    def __ubicacion(self):
        return 'Tangamandapio'


    def __str__(self):
        return f'Nombre: {self.nombre}\nTipo: {self.tipo}\nDescripcion:{self.descripcion}'

#MANDAMOS LLAMAR LA CLASE
"""
_ --> Protected
__ --> Private 
"""
org= Organizacion(nombre='Deorela',tipo='O+',descripcion='Tipo de sangre')
#org.set_tipo('global')
print(org)
