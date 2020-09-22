import math
"""
Crear un programa que te pida un numero entero positivo
y lo eleve a su misma potencia, cuando el numero es par lo resta 
cuando es numero impar lo suma.
"""
while(True):
    resultado =0
    n = int(input("Ingresa un numero entero positivo: "))
    if n > 0:
        for i in range(n):
            i+=1
            if i % 2 == 0:
                resultado-=i**i
            else:
                resultado+=i**i
        print("El resultado es: " + str(resultado))
        break
    else:
        print("error ... Ingresa un numero valido")