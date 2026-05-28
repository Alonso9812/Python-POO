# La herencia permite acceder a la clase hija a todos los atributos y métodos de la clase padre, además de agregar sus propios atributos y métodos.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"{self.nombre} Hola estoy hablando un poco.")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

roberto = Empleado("Roberto", 30, "Mexicano", "Programador", 50000)

roberto.hablar()

# La función super() se utiliza para llamar al método __init__ de la clase padre (Persona) desde la clase hija (Empleado), lo que permite inicializar los atributos heredados.

