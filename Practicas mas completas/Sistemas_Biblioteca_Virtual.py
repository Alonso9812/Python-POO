
from typing import Self


class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
    
    def mostrar_datos(self):
        print(f"""Datos Del Usuario
              Nombre: {self.nombre}
              Correo: {self.correo}""")
        
class Usuario(Persona):
    def __init__(self, nombre, correo, id_usuario):
        super().__init__(nombre, correo)
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def mostrar_libros_prestados(self):
        if len(self.libros_prestados) == 0:
            print("No tiene libros prestados")
        else:
            for libro in self.libros_prestados:
                print("----------------")
                print(f"Título: {libro.titulo}")
                print(f"Autor: {libro.autor}")    

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)
        

class Libro:
    def __init__(self, codigo, titulo, autor,disponible):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def mostrar_info(self):
        print(f"""Informamción del libro
              Codigo: {self.codigo}
              Titulo: {self.titulo}
              Autor: {self.autor}
              Disponibilidad: {self.disponible}""")
        
class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self. libros = []


    def registrar_usuarios(self):
        nombre = input("Nombre del usuario: ")
        correo = input("Correo del usuario: ")
        id_usuario =input("Ingrese el id usuario: ")

        usuario = Usuario(nombre, correo, id_usuario)
        self.usuarios.append(usuario)

        print("Usuario registrado con exito")

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            usuario.mostrar_datos()

    def registrar_libros(self):
        codigo = input("Codigo del libro: ")
        titulo = input("Titulo del libro: ")
        autor = input("Autor del libro: ")
        disponible = True 

        libro = Libro(codigo, titulo, autor, disponible)
        self.libros.append(libro)
        print("Libro registrado con exito")

    def mostrar_libros(self):
        for libro in self.libros:
            libro.mostrar_info()
        
    def prestar_libros(self):
        id_buscar = input("Ingrese el ID del usuario: ")
        for usuario in self.usuarios:
            if usuario.id_usuario == id_buscar:
                codigo = input("Ingrese el código del libro: ")
                for libro in self.libros:
                    if libro.codigo == codigo:
                        if libro.disponible:
                            usuario.libros_prestados.append(libro)
                            usuario.prestar_libro(libro)
                            print(f"Libro {libro.titulo} prestado a {usuario.nombre}")
                            libro.disponible = False
                        else:
                            print("Libro no disponoble")
                print("Libro no existe")
        print("El usuario no existe")
                            

    def mostrar_prestamos_usuario(self):
        id_buscar = input("Ingrese el ID del usuario: ")
        for usuario in self.usuarios:
            if usuario.id_usuario == id_buscar:
                usuario.mostrar_libros_prestados()
                return 
        print("Usuario no encontrado")

    def devolver_libro(self):
        id_buscar = input("Ingrese el ID del usuario: ")
        for usuario in self.usuarios: 
            if usuario.id_usuario == id_buscar:
                codigo_buscar = input("Ingrese el codigo del libro: ")
                for libro in usuario.libros_prestados:
                    if libro.codigo == codigo_buscar:
                        usuario.devolver_libro(libro)
                        libro.disponible = True
                        print(f"El usuario {usuario.nombre} a devuelto el libro {libro.titulo}")
                        return
                print("Libro no existe!")
                return
        print("Usuario no existe!")    

    def guardar_usuario(self):
        with open("Usuarios.txt", "w", ) as archivo:
            archivo.write("USUARIOS REGISTRADOS\n\n")
            for usuario in self.usuarios:
                archivo.write(
                    f"{usuario.nombre}, "
                    f"{usuario.correo}, "
                    f"{usuario.id_usuario}\n"
                )
            

    def guardar_libro(self):
        with open("Libros.txt", "w", ) as archivo:
            archivo.write("LIBROS DE LA BIBLIOTECA\n\n")
            for libro in self.libros:
                archivo.write(
                    f"{libro.codigo}, "
                    f"{libro.titulo}, "
                    f"{libro.autor}, "
                    f"{libro.disponible}\n"
                )

    def cargar_libros(self):
        with open("Libros.txt", "r") as archivo:
         for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            if "LIBROS DE LA BIBLIOTECA" in linea:
                continue
            datos = linea.split(",")
            codigo = datos[0].strip()
            titulo = datos[1].strip()
            autor = datos[2].strip()
            disponible = datos[3].strip()
            libro = Libro(codigo, titulo, autor, disponible)
            if disponible == "True":
                libro.disponible = True
            else:
                libro.disponible = False
            self.libros.append(libro)
         print("Datos cargados correctamente")

    def cargar_usuarios(self):
        self.usuarios.clear()
        with open("Usuarios.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                if "USUARIOS REGISTRADOS" in linea:
                    continue
                datos = linea.split(",")
                nombre = datos[0].strip()
                correo = datos[1].strip()
                id_usuario = datos[2].strip()
                usuario = Usuario(nombre, correo, id_usuario)
                self.usuarios.append(usuario)
        print("Datos cargados correctamente")

biblioteca = Biblioteca()

while True:
    print("1. Mostrar Usuarios: ")
    print("2. Libros prestados: ")
    print("3. Devolver libro: ")
    print("4. Mostrar libros: ")
    print("5. Gestiionar Usuario: ")
    print("6. Salir del sistema: \n")

    opcion = input("Ingrese una opcion:")

    if opcion == "1":
        biblioteca.mostrar_usuarios()
    elif opcion == "2":
        biblioteca.mostrar_prestamos_usuario()
    elif opcion == "3":
        biblioteca.devolver_libro()
    elif opcion == "4":
        biblioteca.mostrar_libros()
    elif opcion == "5":
        while True:
            print("1. Registrar Usuarios: ")
            print("2. Registrar Libros: ")
            print("3. Prestar Libros: ")
            print("4. Devolver Libros: ")
            print("5. Guaradar Libros: ")
            print("6. Guardar Usuarios: ")
            print("7. Cargar Libros: ")
            print("8. Cargar Usuarios: ")
            print("9. Reegresar: \n")

            opcion = input("Sleccione una opcion: ")

            if opcion == "1":
                biblioteca.registrar_usuarios()
            elif opcion == "2":
                biblioteca.registrar_libros()
            elif opcion == "3":
                biblioteca.prestar_libros()
            elif opcion == "4":
                biblioteca.devolver_libro()
            elif opcion == "5":
                biblioteca.guardar_libro()
            elif opcion == "6":
                biblioteca.guardar_usuario()
            elif opcion == "7":
                biblioteca.cargar_libros()
            elif opcion == "8":
                biblioteca.cargar_usuarios()
            elif opcion == "9":
                print("Regresar...")
                break
    elif opcion == "6":
        print("Saliendo del sistema... ... ..")
        break


