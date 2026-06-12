# combinar lista y diccionario

clientes = [
    {"nombre": "Ana", "saldo": 500},
    {"nombre": "Luis", "saldo": 300}
]

for cliente in clientes:
    print(f"Cliente: {cliente['nombre']}, Saldo: {cliente['saldo']}")
# Agregar un nuevo cliente
nuevo_cliente = {"nombre": "Carlos", "saldo": 400}
clientes.append(nuevo_cliente)
# Mostrar todos los clientes después de agregar el nuevo cliente
print("\nDespués de agregar un nuevo cliente:")
for cliente in clientes:
    print(f"Cliente: {cliente['nombre']}, Saldo: {cliente['saldo']}")
# Actualizar el saldo de un cliente
clientes[0]["saldo"] += 100  # Ana recibe un depósito de 100    
# Mostrar todos los clientes después de actualizar el saldo
print("\nDespués de actualizar el saldo de Ana:")
for cliente in clientes:
    print(f"Cliente: {cliente['nombre']}, Saldo: {cliente['saldo']}")       


    