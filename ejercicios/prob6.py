for item in range(1, 101):
    print(item)

# tabla de multiplicar
for i in range (1,13):
    print(("tabla del " + str(i)))
    for j in range (1,13):
        print(str(i) + " x " + str(j) + " = " + str(i*j))


# Adivinar numero
import random
number = random.randint(1, 100)
guess = 0
while guess != number:
    guess = int(input("Adivina el numero entre 1 y 100: "))

    if guess > 100:
        print("Numero invalido: ")
    elif guess <= 100:
        if guess < number:
            print("Demasiado bajo, intenta de nuevo.")
        elif guess > number:
            print("Demasiado alto, intenta de nuevo.")
print("¡Felicidades! Adivinaste el numero.")

# menu infinito

while True:
    print("1. Sumar")
    print("2. restar")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("Estoy sumando")
    elif opcion == "2":
        print("Estoy restando")
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
