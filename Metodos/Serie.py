import math
while(True):
    resultado=1
    n= int(input("Ingresa un numero entero positivo: "))
    if n > 0:
        for i in range(n):
            i += 1
            #print(i)
            if i % 2 == 0:
                resultado = resultado/(1/i)
            else:
                resultado = resultado * (1/i)
        print("El resultado es: " + str(resultado))
        break
    else:
        print("*Error ingresa un numero valido")