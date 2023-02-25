### SETS ###

my_set = set() # Construimos un set
print (type(my_set))
my_other_set = {'Perro', 'Gato', 'Pájaro'} # De esta manera también construimos un set !Ojo si está vacío es un diccionario¡
print (type(my_other_set))

print (len(my_other_set)) # Sabemos la cantidad de elementos que tiene el set

my_other_set.add('García') # Añadimos un elemento al set
print (my_other_set)

''' Un set no es una estructura ordenada ni admite elementos repetidos'''

print ('Marcos' in my_other_set) # Comprobamos si un elemento está dentro de un set
print (my_other_set)

print (my_other_set.remove('Pájaro')) # Eliminamos un elemento del set
print (my_other_set.clear()) # Borra todo el set

print (len(my_other_set))

my_new_set = my_other_set.union(my_set) # Unimos dos set
print (my_new_set)

print (my_new_set.difference(my_set)) # Hacemos la diferencia entre los dos sets



