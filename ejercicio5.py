# Adivinar el número
# Escriba un programa que «piense» un número entre 0 y 100, y entregue pistas al usuario para que lo adivine.
# El programa puede obtener un número al azar entre 0 y 100.
# El usuario debe ingresar su intento, y el programa debe decir si el número pensado es mayor, menor, o el correcto.

import random

def adivinar():
    numeroAleatorio = random.randint(1,100)
    intentos=0

    print()
    print("Adivina el número del 1 al 100")

    while True:
        numero=int(input(f"Intento {intentos}: "))
        intentos+=1

        if numero==numeroAleatorio:
            print(f"Correcto. Adivinaste en {intentos} intentos.")
            break
        elif numero < numeroAleatorio:
            print(f"Es mayor que {numero}")
            print()
        else:
            print(f"Es menor que {numero}")
            print()

# Es hora de invertir los roles: ahora usted pensará un número y el computador lo adivinará.
# La estrategia que debe seguir el programa es recordar siempre cuáles son el menor y el mayor valor posibles, y siempre probar con el valor que está en la mitad
            
def PC_adivina():
    print()
    print("Piensa en un número del 1 al 100")
    limite_menor=1
    limite_mayor=100
    intentos=0
    numeroAleatorio = random.randint(1,100)
    print(f"Intento {intentos}: {numeroAleatorio}")

    while True:
        intentos+=1
        opcion=input("Ingrese <, > o =, dependiendo si el intento es menor, mayor o correcto: ")

        if opcion == "=":
            print(f"Adivine en {intentos} intentos.")
            break
        elif opcion == ">":
            limite_menor = numeroAleatorio
            numeroAleatorio = random.randint(limite_menor, limite_mayor)
            print(f"Intento {intentos}: {numeroAleatorio}")
        elif opcion == "<":
            limite_mayor = numeroAleatorio
            numeroAleatorio = random.randint(limite_menor, limite_mayor)
            print(f"Intento {intentos}: {numeroAleatorio}")
        else:
            print("Opción incorrecta")

opcion=(int(input("Ingrese 1 para adivinar el número o 2 para que la computadora adivine el numero: ")))

if opcion == 1:
    adivinar()
elif opcion == 2:
    PC_adivina()
else:
    print("Opcion invalida")