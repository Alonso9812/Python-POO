#Gestinar vehiculos de reparto, con herencia

class Vehiculo:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def mostrar_datos(self):
        print(f""" LOS DATOS DELVEHICULO SON:
        Marca: {self.marca}
        Modelo: {self.modelo}
        Velocidad: {self.velocidad} km/h""")

class Electrico:
    def __init__(self, bateria):
        self.bateria = bateria

    def cargar_bateria(self):
        print(f"El vehículo se está cargando. Nivel de batería: {self.bateria}%")

class MotoRepart(Vehiculo, Electrico):
    def __init__(self, marca, modelo, velocidad, bateria, Nombre_conductor, Zona_reparto):
        Vehiculo.__init__(self, marca, modelo, velocidad)
        Electrico.__init__(self, bateria)
        self.Nombre_conductor = Nombre_conductor
        self.Zona_reparto = Zona_reparto

    def mostrar_info(self):
        self.mostrar_datos()
        print(f"Conductor: {self.Nombre_conductor}")
        print(f"Zona de reparto: {self.Zona_reparto}")

moto1 = MotoRepart("Yamaha", "YZF-R3", 180, 80, "Carlos", "Zona Norte")
moto1.mostrar_info()
moto1.mostrar_datos()
moto1.cargar_bateria()

