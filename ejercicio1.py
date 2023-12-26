#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

numero=int(input("Ingrese un numero: "))

for i in range(1, 11):
    resultado=numero * i
    print(f"{numero} * {i} = {resultado}")