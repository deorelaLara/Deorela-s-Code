import ply.lex as lex
import re
import codecs
import os 
import sys

reservadas = ['BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO', 'CALL', 'CONST'
                'VAR', 'PROCEDURE', 'OUT', 'IN', 'ELSE']
tokens =reservadas+[ 'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
            'ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
            'LPARENT', 'RPARENT', 'COMMA', 'SEMICOLON', 'DOT', 'UPDATE']

print(tokens)
#palabras reservadas
'''reservadas = {
'begin':'BEGIN',
'end':'END',
'if':'IF',
'then':'THEN',
'whie':'WHILE',
'do':'DO',
'call':'CALL',
'const':'CONST',
'int':'INT',
'procedura ':'PROCEDURE',
'out':'OUT',
'in' : 'IN',
'else' : 'ELSE'
}'''

#TOKENS + RESERVADAS --- > UNIMOS DICCIONARIO CON LISTA 
#HACEMOS NUESTRO DICCIONARIO UNA LISTA
#tokens = tokens + list(reservadas.values())
#print(tokens)

''' DEFINIMOS NUEVAS FUNCIONES PARA CADA TOKEN'''
tok_ignore = '\t ' #Coincide con una tabulacion
tok_plus = r'\+' #N veces el elemento anterior
tok_minus = r'\-'
tok_times = r'\*'
tok_divide = r'/'
tok_ODD = r'ODD'
tok_assign = r'='
tok_NE = r'<>'
tok_LT = r'<'
tok_LTE = r'<='
tok_GT = r'>'
tok_GTE = r'>='
tok_LPARENT = r'\('
tok_RPARENT = r'\)'
tok_COMMA = r','
tok_SEMICOLON = r';'
tok_DOT = r'\.'
tok_UPDATE = r':='

#FUNCION PARA TOKEN ID
def tok_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value

    return t 

def tok_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def tok_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print('error -- > caracter ilegal', t.value[0])
    t.lexer.skip(1)

def buscarFichero(directorio):
    ficheros = []
    #Numero de archivo para listar archivos de prueba
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dir, files in os.walk(directorio):
        ficheros.append(files)
    
    for file in files:
        print(str(cont)+ '. ' +file)
        cont = cont+1
    
    
    while respuesta == False:
        numArchivo = input('\n Numero de Test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta=True
                break

    print ("Has escogido", files[int(numArchivo)-1])
    #print ("Has escogido \" %s\" \n" % %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]


directorio = '/Users/deore/OneDrive/Escritorio/Ago-Dic2020-Semestre/Compiladores/Codigo/Proyecto/pruebas/'
archivo = buscarFichero(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()


'''
    ############################## PRUEBAS PARA LEER FICHERO ###################################
file_name=open('c:/Users/deore/OneDrive/Escritorio/Ago-Dic2020-Semestre/Compiladores/Codigo/Proyecto/test1.txt', 'r')
file_name = buscarFichero(file_name)
cadena = file_name.read()
file_name.close()
'''

analizador = lex.lex()
analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : break
    print(tok)
