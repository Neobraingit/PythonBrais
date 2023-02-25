### DICCIONARIOS ###

my_diccionario = {'nombre' : 'Marcos', 'edad' : 48, 'apellido' : 'Carmona'}
my_other_diccionario = {}
 
'''Los diccionarios son creados por claves  y valores (pares)'''

print (type(my_diccionario))

print (len(my_diccionario))

print (my_diccionario['nombre']) # Accedemos a un elemento en particular
my_diccionario['nombre'] = 'pedro' # Aquí cambiamos el valor de la clave
print (my_diccionario['nombre'])

my_diccionario['calle'] = 'San tirso de abres' # Añadimos una clave, valor nuevas
print (my_diccionario)

del my_diccionario['calle'] # Eliminamos un elemento y su valor. Si no pusieramos clace nos cargaríamos el diccionario completo
print (my_diccionario)

print ('Marcos' in my_diccionario) # Comprobamos si un elemento está en un dicccionario, pero nos dice False por que lo que buscamos es la clave y no el valor

print (my_diccionario.items()) # Nos lista todos los elementos
print (my_diccionario.keys()) # Nos lista todas las claves
print (my_diccionario.values()) # Nos lista todos los valores
print (my_diccionario.fromkeys('nombre', 'edad')) # Nos recorre las keys como si de un for se tratara y crea un diccionario sin valores

my_list = ['Nombre', 1, '2']
my_new_dict = my_diccionario.fromkeys(my_list) # Convertimos una lista a un diccionario sin valores
print (my_new_dict)
'''5:46:13'''