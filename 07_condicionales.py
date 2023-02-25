### CONDICIONALES ###

'''Un condicional en Python se escribe con la palabra reservada if'''

my_condicion = True
if my_condicion: # Si aquí no especificamos nada es que siempre es True
    print ('Se cumple por que es True')
    
print ('La ejecución continua...')

my_condicion = 5 * 2
if my_condicion == 10:
    print ('El resultado es 10')
else:
    print ('No es el resultado de 10')
    
    
condicion = 20

if condicion == 20:
    print ('Se cumple la condición')
elif condicion < 50:
    print ('También se cumple la condición')
else:
    print ('No se cumple la condición')
    
