'''
    #######################################################
    ############# Metodo Runge Kutta  #####################
    ######################################################


    Integrantes :
        - Alvarado Lara Luz Deorela Sabas
        - Flores Reyna Jose Jovany 
        - Bucio Montes Hector Daniel

'''


import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    #return 10 * np.exp(0.8 *x) - 1.5 * y
    return x ** 3 -2 * y

def rk4(f, a, b, y0, h ):
    x = np.arange(a, b+h, h)
    n = len(x)
    y = np.zeros(n)
    y[0] = y0
    
    for j in range(0, n-1):
        k1 = f(x[j], y[j])
        k2 = f(x[j] + h/2, y[j] + k1 * h/2)
        k3 = f(x[j] + h/2, y[j] + k2 * h/2)
        k4 = f(x[j] + h, y[j] + k3 *h)
        y[j+1] = y[j] + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    plt.plot(x, y)
    plt.grid()
    plt.show()

print(rk4(f, 0, 5, 1, 0.01))