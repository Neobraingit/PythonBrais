# Variables
num1 = 1 # Esto es una variable de tipo numérico
str2 = 'Esto es una variable de tipo string'

print (type(num1)) # Type nos dice de que tipo es una variable o dato

''' 
Las variables tienen que ser nombradas de manera simple, sin caracteres extraños ni palabras reservadas de Python
'''

my_variable = 'my string variable'
print (my_variable)

my_int_variable = 5
print (my_int_variable)

my_bool_variable = True
print (my_bool_variable)

print (my_variable, my_int_variable) # Aquí imprimimos dos variables seguidas

# Casting de variables
my_variable_convertida = str(my_int_variable) # Convertimos una variable de tipo numérico a string
print (type(my_variable_convertida))

# Concatenación de cadenas
cadena1 = 'Esto es una '
cadena2 = 'concatenación de cadenas'
print (cadena1 + cadena2) # Aquí concatenamos las dos cadenas

# Como saber la longitud de una cadena de texto
print (len(cadena1))

# Parámetros en los print
print ('Me llamo Marcos Carmona García', cadena2) # Concatenamos el string directamente con la variable

# Inputs y variables
nombre = input('Escribe tu nombre: ')
edad = input('¿Qué edad tienes? ')
print (nombre)
print ('Tengo', edad, 'años')

# Variables en una sola línea (no es una buena práctica)
nombre, apellido = 'Marcos', 'Carmona'
print (nombre, apellido)





