"""
PROGRAMA QUE LEE UNA LISTA DE NUMEROS Y LOS
CLASIFICA EN POSITIVOS, NEGATIVOS, PARES E IMPARES
"""

#FUNCION PARA CLASIFICAR LOS NUMEROS
def clasificacion(lista_numeros):
    positivos = negativos = pares = impares =0 #inicializamos variables
    list = lista_numeros.split()   #Separa cada elemento del string
    
    for x in list:
        x = int (x)
        if x % 2 == 0:
            pares += 1 #sumamos numeros pares 
        if x % 2 != 0:
            impares += 1 #sumamos numeros impares
        if x > 0:
            positivos += 1 #sumamos numeros positivos
        if x < 0:
            negativos += 1 #sumamos numeros negativos
    return """
    {} número(s) positivo(s)\n{} número(s) negativo(s)\n{} número(s) par(es)\n{} número(s) impar(es)
    """.format(positivos, negativos, pares, impares).strip()


if __name__ == '__main__':
    input_string = input()
    print(clasificacion(input_string))
    