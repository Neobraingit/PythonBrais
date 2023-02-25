### LISTAS ###

my_list = list()
my_other_list = []

print (len(my_list))
print (len(my_other_list))

my_list = ['perro', 'gato', 123, 23344]
print (len(my_list)) # Comprobamos el número de elementos de una lista

my_other_list = [1.80, 48, 'Marcos', 'Carmona']
print (my_other_list)
print (type(my_other_list)) # Vemos de que tipo es el dato, en este caso una lista

print (my_other_list[1]) # Accedemos a nuestra edad por medio de slicing
print (my_other_list[0])
print (my_other_list.count('Marcos')) # Nos cuenta cuantos elementos como el pasado existen


altura, edad, nombre, apellido = my_other_list # Todo en una sola línea
print (edad)

print (my_list + my_other_list) # Sumando dos listas(no se pueden hacer màs operaciones con las listas)

my_other_list.append('Marcos Carmona García') # Añadimos un elemento en una lista
print (my_other_list)
my_other_list.insert(3, 'Perro') # Insertamos un elemento en un índice
print (my_other_list)
my_other_list.remove('Perro') # Borramos un elemento
print (my_other_list)
my_other_list.pop() # Borramos el último elemento
print (my_other_list)
my_other_list.pop(2) # Con pop también podemos elegir qué índice queremos eliminar, aunque no sería lo habitual
print (my_other_list)
del my_other_list[2] # Así borramos un índice elegido
print (my_other_list)
my_other_list.clear() # Borramos toda la lista del tirón
print (my_other_list)
my_new_list = my_list.copy() # Copiamos una lista en otra
print (my_new_list)
my_new_list.reverse() # Le damos la vuelta al la lista
print (my_new_list)
my_new_list.sort() # Ordena la lista pero en este caso no funciona porque hay strings
print (my_new_list)
