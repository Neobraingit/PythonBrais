### RESOLVER RETOS ###

'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''

def fizzbuzzz():
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print ('fizzbuzz')
        elif i % 3 == 0:
            print ('fizz')
        elif i % 5 == 0:
            print ('buzz')
        else:
             print(i)
            
       
        
fizzbuzzz()

'''
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
'''

def anagrama(string1, string2):
    if  string1.lower() == string2.lower()[::-1]:
       return True
    else:
        return False

print (anagrama('amor', 'roma'))

'''
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
 '''
 
def fibonacci():
     prev = 0
     next = 1
     for i in range(0, 51):
          
         
         fib = prev + next # Suma de  prev más next
         prev = next  # Prev igual a next
         next = fib  # Next igual a fib
         print (i)
         print (prev)
     
     
     
fibonacci()


