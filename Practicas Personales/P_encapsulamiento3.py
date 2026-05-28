# Sistema gestor de libros 

class Libro:
    def __init__(self, titulo, autor, copias_disponibles, codigo_seguridad):
        self.titulo = titulo
        self.autor = autor
        self.__copias_disponibles = copias_disponibles
        self.__codigo_seguridad = codigo_seguridad

    def mostrar_info(self):
        print(f"""DATOS DEL LIBRO: \n
              Titulo: {self.titulo}
              Autor: {self.autor} """)
        
    def consultar_copias(self):
        print(f"{self.titulo} tiene {self.__copias_disponibles} copias disponibles")

    def prestar_libro(self):
        if self.__copias_disponibles >= 1:
            self.__copias_disponibles -= 1
            print(F"El libro {self.titulo}, se presto con exito")
        elif self.__copias_disponibles == 0:
            print(f"El libro {self.titulo} no tiene copias disponibles")

    def devolver_libro(self):
        self.__copias_disponibles += 1
        print(f"Se ha devuelto el libro: {self.titulo}")

    def cambiar_codigo(self):
        codigo_actual = input("Ingrese el codigo del libro: ")

        if codigo_actual == self.__codigo_seguridad:
            nuevo_codigo = input("Ingrese el nuevo codigo: ")
            self.__codigo_seguridad = nuevo_codigo
            print("Codigo actualizado")
        else:
            print("Codigo incorrecto... ")

titulo = input("Ingrese el titulo del libro: ")
autor = input(" Ingrese el autor del libro: ")
copias_disponibles = int(input("Ingrese la cantidad de copias: "))
codigo_seguridad = input("Ingrese el codigo de seguridad: ")

libro = Libro(titulo, autor, copias_disponibles, codigo_seguridad)

while True:

    print("1. Mostra info del libro: ")
    print("2. Consultar copias: ")
    print("3. Prestar libro: ")
    print("4. Devolver libro: ")
    print("5. Cambiar codigo: ")
    print("6. Salir del menu: ")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        libro.mostrar_info()
    elif opcion == "2":
        libro.consultar_copias()
    elif opcion == "3":
        libro.prestar_libro()
    elif opcion == "4":
        libro.devolver_libro()
    elif opcion == "5":
        libro.cambiar_codigo()
    elif opcion == "6":
        print("Salir del menu...")
        break

