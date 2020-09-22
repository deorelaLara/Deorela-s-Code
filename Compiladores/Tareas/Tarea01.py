"""
    Alumna: Alvarado Lara Luz Deorela Sabas
    Matricula: 10021265
    Tarea 01, 02, 03
"""
import os

#### CONTADOR LINEAS DE UN ARCHIVO ######
print('######### Contador de Lineas en un archivo de texto #########')
file_name = open('c:/Users/deore/OneDrive/Escritorio/Code/Compiladores/file.txt','r')
print('1. Numero de lineas: ', len(file_name.readlines())) # Nos debe devolver 5 
file_name.close()

####### VARIABLES #######
print('######### Contador de IF en una Oracion ##########')
file_name = open('c:/Users/deore/OneDrive/Escritorio/Code/Compiladores/file.txt','r')
arr = []
count = file_name

####### CONTAR IF AL INICIO DE UNA LINEA #######
dex = 0
middle = 0
last = 0
for word in count:
    wrd = word.split(' ')
    arr.append(wrd)
    if (wrd[0] == 'if' or wrd[0] == 'IF' or wrd[0] == 'If'):
        dex = dex + 1
    #print(dex)
    if(wrd[-1] == ' if' or wrd[len(wrd)-1] == ' IF' or wrd[len(wrd)-1] == ' If'):
        last += 1

print('2. Numero de IF al inicio de una linea: ', dex)
print('3. Numero de IF al final de una Oracion: ', last)


### ORDENAR UN ARCHIVO ######
file_name = open('c:/Users/deore/OneDrive/Escritorio/Code/Compiladores/file.txt','r')
#print(file_name)
lineas = []
for linea in file_name:
    lineas.append(linea)

#ordenamos las lineas
ordenar = sorted(lineas, key=len)
for linea in ordenar:
    print(linea[:-1])



