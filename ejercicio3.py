# Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

def division(dividendo, divisor):
    if dividendo % divisor == 0:
        Cociente= dividendo // divisor
        Resto= dividendo % divisor
        return (f"La división es exacta, Cociente:{Cociente} , Resto:{Resto} ")
    else:
        Cociente= dividendo // divisor
        Resto= dividendo % divisor
        return (f"La división no es exacta, Cociente:{Cociente} , Resto:{Resto} ")

dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))

print(division(dividendo, divisor))