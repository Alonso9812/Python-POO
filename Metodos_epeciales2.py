class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, other):
        nuevo_valor = self.edad + other.edad
        return Persona(self.nombre+other.nombre, nuevo_valor)
    
persona1 = Persona("Juan", 30)
persona2 = Persona("Maria", 25)

nueva_persona = persona1 + persona2
print(nueva_persona)  # Output: Persona(nombre=JuanMaria, edad=55)  
print(nueva_persona.nombre)  # Output: JuanMaria
print(nueva_persona.edad)  # Output: Persona(nombre=JuanMaria, edad=55)