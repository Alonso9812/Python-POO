# Sistema Universitario

class Estudiante:
    def __init__(self, nombre, carrera, promedio):
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio
    
    def estudiar(self):
        print(f"{self.nombre} esta estudiando {self.carrera}")
        
class Deportista:
    def __init__(self, deporte):
        self.deporte = deporte
    
    def entrenar(self):
        print(f"Practica Futboll")

class EstudianteDeportista(Estudiante, Deportista):
    def __init__(self, nombre, carrera, promedio, deporte, universidad, n_medallas):
        Estudiante.__init__(self, nombre, carrera, promedio)
        Deportista.__init__(self, deporte)
        self.universidad = universidad
        self.n_medallas = n_medallas

    def mostrar_perfil(self):
        print(f"""PERFIL DEL ESTUDIANTE \n\n
              Nombre: {self.nombre}
              Carrera: {self.carrera}
              Promedio: {self.promedio}
              Deporte: {self.deporte}
              Universidad: {self.universidad}
              Cantidad de Medallas: {self.n_medallas}""")
        
Jordi = EstudianteDeportista("Jordi Lopez Aguero", "Ingenieria de sistemas", 80, "Futboll", "UNA", 1 )
Jordi.mostrar_perfil()
Jordi.estudiar()
Jordi.entrenar()