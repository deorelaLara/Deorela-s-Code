import math
import sympy as sy
import numpy as np 
from sympy.functions import sin, cos

def Taylor(f, xi, x0, es):
    fx = sy.Symbol(f)
    tval = fx.subs(fx, x0)
    h = x0 - xi
    sAnterior = fx.subs(fx, xi)
    
    et = 100
    j = 1
    while et >= es:
        der = f.diff(fx, j)
        evDer = f.subs(der, xi)
        sol = sAnterior + (evDer*h**j/math.factorial(j))
        et = abs(tval-sol)/(tval)*100
        sAnterior = sol
        Orden = j
        j += j
        
        
print(Taylor('-0.1x^4 - 0.15x^3', 0, 1, 0.01))
        
        

        
        
    