class Jugador:
    def __init__(self, nombre, correo, password, nivel, vida, monedas):
        self.nombre = nombre
        self.correo = correo
        self.__password = password
        self.nivel = nivel 
        self.vida = vida
        self.monedas = monedas 

    def mostrar_perfil(self):
        print(f"""PERFIL DEL JUGADOR
            Nombre: {self.nombre}
            Correo: {self.correo}
            Nivel: {self.nivel}
            Vida: {self.vida}
            Monedas: {self.monedas}""")
        
    def subir_nivel(self):
        self.nivel += 1
        print(f"Felicidadez has subido de nivel {self.nivel}")


    def recibir_recompensa(self):
        self.monedas += 50
        print(f"Has ganado 50 monedas de oro total: {self.monedas}")

    def recibir_daño(self, dano):
       self.vida -= dano

class Enemigo:
    def __init__(self, nombre, vida, dano):
        self.nombre = nombre
        self.vida = vida
        self.dano = dano

    def mostrar_enemigo(self):
        print(f"""INFORMACIÓN DEL ENEMIGO
                Nombre: {self.nombre}
                Vida: {self.vida}
                Daño: {self.dano}""")
        
    def atacar(self, jugador):
        jugador.recibir_daño(self.dano)
        print(f"El jugador {jugador.nombre} ha recibido {self.dano} puntos de daño")
        
class Batalla():
    def __init__(self, jugador, enemigo):
        self.jugador = jugador
        self.enemigo = enemigo

    def seleccionar_enemigo(self):
        for i, enemigo in enumerate(enemigos):
            print(f"{i + 1}. {enemigo.nombre}")
            
        selec_enemigo = int(input("Seleccione el Enemigo"))
        self.enemigo = enemigos[selec_enemigo - 1]
        return enemigo
    
    def atacar_enemigo(self, enemigo):
        ataque = 25
        enemigo.vida -= ataque
        print("ATACANDO: has hecho 25 puntos de daño")

    def recibir_daño(self, enemigo):
        self.enemigo.atacar(self.jugador)

    def ganador_perdedor(self):
        if self.jugador.vida > self.enemigo.vida:
            ganador = "ganador"
            print(f"El jugador {self.jugador.nombre}")
            self.jugador.subir_nivel()
            self.jugador.recibir_recompensa()
        else:
            print(f"El enemigo {enemigo.nombre} ha ganado la partida")

 #Guardar datos de jugadores y enemigos en archivos txt
class GuardarDatos:
    def guardar_jugador(self, jugador):
        with open("jugadores.txt", "a") as file:
            file.write(f"{jugador.nombre},{jugador.correo},{jugador.nivel},{jugador.vida},{jugador.monedas}\n")

    def guardar_enemigo(self, enemigo):
        with open("enemigos.txt", "a") as file:
            file.write(f"{enemigo.nombre},{enemigo.vida},{enemigo.dano}\n")

    def cargar_jugadores(self):
        jugadores = []
        try:
            with open("jugadores.txt", "r") as file:
                for line in file:
                    nombre, correo, nivel, vida, monedas = line.strip().split(",")
                    jugador = Jugador(nombre, correo, "", int(nivel), int(vida), int(monedas))
                    jugadores.append(jugador)
        except FileNotFoundError:
            print("No se encontraron datos de jugadores.")
        return jugadores
    
    def cargar_enemigos(self):
        enemigos = []
        try:
            with open("enemigos.txt", "r") as file:
                for line in file:
                    nombre, vida, dano = line.strip().split(",")
                    enemigo = Enemigo(nombre, int(vida), int(dano))
                    enemigos.append(enemigo)
        except FileNotFoundError:
            print("No se encontraron datos de enemigos.")
        return enemigos
            


class Menu:
    def __init__(self):
        self.jugadores = []
        self.enemigos = []
        self.guardar_datos = GuardarDatos()

    def registrar_jugador(self):
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")
        jugador = Jugador(nombre, correo, password, nivel=1, vida=100, monedas=0)
        self.jugadores.append(jugador)
        print(f"Jugador {nombre} registrado exitosamente")

    def iniciar_sesion(self):
        correo = input("Ingrese su correo: ")
        password = input("Ingrese su contraseña: ")
        for jugador in self.jugadores:
            if jugador.correo == correo and jugador._Jugador__password == password:
                print(f"Bienvenido {jugador.nombre}")
                self.menu_jugador(jugador)
                return
        print("Correo o contraseña incorrectos")

    def menu_principal(self):
        while True:
            print("""
            1. Registrar jugador
            2. Iniciar sesión
            3. Salir
            """)

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_jugador()

            elif opcion == "2":
                self.iniciar_sesion()

            elif opcion == "3":
                break

            else:
                print("Opción no válida, por favor intente de nuevo")


    def menu_jugador(self, jugador):
        while True:
            print("""
            1. Ver perfil
            2. Seleccionar enemigo
            3. Atacar enemigo
            4. Salir
            """)

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                jugador.mostrar_perfil()

            elif opcion == "2":
                enemigo = batalla.seleccionar_enemigo()

            elif opcion == "3":
                batalla.atacar_enemigo(enemigo)
                batalla.recibir_daño(enemigo)
                batalla.ganador_perdedor()

            elif opcion == "4":
                break

            else:
                print("Opción no válida, por favor intente de nuevo")   
menu = Menu()
menu.menu_principal()   

batalla = Batalla()
guardar_datos = GuardarDatos()


