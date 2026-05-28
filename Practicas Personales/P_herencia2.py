#Sistema de personajes para un video juego

class Personaje:
    def __init__(self, nombre, nivel, vida):
        self.nombre = nombre
        self.nivel = nivel
        self.vida= vida
        
    def atacar(self):
        print(f"{self.nombre} esta atacando")

class Mago:
    def __init__(self, tipo_magia):
        self.tipo_magia = tipo_magia

    def lanzar_hechizo(self):
        print(f"Lanzo el hechizo de {self.tipo_magia}")

class MagoGerrero(Personaje, Mago):
    def __init__(self, nombre, nivel, vida, tipo_magia, arma_pricipal, cantidad_mana):
       Personaje.__init__(self, nombre, nivel, vida)
       Mago.__init__(self, tipo_magia)
       self.arma_principal = arma_pricipal
       self.cantidad_mana = cantidad_mana

    def mostrar_personaje(self):
        print(f"""DATOS DEL PERSONAJE \n\n
              Nombre: {self.nombre}\n
              Nivel: {self.nivel}\n
              Vida: {self.vida} %\n
              Tipo Magia: {self.tipo_magia}\n
              Arma Pricipal: {self.arma_principal}\n
              Cantidad de mana: {self.cantidad_mana} """)
        
Personaje1 = MagoGerrero("SKANOR", 34, 100, "MAGIA BLANCA", "ESPADA SOLAR", 300)
Personaje1.mostrar_personaje()
Personaje1.atacar()
Personaje1.lanzar_hechizo()