#VARIABLES PARA INGRESAR DATOS
m = int(input("Ingresa un numero (m): "))
n = int(input("Ingresa un numero (n): "))

#FUNCION CON LISTA COMPRIMIDA
def potencias(n, m):
    potencia = [n ** i for i in range(0, m)]
    return potencia
print(potencias(n,m))

#FUNCION CON CICLO FOR
def potenciasFor(n, m):
    potencia=[]
    for x in range(m):
        potencia.append(n ** x)
    return potencia
print(potenciasFor(n, m))

def pot():
    for i in range(m):
        print((n ** i))

pot()