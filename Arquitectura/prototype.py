import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attr)
        return obj


class Oveja(object):

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def setNombre(self, nombre):
        self.nombre

    def getNombre(self):
        return self.nombre

    def setTipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def __str__(self):
        return f'Nombre: {self.nombre}\nTipo: {self.tipo}'


prototype = Prototype()
oveja = Oveja('Dolly', 'Dorper')

prototype.register_object('Dolly', oveja)
ove = prototype.clone('Dolly',nombre='Garry', tipo='Suffolk')

print(oveja)
print('-----')
print(ove)
