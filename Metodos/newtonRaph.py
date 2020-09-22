import numpy as np
import matplotlib.pyplot as plt

#FUNCION F(X) DADA POR EL USUARIO 
def f(x):
    return x ** 2 - 3*x -4
    #return x **3 - np.cos(x)
    #return x **2 -2
#DERIVADA DE LA FUNCION
def dFdx(x):
    return 2 * x -3
    #return 3 * x **2 + np.sin(x)
    #return 2 *x 

####################GRAFICA FUNCION ORIGINAL #######################
x = np.linspace(-9, 9, 200) #Intervalo de las raices de -2 a 2 
plt.figure(num='Newton Raphson')#Nombre de cada grafica
plt.plot(x, f(x))
plt.grid('on') #---> Cuadricula 
plt.show() # Nos devuelve la funcion original y la funcion derivada en una grafica 

########### METODO NEWTON RAPHSON ################
rootValues = [8] #valor inicial --- > X0
error = 0.001 
rootGuess = rootValues[-1] # aproximacion actual
i = 1
while True:
    #print(rootGuess,f(rootGuess))
    droot = -1 * f(rootGuess) / dFdx(rootGuess) #valor aproximado
    #error  =  rootGuess - rootValues[-1]/ rootGuess * 100 
    rootGuess = rootGuess + droot
    rootValues.append(rootGuess)
    print('Iter:', i,'  --  ','x: ',rootGuess, '  --  ','F(x): ', f(rootGuess))
    i +=1

    if abs(rootValues[-2] - rootValues[-1]) < error: 
        break
    
######## GRAFICANDO LA APRXIMACION #################
rootValues = np.array(rootValues)
x = np.linspace(0,8,200) #Intervalo de numeros en x de 0 a 5
plt.figure(num="Newton Raphson")
#plt.clf()
plt.plot(x, f(x))
plt.plot(rootValues, f(rootValues), 'or', ms=7)
plt.grid('on')
plt.show()