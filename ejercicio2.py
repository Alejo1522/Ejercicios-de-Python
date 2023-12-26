# Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:

numero=int(input("Ingrese un numero: "))

for i in range(0, numero+1):
    potencia=2**i
    print(potencia, end=" ")