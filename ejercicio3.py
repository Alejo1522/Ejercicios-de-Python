# Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

numero1=int(input("Ingrese un número: "))
numero2=int(input("Ingrese otro número: "))

if numero1>numero2:
    numero1, numero2 = numero2, numero1

suma=0
expresion=""

for i in range (numero1+1, numero2):
    suma += i
    expresion += str(i)
    if i+1 < numero2:
        expresion+=" + "

print(f"{expresion} = {suma}")