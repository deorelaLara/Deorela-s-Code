'''
    #######################################################
    ############# Metodo Simpson's 1/3 ###################
    ######################################################


    Integrantes :
        - Alvarado Lara Luz Deorela Sabas
        - Flores Reyna Jose Jovany 
        - Bucio Montes Hector Daniel

'''
#Hallar el area bajo la curva de f(X)= e^x Sin(x) entre x = 0 y x = 3.1416
import numpy as np
import matplotlib.pyplot as plt

#Definimos nuestra funcion f(x)
def f(x):
    return np.exp(x) * np.sin(x)

#Graficamos nuestra funcion
x = np.linspace(0, np.pi, 101)
plt.plot(x, f(x))
plt.grid()
plt.show()

#Definimos nuestra funcion simpson13 a la cual le pasamos como parametros 
# la funcion f, el limite inferior a y el limite superior b
def simpson13(f, a, b):
    m = (a + b) / 2
    integral = (b - a)/6 *(f(a) + 4 * f(m) + f(b))
    return integral

a = 0
b = np.pi
#Numero de iteraciones a realizar
n = 5
h = (b - a)/n
suma = 0
#Por cada elemento en n realizamos una iteracion 
for i in range(n):
    b = a + h
    area = simpson13(f, a, b)
    suma = suma + area
    a = b
    print('iter',i ,'=',suma)

#print(suma)
vt = np.exp(np.pi)/2 + 1/2 
errorPorcentual = abs((vt - suma)/vt) * 100
print('Error = ', errorPorcentual)