import numpy as np
import matplotlib.pyplot as plt

#FUNCION F(X)
def f(x):
    #nos retorna esta funcion para cualquier valor x que se ingrese 
    #return x **3 - np.cos(x) 
    return x ** 2 - 3*x -4

#Almacenamos la derivada de f(x) en la siguiente funcion 
def dFdx(x):
    return 2 * x -3
    #return 3 * x **2 + np.sin(x)
"""
########## Metodo de Newton Raphson ##########
"""
x0 = 8
error = 10
i = 1
while error > 1e-10: #6 cifras decimales 
    x1 = x0 - f(x0) / dFdx(x0)
    error = (x1 - x0)/x1 * 100 #calcula la diferencia error 
    x0 = x1
    print('Iteracion:', i,'---', 'Raiz Aprox:', x0, '---','error: ', error)
    i += 1
    
#Imprimimos el valor de x0 que toma la ultima iteracion 
# y este es el mas cercano a la raiz    
#print(x0)

"""
########### GRAFICAMOS LA FUNCION ORIGINAL ############
"""
x = np.linspace(-2, 2, 100) #le damos a x un valor entre -5 y 5 tomando 100 valores
plt.plot(x,f(x)) #Pedimos que nos dibuje la funcion que tenemos
plt.plot(x0, f(x0), 'or')
plt.grid()
plt.show()





"""
    Metodo de newton con ciclo for
    x0 = 1
for i in range(0,5):
    x1 = x0 - f(x0)/dFdx(x0)
    x0 = x1 
    print('Iteracion:', i,'---', 'Raiz Aprox:', x0)
    #print(i, x0)
"""