import numpy as np

#DECLARAR MATRIZ
m = int(input('Valor de m: ')) #Renglones = m
n = int(input('Valor de n: ')) #Columnas = n
matrix = np.zeros((m, n))
x = np.zeros((m))

vector = np.zeros((n))
comp = np.zeros((m))
error = []

print('Metodo de Gauss-Seidel')
print('Introduce la matriz de coeficientes y el vector solucion')

for r in range(0, m):
    for c in range(0, n):
        matrix[(r),(c)] = float (input('Elemento a['+str(r + 1)+ str(c+1) + ']'))
    vector[(r)] = float(input('b[' + str(r+1)+ ']:' ))
tol = float(input('Cual es la tolerancia que deseas: '))
iter = int(input('Numero maximo de iteraciones: '))

#METODO DE GAUSS SEIDEL 
k = 0 
while k < iter:
    suma = 0
    k += 1
    for r in range(0, m):
        suma = 0
        for c in range (0, m):
            if (c != r):
                suma = suma + matrix[r, c]*x[c]
                x[r] = (vector[r] - suma)/matrix[r, r]
                print('x[' + str(r) + ']: ' + str(x[r]))
    del error[:] 
    
    #Comprobación 
    for r in range(0, m):
        suma = 0
        for c in range (0, m):
            suma = suma + matrix[r, c]*x[c]
        comp[r] = suma
        dif = abs(comp[r] - vector[r])
        error.append(dif)
        print('Error en x[', r, ']= ', error[r])
    #Numero de iteraciones 
    print('Iteraciones: ', k)
    if all(i < tol for i in error) == True:
        break

print('Fin!') 
            