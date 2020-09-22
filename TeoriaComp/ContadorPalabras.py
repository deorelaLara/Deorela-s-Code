"""Escribir una aplicacion llamada "Contador de Palabras",
   que lea lineas de un archivo tipo texto, hasta que encuentre el fin del archivo

   La aplicacion debe indicar cuantas palabras tiene cada linea, una palabra es un conjunto
   de caracteres separados por uno oo mas espacios. Y tambien debe indicar el numero de lineas leidas.

   Alumno(a) : ALVARADO LARA LUZ DEORELA SABAS
   Matricula: 10021265

   """

def contarPalabras(archivo = 'test.txt'):
    local = open(archivo, 'r')
    lineas = local.readlines()
    for i in range(0,len(lineas)):
        print('línea {}: {} palabras'.format(i+1, len(lineas[i].split())))

def contarLineas(archivo = 'test.txt'):
    local = open(archivo, 'r')
    print('total {} líneas.'.format(len(local.readlines())))
    local.close()

def main():
    contarPalabras()
    contarLineas()

if __name__ == '__main__':
    main()
