### STRINGS ###

my_string = ' Esto es un string'
print (my_string)
print (len(my_string)) # Calculamos la longitud del string

''' Los strings se pueden concatenar y pueden llevar ciertos caracteres'''

print ('Esto es un string\nque hace un salto de línea')
print ('Esto es un string\tque hace una tabulación')
print ('\tEste es un string escapado')

### FORMATEAR LOS STRINGS ###

nombre = 'Marcos'
edad = '48'
print (f'Mi nombre es {nombre} y mi edad es {edad}') # Formateamos con f 
print ('Mi nombre es {} y mi edad es {}'.format(nombre, edad)) # Otra forma de formatear

### DESEMPAQUETADO DE CARACTERES ###
languaje = 'Python'
a, b, c, d, e, f = 'Python' # Asignamos tantas variables como caracteres tenga la palabra
print (a)
print (b)
print (c)
print (d)
print (e)
print (f)

'''2:47:53'''