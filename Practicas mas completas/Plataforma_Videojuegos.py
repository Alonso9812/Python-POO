
class Usuario:
    def __init__(self, nombre, correo, saldo):
        self.nombre = nombre
        self.correo = correo
        self.__saldo = saldo
    
    def mostrar_info(self):
        print(f"""DATOS DEL USUARIO
                Nombre: {self.nombre}
                Correo: {self.correo} """)

    @property
    def saldo(self):
        return self.__saldo
    
    def descontar_saldo(self, monto):
        self.__saldo -= monto

    def consultar_saldo(self):
        print(f"El Saldo del usuario {self.nombre} es de: {self.__saldo} colones")

    def depositar(self):
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        self.__saldo += cantidad
        print("Deposito Realizado")

    def retirar(self):
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > self.__saldo:
            print("Saldo insuficiente")
        elif cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro una cantidad de: {cantidad} colones")

class GestorUsuario:

    def crear_usuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        correo = input("Correo del usuario: ")
        saldo = 0
        
        usuario = Usuario(nombre, correo, saldo)
        return usuario

class ValidarCorreo:
    def validar_correo(self, correo):
       if "@" in correo.correo and ".com" in correo.correo: 
            print("Correo valido")
       else: 
           print("Correo invalido")

#Herencia y Polimorfismo
class Jugador(Usuario):
    def __init__(self, nombre, correo, saldo, nickname):
        super().__init__(nombre, correo, saldo)
        self.nickname = nickname

    def usar_plataforma(self):
        print(f"El Jugador {self.nickname} esta jugando videojuegos")

class Administrador(Usuario):
    def __init__(self, nombre, correo, saldo, nivel_admin):
        super().__init__(nombre, correo, saldo)
        self.nivel_admin = nivel_admin

    def usar_plataforma(self):
        print(f"rol {self.nivel_admin}:  {self.nombre} esta gestionando usuarios")

class Streamer(Usuario):
    def __init__(self, nombre, correo, saldo, plataforma_stream):
        super().__init__(nombre, correo, saldo)
        self.plataforma_stream = plataforma_stream

    def usar_plataforma(self):
        print(f"El streamer {self.nombre} esta tramitiendo en vivo por {self.plataforma_stream}")
#Metodos Magicos  __str__ y __add__
class VideoJuego:
    def __init__(self, nombre_V, precio, horas_jugadas):
        self.nombre_V = nombre_V
        self.precio = precio
        self.horas_jugadas = horas_jugadas
    
    def mostrar_Video_Game(self):
        print(f""" Datos del video juego
            NOmbre: {self.nombre_V}
            Precio: {self.precio} 
            Horas:Jugadas {self.horas_jugadas}""")

    def __str__(self):
        return f'Persona(nombre={self.nombre_V}, edad={self.precio},  horas_jugados={self.horas_jugadas})'
    
    def __add__(self, otro_vg):
        nuevo_nombre = self.nombre_V + " " + otro_vg.nombre_V
        nuevo_precio = self.precio + otro_vg.precio
        nueva_horas = self.horas_jugadas + otro_vg.horas_jugadas

        return VideoJuego(nuevo_nombre, nuevo_precio, nueva_horas)
# Principio SRP
class Tienda:
   def comprar_videojuego(self, usuario, videojuego):

        if usuario.saldo >= videojuego.precio:
            usuario.descontar_saldo(videojuego.precio)
            print(f"{usuario.nombre} compró "f"{videojuego.nombre_V}")
            print(f"Saldo restante: {usuario.saldo}")
        else:
            print("Saldo insuficiente")
# Principio SRP
class Factura:
    def generar(self, usuario, videojuego):

        print(f"""
            ============= FACTURA =============

            Cliente: {usuario.nombre}

            Videojuego: {videojuego.nombre_V}

            Precio: {videojuego.precio} colones

            Saldo restante: {usuario.saldo} colones

            ==================================
            """)
#SRP      
class GuardarDatos:
    def guardar(self, usuarios):
        with open("Usuarios_Plataforma.txt", "w") as archivo:
            archivo.write("Usuarios de la plataforma\n\n")
            for usuario in usuarios:
                archivo.write(
                    f"{usuario.nombre}, "
                    f"{usuario.correo}, "
                    f"{usuario.saldo}\n"
                )

class ImprimirFactura:
    def imprimir(self, usuario, videojuego):
        with open("Factura.txt", "w") as archivo:
            archivo.write(f"""
============= FACTURA =============

Cliente: {usuario.nombre}

Videojuego: {videojuego.nombre_V}

Precio: {videojuego.precio} colones

Saldo restante: {usuario.saldo} colones

==================================
""")
        print("Factura guardada correctamente")
# Principio OCP
class Tester(Usuario):
    def __init__(self, nombre, correo, saldo, servidor):
        super().__init__(nombre, correo, saldo)
        self.servidor = servidor
    def usar_plataforma(self):

        print(
            f"El tester {self.nombre} "
            f"está probando el servidor "
            f"{self.servidor}"
        )

class Editor(Usuario):
    def __init__(self, nombre, correo, saldo, servidor):
        super().__init__(nombre, correo, saldo)
        self.servidor = servidor

    def usar_plataforma(self):
        print(
            f"El Editor {self.nombre} "
            f"está esperando el servidor "
            f"{self.servidor}"
        )

class Moderador(Usuario):
    def __init__(self, nombre, correo, saldo, servidor):
        super().__init__(nombre, correo, saldo)
        self.servidor = servidor

    def usar_plataforma(self):
        print(
            f"El moderador {self.nombre} "
            f"está moderando el servidor "
            f"{self.servidor}"
        )
               
gestor = GestorUsuario()
usuarios = []

gamer = Jugador("Jordi", "jordi@gmail.com", 5000, "Gallito_game")
admin = Administrador("Carlos", "admin@gmail.com", 10000, "Soporte")
influencer = Streamer("Juana", "juana@gmail.com", 300000, "Twitch")
tester = Tester("Lucas", "luca@gmail.com", 54000, "Servidor")
editor = Editor("Tatiana", "taty@gmail.com", 81000, "servidor")
moderador = Moderador("Paulina", "penas@gmail.com", 300000, "servidor")

usuarios = [gamer, admin, influencer, tester, editor, moderador]

def runlist(usuarios):
    for item in usuarios:
        item.usar_plataforma()

videogame1 = VideoJuego("Gog", 12000, 8)
videogame2 = VideoJuego("dog", 10000, 7)
videojuegos = [videogame1, videogame2]

def runlista(videojuegos):
    for item in videojuegos:
        item.mostrar_Video_Game()

def nuevo_game():
    return videogame1 + videogame2

validar = ValidarCorreo()
validar.validar_correo(gamer)

tienda = Tienda()
factura = Factura()
guardar = GuardarDatos()
imprimir = ImprimirFactura()
while True:

    print(f"1. Gestion Usuario: ")
    print("2. Mostrar Usuarios Activos: ")
    print("3. Fusionar Games: ")
    print("4. VideoJuegos: ")
    print("5. Comprar Videojuego: ")
    print("6. Imprimir datos de usuario")
    print("7. Imprimir Factura")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            print("1. Crear Usuarios: ")
            print("2. Mostrar Datos: ")
            print("3. Consultar Saldo: ")
            print("4. Depositar")
            print("5. Retirar")
            print("6. Menu Principal") 

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nuevo_usuario = gestor.crear_usuario()
                usuarios.append(nuevo_usuario)
                print("Usuario creado con éxito")   
            elif opcion == "2":
                if len(usuarios) == 0:
                    print("No hay usuarios registrados")
                else:
                    for usuario in usuarios:
                        usuario.mostrar_info()   
            elif opcion == "3":
                 
                 print("\nUSUARIOS")
                 for i, usuario in enumerate(usuarios):
                    print(f"{i + 1}. {usuario.nombre}")

                 seleccion_usuario = int(input("Seleccione usuario: "))
                 usuario = usuarios[seleccion_usuario - 1]
                 usuario.consultar_saldo()
            
            elif opcion == "4":
                 print("\nUSUARIOS")
                 for i, usuario in enumerate(usuarios):
                    print(f"{i + 1}. {usuario.nombre}")

                 seleccion_usuario = int(input("Seleccione usuario: "))
                 usuario = usuarios[seleccion_usuario - 1]
                 usuario.depositar()
            elif opcion == "5":
                print("\nUSUARIOS")
                for i, usuario in enumerate(usuarios):
                    print(f"{i + 1}. {usuario.nombre}")

                seleccion_usuario = int(input("Seleccione usuario: "))
                usuario = usuarios[seleccion_usuario - 1]
                usuario.retirar()
            elif opcion == "6":
                print("Regresando al menu Principal... ... ...")
                break

    elif opcion == "2":
        runlist(usuarios)
    elif opcion == "3":
        game_fusionado = nuevo_game()
        print("Video juego fusionado")
        game_fusionado.mostrar_Video_Game()
    elif opcion == "4":
        runlista(videojuegos)
    elif opcion== "5":
        print("\nUSUARIOS")

        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. {usuario.nombre}")

        seleccion_usuario = int(input("Seleccione usuario: "))

        usuario = usuarios[seleccion_usuario - 1]
        print("\nVIDEOJUEGOS")

        for i, juego in enumerate(videojuegos):
            print(f"{i + 1}. {juego.nombre_V}")
        seleccion_juego = int(input("Seleccione videojuego: "))
        videojuego = videojuegos[seleccion_juego - 1]
        tienda.comprar_videojuego(usuario, videojuego)
        factura.generar(usuario, videojuego)
    elif opcion == "6":
         guardar.guardar(usuarios)
         print("Usuarios guardados correctamente")
    elif opcion == "7":
        imprimir.imprimir(usuario, videojuego)
    elif opcion == "8":
        print("Saliendo del sistema... ... ... ")
        break

