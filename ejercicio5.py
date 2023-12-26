# Escriba un programa que pida al usuario que ingrese varios valores enteros, que pueden ser positivos o negativos. Cuando se ingrese un cero, el programa debe terminar y mostrar un gráfico de cuántos valores positivos y negativos fueron ingresados:

contador_negativos=0
contador_positivos=0

print("Ingrese un cero para terminar")

while True:
    numero=int(input("Ingrese un numero: ")) 
    if numero > 0:
        contador_positivos+=1
    elif numero < 0:
        contador_negativos+=1
    else:
        break

print(f"Positivos: {'*'*contador_positivos}")
print(f"Negativos: {'*'*contador_negativos}")