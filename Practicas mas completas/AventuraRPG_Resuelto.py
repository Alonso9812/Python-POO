class Jugador:
    def __init__(self, nombre, correo, password, nivel, vida, monedas):
        self.nombre = nombre
        self.correo = correo
        self.__password = password
        self.nivel = nivel
        self.vida = vida
        self.monedas = monedas

    def mostrar_perfil(self):
        print(f"""
            PERFIL DEL JUGADOR
            Nombre: {self.nombre}
            Correo: {self.correo}
            Nivel: {self.nivel}
            Vida: {self.vida}
            Monedas: {self.monedas}
            """)

    def subir_nivel(self):
        self.nivel += 1
        print(f"¡Has subido al nivel {self.nivel}!")

    def recibir_recompensa(self):
        self.monedas += 50
        print(f"Has ganado 50 monedas. Total: {self.monedas}")

    def recibir_daño(self, dano):
        self.vida -= dano

    def obtener_password(self):
        return self.__password
    
class Enemigo:
    def __init__(self, nombre, vida, dano):
        self.nombre = nombre
        self.vida = vida
        self.dano = dano

    def mostrar_enemigo(self):
        print(f"""
            ENEMIGO
            Nombre: {self.nombre}
            Vida: {self.vida}
            Daño: {self.dano}
            """)

    def atacar(self, jugador):
        jugador.recibir_daño(self.dano)

        print(
            f"{self.nombre} atacó a {jugador.nombre} "
            f"y causó {self.dano} puntos de daño."
        )

class Batalla:
    def __init__(self, jugador, enemigo):
        self.jugador = jugador
        self.enemigo = enemigo

    def atacar_enemigo(self):
        dano = 25

        self.enemigo.vida -= dano

        print(
            f"{self.jugador.nombre} atacó "
            f"e hizo {dano} puntos de daño."
        )

    def recibir_daño(self):
        self.enemigo.atacar(self.jugador)

    def ganador_perdedor(self):

        if self.enemigo.vida <= 0:

            print(
                f"¡{self.jugador.nombre} ha derrotado a "
                f"{self.enemigo.nombre}!"
            )

            self.jugador.subir_nivel()
            self.jugador.recibir_recompensa()

            return True

        elif self.jugador.vida <= 0:

            print(
                f"{self.enemigo.nombre} ha derrotado a "
                f"{self.jugador.nombre}"
            )

            return True

        return False

    def iniciar_batalla(self):

        while True:

            print("\n--- COMBATE ---")

            print(
                f"{self.jugador.nombre}: "
                f"{self.jugador.vida} HP"
            )

            print(
                f"{self.enemigo.nombre}: "
                f"{self.enemigo.vida} HP"
            )

            input("Presione ENTER para atacar...")

            self.atacar_enemigo()

            if self.ganador_perdedor():
                break

            self.recibir_daño()

            if self.ganador_perdedor():
                break

class GuardarDatos:

    def guardar_jugador(self, jugador):

        with open("Jugadores.txt", "a") as archivo:

            archivo.write(
                f"{jugador.nombre},"
                f"{jugador.correo},"
                f"{jugador.obtener_password()},"
                f"{jugador.nivel},"
                f"{jugador.vida},"
                f"{jugador.monedas}\n"
            )

    def cargar_jugadores(self):

        jugadores = []

        try:

            with open("Jugadores.txt", "r") as archivo:

                for linea in archivo:

                    datos = linea.strip().split(",")

                    jugador = Jugador(
                        datos[0],
                        datos[1],
                        datos[2],
                        int(datos[3]),
                        int(datos[4]),
                        int(datos[5])
                    )

                    jugadores.append(jugador)

        except FileNotFoundError:

            print("No existe Jugadores.txt")

        return jugadores

    def cargar_enemigos(self):

        enemigos = []

        try:

            with open("Enemigos.txt", "r") as archivo:

                for linea in archivo:

                    datos = linea.strip().split(",")

                    enemigo = Enemigo(
                        datos[0],
                        int(datos[1]),
                        int(datos[2])
                    )

                    enemigos.append(enemigo)

        except FileNotFoundError:

            print("No existe Enemigos.txt")

        return enemigos

class Menu:

    def __init__(self):

        self.guardar = GuardarDatos()

        self.jugadores = self.guardar.cargar_jugadores()

        self.enemigos = self.guardar.cargar_enemigos()

    def registrar_jugador(self):

        nombre = input("Nombre: ")
        correo = input("Correo: ")
        password = input("Contraseña: ")

        jugador = Jugador(
            nombre,
            correo,
            password,
            1,
            100,
            0
        )

        self.jugadores.append(jugador)

        self.guardar.guardar_jugador(jugador)

        print("Jugador registrado.")

    def iniciar_sesion(self):

        correo = input("Correo: ")
        password = input("Contraseña: ")

        for jugador in self.jugadores:

            if (
                jugador.correo == correo
                and jugador.obtener_password() == password
            ):

                print(f"Bienvenido {jugador.nombre}")

                self.menu_jugador(jugador)

                return

        print("Credenciales incorrectas.")

    def seleccionar_enemigo(self):

        print("\nENEMIGOS DISPONIBLES")

        for i, enemigo in enumerate(self.enemigos):

            print(f"{i+1}. {enemigo.nombre}")

        opcion = int(input("Seleccione enemigo: "))

        return self.enemigos[opcion - 1]

    def menu_jugador(self, jugador):

        while True:

            print("""
                1. Ver perfil
                2. Ir a batalla
                3. Cerrar sesión
                """)

            opcion = input("Seleccione: ")

            if opcion == "1":

                jugador.mostrar_perfil()

            elif opcion == "2":

                enemigo = self.seleccionar_enemigo()

                batalla = Batalla(
                    jugador,
                    enemigo
                )

                batalla.iniciar_batalla()

            elif opcion == "3":

                break

    def menu_principal(self):

        while True:

                        print("""
                1. Registrar jugador
                2. Cargar jugadores
                3. Cargar enemigos
                4. Iniciar sesión
                5. Salir
                """)

                        opcion = input("Seleccione: ")

                        if opcion == "1":
                            self.registrar_jugador()

                        elif opcion == "2":

                            self.jugadores = self.guardar.cargar_jugadores()

                            print(
                                f"Se cargaron "
                                f"{len(self.jugadores)} jugadores."
                            )

                        elif opcion == "3":

                            self.enemigos = self.guardar.cargar_enemigos()

                            print(
                                f"Se cargaron "
                                f"{len(self.enemigos)} enemigos."
                            )

                        elif opcion == "4":

                            self.iniciar_sesion()

                        elif opcion == "5":
                            print("¡Hasta luego!")
                            break

menu = Menu()
menu.menu_principal()