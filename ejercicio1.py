# Escriba un programa que determine la cantidad de dígitos en un número entero ingresado por el usuario:

numero=int(input("Ingrese un numero: "))

cantidad=len(str(abs(numero)))

print(f"El número {numero} tiene {cantidad} de digitos")