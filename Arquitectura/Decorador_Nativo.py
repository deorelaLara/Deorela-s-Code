########################################
##### Decoradores nativos de Python
########################################

# 1: Funciones como objetos y referencias

def hello_world():
	return 'Hola Mundo!'

def hello_world_with_name(function, name):
	return f'{function()}, y hola {name}!'

print(hello_world_with_name(hello_world, 'Bobby'))

# 2: Funciones internas

def hello_class():
	print('Hola clase de diseño y arquitectura de software!')

	def hello_emilio():
		print('y hola a ti Emilio :D!')

	def hello_angela():
		print('y hola a ti Angela :D!')

	def hello_fer():
		print('y hola a ti Luis Fernando >:D!')

	hello_emilio()
	hello_angela()
	hello_fer()

hello_class()

# 3: Podemos retornar valores desde las funciones internas
def hello_clase(numero):
    print('Hola clase de diseño y arquitectura de software!')
    
    def hello_deorela():
        return 'y hola a ti deorela :D!'
    
    def hello_daniel():
        return 'y hola a ti daniel :D!'
    def hello_piuch():
        return 'y hola a ti piucha >:D'
    
    if numero == 1:
        return hello_deorela()
    if numero == 2:
        return hello_daniel()
    if numero == 3:
        return hello_piuch()
    
print(hello_clase(3))
variable = hello_clase(2)
print(variable)

print('\n\n##### DECORADORES #####')
# 4: Ahora si los decorators! :D

def cafecito():
	print('Cafecito! :D')

def decorador(function):
	def wrapper():
		function()
		print('Con pan!')
		print('Y con leche y azucar >:D!')

	return wrapper

cafecito = decorador(cafecito)
print(cafecito())

print('\n\n#### AZUQUITAR ####')
# 5: Decoradores con "syntactic sugar" ;) wink-wink
def decorador2(function):
    def wrapper():
        function()
        print('con pan!')
        print(' Y con leche y azucar :D!')
    return wrapper

@decorador2
def cafecito2():
    print('Cafecito! :D')

print(cafecito())

