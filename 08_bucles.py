### BUCLES ###

'''Nos sirven para pasar por el mismo código varias veces'''

# While

condicion = 0
 
while  condicion < 10:
    print (condicion)
    condicion += 1
    
i = 10
while i >= 0:
    i -= 1
    print (i)
    
print ('Cuenta atrás finalizada')

# For

milista = ['nombre', 'apellido', 'edad', 'altura']
for i in milista:
    print (i)
    
mitupla = ('Marcos', 'David', 'Eva', 'Marta')
for i in mitupla:
    if i == 'David':
        break
    print (i)

midiccionario = {'nombre' : 'Marcos', 'apellido' : 'Carmona'}
for i in midiccionario.values():
    print(i)
print ('El bucle for ha finalizado')
    
'''Con el for, podremos recorrer iterando cualquier tipo de colección'''



