### EXCEPCIONES ###

num1, num2 = 5, 1
num2 = '1'

# Try except
try:
    print (num1 + num2)
    print ('No se ha producido error')
except:
    print ('Se ha producido un error')
    
# Try except else finally

try:
    print (num1 + num2)
    print ('No se ha producido error')
except:
    print ('Se ha producido un error')
else:
    # Se ejecuta si no se produce la excepción
    print ('La ejecución continua correctamente')
finally:
    # Se ejecuta siempre
    print ('La ejecución continua ')
    

# Excepción por tipo    
    
try:
    print (num1 + num2)
    print ('No se ha producido error')
except TypeError as error:  # Este bloque se ejecuta solo si es un TypeError
    print (error)

