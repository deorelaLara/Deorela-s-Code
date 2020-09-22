import numpy as np
#VALOR INICIAL DE LAS VARIABLES
x = 4
y = 2
z = -3
#NUMERO DE ITERACIONES
n = 1

for i in range(n):
    f1 = x**3 + y**3 - z**3 -129
    f2 = x**2 + y**2 - z**2 - 9.75
    f3 = x + y - z - 9.49
    print(f1)
    print(f2)
    print(f3)