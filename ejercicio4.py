#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

def convercion(centimetros):
    return (f"{centimetros}cm equivalen a {centimetros/2.54}in")

centimetros=int(input("Ingrese los centimetros que va a convertir: "))

print(convercion(centimetros))