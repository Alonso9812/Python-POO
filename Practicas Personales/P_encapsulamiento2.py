#Sistema de Productos de una tienda

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def info(self):
        print(f"""DATOS DEL PRODUCTO
              Nombre: {self.nombre}
              Precio: {self.__precio}
              Stock: {self.__stock} """)
        
    def consultar_stock(self):
        print(f"{self.nombre} tiene {self.__stock} unidades disponibles")

    def aumentar_stock(self, unidades):
        self.__stock += unidades
        print(f"Se agregaron {unidades} unidades de {self.nombre} al inventario")

    def vender_producto(self, unidades):
        if self.__stock >= unidades:
            self.__stock -= unidades
            print(f"se vendieron {unidades} unidades de {self.nombre}")
        elif self.__stock < unidades:
            print("Unidades en stock insuficientes")

    def cambiar_precio(self):
        clave = "1234"
        clave_actual = input("Ingrese la clave de administrador: ")
        if clave_actual == clave:
            new_precio = float(input("Ingrese el nuevo precio: "))
            self.__precio = new_precio
            print("El precio ha sido cambiado con exito!: ")
        else:
            print("Clave incorrecta, no se pudo cambiar el precio :(")

nombre = input("Ingrese su nombre: ")
precio = float(input("Ingrese el precio del producto: "))
stock = int(input("Ingrese la cantidad de unidades: "))

producto = Producto(nombre, precio, stock)

while True:
    print("1. Mostrar Producto")
    print("2. Consultar Stock")
    print("3. Vender Producto")
    print("4. Agregar Stock")
    print("5. cambiar Precio")
    print("6. Salir")

    opcion = input("Seleccione una opción del menu: ")

    if opcion == "1":
        producto.info()
    elif opcion == "2":
        producto.consultar_stock()
    elif opcion == "3":
        unidades = int(input("Ingrese las unidades: "))
        producto.vender_producto(unidades)
    elif opcion == "4":
        unidades = int(input("Ingrese las unidades: "))
        producto.aumentar_stock(unidades)
    elif opcion == "5":
        producto.cambiar_precio()
    elif opcion == "6":
        print("Salir del Menu")
        break