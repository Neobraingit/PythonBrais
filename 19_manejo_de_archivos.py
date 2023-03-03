### MANEJO DE ARCHIVOS ###

# .txt file

import os

txt_file = open ('/Users/marcos/Documents/Documentos - MacBook Pro de Marcos/Brais/PythonBrais/file.txt','r+') # Leer y escribir
# print (txt_file.read())
# print (txt_file.read(10)) # Solo lee los 10 primeros caracteres
# print (txt_file.readline()) # Lee línea a línea
# print (txt_file.readlines()) # Saltos de línea

txt_file.write('\nHola mundo')







