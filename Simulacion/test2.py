import random
from graphics import *

ladoVentana = 500
radioVentana = ladoVentana/2
centro = Point(radioVentana, radioVentana)
enCirculo = 0.

print("Estimacion de pi por el Metodo de Montecarlo")

puntos = int(input('Cantidad de pruebas que deseas realizar -Puntos aleatorios- : '))
if(puntos < 1):
    puntos = 2
"""
    PARTE GRAFICA 
"""
ventana = GraphWin('Ventana de Grafico', ladoVentana, ladoVentana)
ventana.setBackground('red')
ventana.setCoords(0, 0, ladoVentana, ladoVentana)

circulo = Circle(centro, radioVentana)
circulo.setOutline('blue')
circulo.setWidth(3)
circulo.draw(ventana)


"""
    PARTE LOGICA 
"""
for n in range(puntos):
    x = random.uniform(-radioVentana, radioVentana)
    y = random.uniform(-radioVentana, radioVentana)
    ventana.plot(x + radioVentana, y + radioVentana)
    #Si x** y y** es menor entonces el punto cayo dentro del circulo y se le suma un valor
    if((x**2 + y**2) <= radioVentana**2):
        enCirculo+=1
#Utilizamos la expresion matematica para determinar la aprox a PI
# 4 * lanzamientos en el circulo / total de lanzamientos
valorpi = 4. *enCirculo/puntos

print('VALOR ESTIMADO DE PI = ', valorpi)
print('####################################')

ventana.getMouse()
ventana.close()