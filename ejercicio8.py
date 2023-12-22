#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

def decimal(numero):
    parte_decimal=abs(numero) % 1
    return parte_decimal

numero=float(input("Ingrese un numero: "))

print(decimal(numero))