### TUPLAS ###

my_tuple = ()
my_other_tuple = ()

my_tuple = (48, 1.80, 'Marcos', 'Carmona')

print (type(my_tuple))

print (my_tuple[0]) # Podemos acceder con slicing como en las listas
print (my_tuple[::-1]) # Le damos la vuelta a la tupla

print (my_tuple.count('García')) # Nos cuenta el número de elementos que hemos introducidos y nos dice cuantas veces aparece

print (my_tuple.index('Marcos')) # Nos dice el índice en el que está el elemento indicado

''' Los datos de las tuplas son inmutables; no se pueden cambiar'''

my_other_tuple = ('Pelusa', 'Dune')

print (my_other_tuple + my_tuple) # Concatenando tuplas

print (my_other_tuple[2:3]) # Creamos una subtupla por medio de slicing

new_tuple = list(my_other_tuple) # Convertimos la tupla a lista
print (new_tuple)
print (type(new_tuple)) # Comprobamos el tipo de colección que es

del my_other_tuple # Borramos la tupla
print (my_other_tuple) # Nos muestra un error por que la tupla no está definida ya que se borró en el paso anterior con el del



