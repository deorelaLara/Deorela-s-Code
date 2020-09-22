'''def volumenCaja():
    lado = int(input('Ingresa el tamaño del lado de la caja: '))
    print('VOLUMEN CAJA')
    volumen = lado ** 3
    return volumen'''

def ladosCaja (*kwargs):
    for arg in kwargs:
        return arg
    #lado = int(input('Ingrese el tamaño del lado de la caja: '))
    #volumen = lado ** 3
    #return volumen"""

def contLiquido(*argv):
    for arg in argv:
        #orden = int(input)
        #cont = int(input('Cuantos contenedores deseas ingresar? '))
        #lit = int(input('Litros por contenedor: '))
        #litrosTotales = cont * lit
        #volumen = litrosTotales / 1000
        #print('#### ORDEN TOTAL ####')
        #return litrosTotales , volumen
        #print('Orden:' , arg)
        return arg
        

def Total():
   caja = ladosCaja((8), (8))
   liquido = contLiquido((5, 10),(10, 5),(30,1))
   return liquido




#print(ladosCaja())
print(contLiquido())
print(Total())
#print(volumenCaja())