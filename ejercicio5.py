# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso

def numeroInvertido(numero):
    numero_invertido = int(str(numero)[::-1])
    return numero_invertido

numero=int(input("Ingrese el numero que va a invertir: "))

print(numeroInvertido(numero))