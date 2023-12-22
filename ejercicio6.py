#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo

def sacarHipotenusa(cateto_A,cateto_B):
    hipotenusa=(cateto_A**2+cateto_B**2)**0.5
    return (f"La hipotenusa es: {hipotenusa}")

cateto_A=float(input("Ingrese la longitud del cateto A: "))
cateto_B=float(input("Ingrese la longitud del cateto B: "))

print(sacarHipotenusa(cateto_A,cateto_B))