# numero primo

num = int(input("Ingrese un numero: "))

for i in range(2, num):
    if num % i == 0:
        print("El numero no es primo")
        break
else:    
    print("El numero es primo")

# invertir una palabra
palabra = input("Ingrese una palabra: ")
palabra_invertida = ""
for letra in palabra:
    palabra_invertida = letra + palabra_invertida
print("La palabra invertida es: " + palabra_invertida)

numers = "12345"
numers_invert = ""
for i in numers:
    numers_invert = i + numers_invert
print("Lista ivertida: " + numers_invert)

#contar vocales 

palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
print("La cantidad de vocales en la palabra es: " + str(contador))

item = input("ingrese un numero: ")
caja = "2154215425"
count = 0

for i in caja:
    if i == item:
        count += 1
print("la cantida del mismo item es de: " + str(count))

# encontrar duplicados en una lista

lista = [1, 2, 3, 4, 5, 1, 2, 3]  
duplicados = []

for i in lista:
    if lista.count(i) > 1 and i not in duplicados:
        duplicados.append(i)
print("Los elementos duplicados en la lista son: " + str(duplicados))

#ordenar lista sin usar sort()

lista = [5, 2, 9, 1, 5, 6]
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
print("Lista ordenada: " + str(lista))

