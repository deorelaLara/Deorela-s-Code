import math 

x = int(input('Ingresa el valor de X: '))
h = int(input('Ingresa el valor de h: '))
n = int(input('Rango que deseas que tenga tu funcion: '))

def Taylor(x, n):
    res = 0
    for i in range(n):
        res += ((x**i)*(math.exp(x))*(h)/math.factorial(i))
    return float(res)

#COMPARAMOS LA FUNCION QUE CREAMOS PARA APROXIMAR A TAYLOR Y LA FUNCION APROXIMACION EN PYTHON
for i in range(0, n):
    e_aprox= Taylor(x, i)
    e_exp = math.exp(x)
    e_error = abs(e_aprox - e_exp/e_exp)*100
    print(f'{i} terms: Taylor Series approx= {e_aprox}, exp calc= {e_exp}, error = {e_error}')
    if e_error < 1:
        break
#LLAMAMOS LA FUNCION 
#Taylor(x, n)
