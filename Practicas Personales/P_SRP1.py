
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        print(f""" Info del Producto
              Producto: {self.nombre}
              Precio: {self.precio}
              Cantidad: {self.cantidad}""")

class CalculadoraDePedido:
    def calcular_total(self, productos):
        total = 0
        for producto in productos:
            total += producto.precio * producto.cantidad
        print(f"Total del pedido: {total}")
    
class GeneradorFactura:
    def generar_factura(self, productos):
        total = 0
        print("Factura Física")
        for producto in productos:
            subtotal = producto.precio * producto.cantidad
            total += subtotal
            print(f"""{producto.nombre}: {producto.cantidad} x {producto.precio} = {subtotal}""")
        print(f"Total de la factura: {total}")

# Guardar pedido en un archivo de texto, con el formato: Producto: cantidad x precio = subtotal
class GuardaPedido:
    def guardar_pedido(self, productos):
        with open("pedido.txt", "w") as archivo:
            total = 0
            for producto in productos:
                subtotal = producto.precio * producto.cantidad
                total += subtotal
                archivo.write(f"{producto.nombre}: {producto.cantidad} x {producto.precio} = {subtotal}\n")
            archivo.write(f"Total del pedido: {total}\n")


producto1 = Producto("Arroz", 1200, 3)
producto2 = Producto("Frijoles", 1500, 2)
productos = [producto1, producto2]

total = CalculadoraDePedido()
info = GeneradorFactura()

producto1.mostrar_informacion()
producto2.mostrar_informacion()

total.calcular_total(productos)
info.generar_factura(productos)

guardar = GuardaPedido()
guardar.guardar_pedido(productos)