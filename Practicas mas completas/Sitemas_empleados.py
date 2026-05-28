# Sistema de gestión de empleados

class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.__salario = salario

    def registrar_accion(funcion):
        def funcion_activa(self):
            print("Buscando la funcion: ")
            print(f"La función activa es: {funcion.__name__}")
            funcion(self)
            print("Saliendo")
        return funcion_activa

    @registrar_accion
    def trabajar(self):
        pass

    @registrar_accion
    def mostrar_info(self):
        print(f""" Datos del Empleado
              Nombre: {self.nombre}
              Edad: {self.edad}
              Salario: {self.__salario} colones """)
              
        
    def consultar_salario(self):
        print(f"El salario del empleado {self.nombre} es de: {self.__salario} colones")

    def cambiar_salario(self):
        clave = "1234"

        clave_actual = input("Ingrese la clave: ")
        if clave_actual == clave:
            new_salario = input("Ingrese el nuevo salario: ")
            self.__salario = new_salario
            print("salario cambiado con exito: ")
        else:
            print("clave incorrecta, no puedes cambiar el salario ")

class Programador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje_programacion):
        super().__init__(nombre, edad, salario)
        self.lenguaje_programacion = lenguaje_programacion

    def trabajar(self):
        print(f"{self.nombre} esta desarrollando en {self.lenguaje_programacion}")

class Diseñador(Empleado):
    def __init__(self, nombre, edad, salario, herramienta):
        super().__init__(nombre, edad, salario)
        self.herramienta = herramienta

    def trabajar(self):
        print(f"{self.nombre} esta maquetando una interfaz")

class Administrador(Empleado):
    def __init__(self, nombre, edad, salario, area):
        super().__init__(nombre, edad, salario)
        self.area = area 

    def trabajar(self):
        print(f"{self.nombre} esta organizando tareas en el área de {self.area}")

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
salario = float(input("Ingrese el salario: "))
lenguaje = input("Ingrese el lenguaje de programación: ")

empleado = Programador(nombre, edad, salario, lenguaje)

#empleado = [programador]

#def runlist(empleado):
#    for item in empleado:
#        item.trabajar()

#runlist(empleado)

while True:
    print("1. Mostrar Empleado")
    print("2. Hacer trabajar empleados")
    print("3. Consultar salario")
    print("4. Cambiar Salario")
    print("5. salir")

    opcion = input("SELECCIONE UNA OPCIÓN: ")

    if opcion == "1":
        empleado.mostrar_info()
    elif opcion == "2":
        empleado.trabajar()
    elif opcion == "3":
        empleado.consultar_salario()
    elif opcion == "4":
        empleado.cambiar_salario()
    elif opcion == "5":
        print("SALIENDO DEL MENU: ")
        break
    
         

