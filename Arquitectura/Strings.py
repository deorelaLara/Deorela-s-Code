def suma(a, b):
    return a+b

print(suma(1, 3))

def imprime_nombre(mensaje, nombre):
    #formatear un string
    print(f'{mensaje} {nombre}')

imprime_nombre('Un mensaje coqueto:','juanito')

def division(x, y):
    if y == 0:
        return 0,'Division entre cero'
    return x/y

#IMPRIME EN UNA TUPLA EL RESULTADO Y CADA VALOR LO GUARDA EN UNA VARIABLE ... RESULTADO-MENSAJE

resultado, mensaje= division(10,0)
print(resultado)
print(mensaje)

#FUNCION ANONIMA
suma2 = lambda a, b : a + b
print(suma2(20,10))

mi_funcion = lambda a: a + 10
print(mi_funcion(5))


#formatear un string
nombre = 'juanito'
nombre2 = 'Pedro'
print('Hola! ' + nombre)
#print('Hola! '  nombre) #old style python2
print('Hola!! {}' .format(nombre)) #old style python3
print('HOla!! {} y {}' .format(nombre,nombre2))
