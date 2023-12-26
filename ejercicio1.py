#Escriba un programa que determine si el número entero ingresado por el usuario es par o no.

def determinarPar(numero):
    if numero%2==0:
        return ("Su número es par")
    else:
        return ("Su número es impar")
    
numero=(int(input("Ingrese un numero: ")))

print(determinarPar(numero))