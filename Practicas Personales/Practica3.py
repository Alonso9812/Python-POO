#Gestor de inventario de videojuegos

class Videojuego:
    def __init__(self, nombreVJ, genero, precio, cantidad_disponible):
        self.nombreVJ = nombreVJ
        self.genero = genero
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
  
    def vender_videojuego(self, cantidad):
        if self.cantidad_disponible >= cantidad:
            self.cantidad_disponible -= cantidad
            print(f"Vendiendo {cantidad} unidades de {self.nombreVJ}")
        else:
            print("Cantidad insuficiente en el inventario")
    
    def agregar_unidades(self, cantidad):
        self.cantidad_disponible += cantidad
        print(f"Agregando {cantidad} unidades de {self.nombreVJ} al inventario")
    
    def mostrar_informacion(self):
        print(f"Nombre del videojuego: {self.nombreVJ}")
        print(f"Genero: {self.genero}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad disponible: {self.cantidad_disponible}")



nombreVJ = input("Ingrese el nombre del videojuego: ")
genero = input("Ingrese el genero del videojuego: ")
precio = float(input("Ingrese el precio del videojuego: "))
cantidad_disponible = int(input("Ingrese la cantidad disponible del videojuego: "))

game = Videojuego(nombreVJ, genero, precio, cantidad_disponible)
print(f"""LOS DATOS DEL VIDEOJUEGO SON: \n\n
      Nombre del videojuego: {game.nombreVJ} \n
      Genero: {game.genero} \n
      Precio: {game.precio} \n
      Cantidad disponible: {game.cantidad_disponible}""")

#CREANDO UN MENU PARA REALIZAR LAS OPERACIONES DEL INVENTARIO DE VIDEOJUEGOS
while True:
    print("1. Vender videojuego")
    print("2. Agregar unidades al inventario")
    print("3. Mostrar informacion del videojuego")
    print("4. Salir")

    opcion = input("Seleccione la opcion que desea realizar: ")

    if opcion == "1":
        cantidad = int(input("Ingrese la cantidad a vender: "))
        game.vender_videojuego(cantidad)
    elif opcion == "2":
        cantidad = int(input("Ingrese la cantidad a agregar al inventario: "))
        game.agregar_unidades(cantidad) 
    elif opcion == "3":
        game.mostrar_informacion()
    elif opcion == "4":       
        print("Saliendo del programa...")
        break