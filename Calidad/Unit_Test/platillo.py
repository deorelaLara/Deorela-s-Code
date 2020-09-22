class Ingrediente:
    def __init__(self, nombre, UdM, kalXunidad):
        self.nombre = nombre
        self.UdM = UdM
        self.kalXunidad = kalXunidad

class Platillo:
    def __init__(self):
        self.ingredientes = list()
    
    def addIngrediente(self, ingrediente, cantidad):
        self.ingredientes.append({'ingrediente': ingrediente, 'cantidad': cantidad})