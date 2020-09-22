import math
import sympy as sy
import numpy as np 
from sympy.functions import sin, cos

#POLINOMIO DE TAYLOR DE UNA FUNCION 
#DEFINIMOS NUESTRA VARIABLE SIMBOLICA Y LA FUNCION 
x = sy.Symbol('x')
f = (x**2)

#DEFINIMOS LA FUNCION FACTORIAL
def fac(n):
    if n <= 0:
        return 1
    else:
        return n * math.factorial(n-1)   
#APROXIMACION DE TAYLOR EN X0 DE LA FUNCION f
#x0 = punto o polinomio
def taylor(function, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x, i).subs(x, x0))/(fac(i))*(x-x0)**i
        i += 1
    return print(p)


taylor(f, 2, 1)