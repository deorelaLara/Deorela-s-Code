import math
"""
    Un paracaidista, con una masa de 68.1kg salta de un globo aerostatico fijo.
    Calcule la velocidad antes de abrir el paracaidas. Cf = 12.5 kg/s
            V(t) = (( g * m ) / c) * ( 1 - e^(( -c / m ) * t ))
"""
#DATOS
m = 68.1
c = 12.5
g = 9.8
x = c/m
#Incrementamos el tiempo (t) --. es infinito a partir de t=28
for t in range(1, 12, 2):
    t += 1
    print(t)
    resultado = ((g*m)/c) * (1 - math.exp((-c/m)*t))
    print(resultado)