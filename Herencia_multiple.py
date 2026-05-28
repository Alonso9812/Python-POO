# Herencia multiple: En Python, una clase puede heredar de múltiples clases padre. Esto se logra simplemente listando las clases padre entre paréntesis al definir la clase hija.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"{self.nombre} Hola estoy hablando un poco.")

class Artista:
    def __init__(self, arte):
        self.arte = arte

    def mostrar_arte(self):
        return f"Mi arte es: {self.arte}"
    
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, arte, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, arte)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años, soy {self.nacionalidad}, trabajo en {self.empresa} y mi arte es {self.arte}.")

jordi = EmpleadoArtista("Jordi", 25, "Español", "Pintura", 40000, "Galería de Arte")

jordi.presentarse()


herencia_multiple = issubclass(EmpleadoArtista, Artista) 
instancia = isinstance(jordi, EmpleadoArtista)
print(instancia)
print(f"¿EmpleadoArtista es una subclase de Artista? {herencia_multiple}")
