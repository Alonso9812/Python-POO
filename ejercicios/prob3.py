#guardar 10 nombre en una lista y luego imprimirlos ejemplo primer nombre, segundo nombre, etc cantidad de nombres guardados

nombres = ["john", "maria", "pedro", "lucia", "carlos", "ana", "luis", "sophia", "diego", "laura"]
posisiones = ["primer", "segundo", "tercer", "cuarto", "quinto", "sexto", "séptimo", "octavo", "noveno", "décimo"]

for i in range(len(nombres)):
    print(f"{posisiones[i]} nombre: {nombres[i]}")
print(f"Total de nombres guardados: {len(nombres)}")


# perdir 5 numeros mostrar mayor, menor y promedio sin usar max, min o sum

numeros = []

for i in range(5):
    num = float(input(f"Ingresa el número {i+1}: "))
    numeros.append(num) 

mayor = numeros[0]
menor = numeros[0]
suma = 0

for num in numeros:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
    suma += num

promedio = suma / len(numeros)

print(f"Mayor número: {mayor}")
print(f"Menor número: {menor}")
print(f"Promedio: {promedio}")      

#
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for name in names:
    name = input("Ingrese un nombre: ")
    if name in names:
        print(f"{name} encontrado en la posision {i+1}") 
    else:
        print(f"{name} no se encuentra en la lista.")

