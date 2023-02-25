### CLASES ###

class Persona:
    pass  

print (Persona)


class MyPersona:
    def __init__(self, name, surname, edad):
        self.name = name
        self.surname = surname
        self.edad = edad
        
    def caminar(self):
        print ('Esta persona camina')
        
mypersona = MyPersona('Marcos', 'Carmona',48)
print (mypersona.surname)
print (mypersona.name)
print (mypersona.edad)
mypersona.caminar()

