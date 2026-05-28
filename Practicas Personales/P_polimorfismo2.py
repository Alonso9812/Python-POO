#Sistema de empleados 

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self):
        pass

class Programador(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def trabajar(self):
        print(f"{self.nombre} esta desarrollando un video juego")

class Diseñador(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def trabajar(self):
        print(f"{self.nombre}  estoy maquetando")

class Administrador(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def trabajar(self):
        print(f"{self.nombre} estoy revisando las cuentas ")

persona1 = Programador("Jordi")
persona2 = Diseñador("Juan")
persona3 = Administrador("Maria")

lista = [persona1, persona2, persona3]

def recorrer(lista):
    for item in lista:
        item.trabajar()

recorrer(lista)