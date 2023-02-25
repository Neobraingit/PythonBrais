### FUNCIONES ###

def myfuncion():
    print ('Esto es una función')
    

myfuncion()

def sum_two_values(num1, num2):
    print (num1 + num2)
    

sum_two_values(2,2)

def sum_two_values_with_return(num1, num2):
    return num1 + num2

my_result = sum_two_values_with_return(10, 5) # Aquí nos guardamos el retorno

print (my_result)

def print_name(name, surname):
    print ('Mi nombre es {} y mi apellido es {}'.format(name, surname))
    
    
print_name('Marcos', 'Carmona')
    
    

