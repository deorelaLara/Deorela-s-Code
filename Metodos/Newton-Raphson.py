


def func(x):
    # x^3 - x^2 + 2
    return x ** 3 - x ** 2 + 2

def derivada(x):
    #3x^2 - 2x
    return 3 * x**2 - 2 * x

#FUNCION PARA ENCONTRAR LA RAIZ 
def NewtonRaphson(x):
    h = func(x)/ derivada(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivada(x)
        #x(x+1) = x(i) - f(x)/ f'(x)
        x = x -h
        
    print('The value of the root is ', '%.4f'%x)
    
    
x0 =458
NewtonRaphson(x0)