"""
    Metodo de ordenamiento Burbuja
    Revisa cada elemento de la lista con el siguiente elemento, intercambia
    de posicion si estan en el orden equivocado 

    Ejemplo

    4 2 6 8 5 7 
    2 4 6 8 5 7
    2 4 6 5 8 7
    2 4 6 5 7 8 
    2 4 5 6 7 8  

"""

list = [4, 2, 6, 8, 5, 7]

for i in range(len(list)):
    #recorre cada elemento de la lista para comparar
    for x in range(len(list)-1):
        #comparamos el elemento actual contra el siguiente para verificar si es mayor 
        if list[x] > list[x+1]:
            #intercambiamos valores
            aux = list[x] # indice 0 --- elemento [4]
            list[x] = list[x+1]
            list[x+1] = aux
            print(list)