#Gestor de biblioteca

class Libro:
    def __init__(self, titulo, autor, genero, codigo, disponibilidad=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo
        self.disponibilidad = disponibilidad

    def agregar_nuevo_libro(self, titulo, autor, genero, codigo):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo
        self.disponibilidad = True
        print(f"Agregando el libro {self.titulo} a la biblioteca")
    
    def prestar_libro(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print(f"Prestando el libro {self.titulo}")
        else:
            print("El libro no esta disponible para prestar")
    
    def devolver_libro(self):
        if not self.disponibilidad:
            self.disponibilidad = True
            print(f"Devolviendo el libro {self.titulo}")
        else:
            print("El libro ya esta disponible en la biblioteca")

    def mostrar_informacion(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Genero: {self.genero}")
        print(f"Codigo: {self.codigo}")
        print(f"Disponibilidad: {self.disponibilidad}")

titulo = input("Ingrese el titulo del libro: ")
autor = input("Ingrese el autor del libro: ")
genero = input("Ingrese el genero del libro: ")
codigo = input("Ingrese el codigo del libro: ")
disponibilidad = input("Ingrese la disponibilidad del libro (True/False): ")

libro = Libro(titulo, autor, genero, codigo, disponibilidad)
print(f"""DATOS DEL LIBRO: \n\n
Titulo: {libro.titulo}
Autor: {libro.autor}
Genero: {libro.genero}
Codigo: {libro.codigo}
Disponibilidad: {libro.disponibilidad}
""")
#CREANDO UN MENU PARA REALIZAR LAS OPERACIONES DE LA BIBLIOTECA
while True:
    print("1. Agregar nuevo libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar informacion del libro")
    print("5. Salir")

    opcion = input("Ingrese la opcion que desea realizar: ")

    if opcion == "1":
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el genero del libro: ")
        codigo = input("Ingrese el codigo del libro: ")
        libro.agregar_nuevo_libro(titulo, autor, genero, codigo)
    elif opcion == "2":
        libro.prestar_libro()
    elif opcion == "3":
        libro.devolver_libro()
    elif opcion == "4":
        libro.mostrar_informacion()
    elif opcion == "5":
        print("Saliendo del programa...")
        break






