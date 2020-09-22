"""
NOMBRE: ALVARADO LARA LUZ DEORELA SABAS
"""
import random

def del0to10():
    return int(random.random()*11)

class MatrizLoca():
    def __init__(self):
        self.matriz = []
        for y in range(0,10):
            self.matriz.append([])
            for x in range(0,5):
                self.matriz[y].append(del0to10())

    def __str__(self):
        returnString = ''
        for y in range(0,10):
            returnString += '\t'.join(str(x) for x in self.matriz[y])
            returnString += '\n'
        return returnString

def busqueda(keyword):
    matriz = MatrizLoca()
    print(matriz)
    contador = 0
    vocales = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
    for letra in keyword:
        if letra in 'aeiou':
            if matriz.matriz[contador][vocales[letra]] == 10:
                return 'Hay un 10 en la fila {}, columna {}.'.format(contador+1, letra)
            else:
                linea = matriz.matriz[contador][vocales[letra]]
    return 'No hay más carácteres para buscar vocales.'

def main():
    print(busqueda(input('Escribe algo aquí: ')))

if __name__ == '__main__':
    main()