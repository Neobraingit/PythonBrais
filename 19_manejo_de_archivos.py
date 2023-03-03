### MANEJO DE ARCHIVOS ###

# .txt file

import os

txt_file = open ('/Users/marcos/Documents/Documentos - MacBook Pro de Marcos/Brais/PythonBrais/file.txt','r+') # Leer y escribir
# print (txt_file.read())
# print (txt_file.read(10)) # Solo lee los 10 primeros caracteres
# print (txt_file.readline()) # Lee línea a línea
# print (txt_file.readlines()) # Saltos de línea

txt_file.write('\nHola mundo')
#os.remove('/Users/marcos/Documents/Documentos - MacBook Pro de Marcos/Brais/PythonBrais/file.txt') # Borramos el fichero

# .jason file

import json

json.file = open('my_file.json', 'w+') # Creamos el fichero

json.text = {'Nombre' : 'Marcos', 
             'Apellido'  : 'Carmona',
             'Segundo_apellido' : 'García'}

json.dump(json.text, json.file)







