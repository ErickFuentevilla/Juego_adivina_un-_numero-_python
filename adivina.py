import random

print("Hola, bienvenido al juego de adivinar un número.")
nombre = input("¿Cuál es tu nombre? ")

numero_secreto = random.randint(1, 100)

print(f"Hola {nombre}, ¿Puedes adivinar en qué número estoy pensando? Es un número del 1 al 100.")

adivinanza = int(input())

while adivinanza != numero_secreto:
    if adivinanza < numero_secreto:
        print("El número es mayor. Por favor, intenta de nuevo.")
    else:
        print("El número es menor. Por favor, intenta de nuevo.")
    adivinanza = int(input())

print(f"¡Perfecto, {nombre}! El número secreto era {numero_secreto}.") 
