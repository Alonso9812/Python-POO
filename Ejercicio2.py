# sistema de escuela 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ver_datos(self):
        print(f""" DATOS DE LA PERSONA \n  
              Nombre: {self.nombre}
              Edad: {self.edad} """)
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def ver_grado(self):
        print(f"El grado del estudiante es: {self.grado} grado")

Estudiante1 = Estudiante("Jordi", 27, 5)
Estudiante1.ver_datos()
Estudiante1.ver_grado()