# Un jugador debe lanzar dos dados numerados de 1 a 6, y su puntaje es la suma de los valores obtenidos.
# Un puntaje dado puede ser obtenido con varias combinaciones posibles. Por ejemplo, el puntaje 4 se logra con las siguientes tres combinaciones: 1+3, 2+2 y 3+1.
# # Escriba un programa que pregunte al usuario un puntaje, y muestre como resultado la cantidad de combinaciones de dados con las que se puede obtener ese puntaje

numero=int(input("Ingrese el puntaje : "))

if numero<12:
    cantidad=0
    for i in range(1,7):
        for k in range(1,7):
            if i + k == numero:
                cantidad+=1
    print(f"Hay {cantidad} combinaciones para obtener {numero}")
else:
    print(f"Hay 0 combinaciones para obtener {numero}")