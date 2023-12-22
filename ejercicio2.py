# Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

def area(radio):
    return (f"El area del circulo es {3.14*radio**2}")

def perimetro(radio):
    return (f"El perimetro del circulo es {2*(3.14)*radio}")

radio=float(input("Ingrese el radio del circulo: "))

print(area(radio))
print(perimetro(radio))