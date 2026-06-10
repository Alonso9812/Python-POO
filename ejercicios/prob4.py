estudiante = {
    "nombre": "Jordi",
    "edad": 22,
    "carrera": "Ingeniería"
}
print(estudiante)

contactos = {
    "Ana": "8888-8888",
    "Luis": "7777-7777"
}

for contacto in contactos:
    contacto = input("Ingrese el nombre del contacto: ")
    if contacto in contactos:
        print(f"El número de {contacto} es: {contactos[contacto]}")
    else:
        print("Contacto no encontrado.")

#Actualizar stock
productos = {
    "Laptop": 10,
    "Mouse": 20,
    "Teclado": 15
}

for producto in productos:
    producto = input("Ingrese el nombre del producto para actualizar su stock: ")
    if producto in productos:
        nuevo_stock = int(input(f"Ingrese el nuevo stock para {producto}: "))
        productos[producto] = nuevo_stock
        print(f"Stock actualizado para {producto}: {productos[producto]}")
    else:
        print("Producto no encontrado.")

print(productos)
