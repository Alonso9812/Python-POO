#Clase basica

class Persona():
    nombre = "Juan"
    edad = 30
    altura = 1.75

persona1 = Persona()
persona1.nombre = "Jordi"
print(persona1.nombre)

#Clase Funcional
# def__init_ es el constructor de la clase, se ejecuta cada vez que se crea un nuevo objeto de esa clase
class Celular:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio


celular1 = Celular("Apple", "iphone 17", 1000)
celular2 = Celular("Samsung", "Galaxy S26", 1000)

print(celular1.modelo)
print(celular2.modelo)
