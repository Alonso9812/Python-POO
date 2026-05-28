# los metodos especiales son aquellos que se ejecutan de forma automatica al realizar ciertas acciones,
#  como por ejemplo al imprimir un objeto, al sumar dos objetos, etc.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
persona1 = Persona("Juan", 30)

repre = repr(persona1)
resultado = eval(repre)

print(resultado.nombre)  # Output: Juan