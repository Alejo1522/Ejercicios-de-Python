# Calculadora
# Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.

# El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

# La salida del programa debe ser el resultado de la operación.

def ordenarNumeros(numero1,operador,numero2):
    if operador == "+":
        return (f"{numero1} + {numero2} = {numero1 + numero2}")
    elif operador == "-":
        return (f"{numero1} - {numero2} = {numero1 - numero2}")
    elif operador == "*":
        return (f"{numero1} * {numero2} = {numero1 * numero2}")
    elif operador == "/":
        return (f"{numero1} // {numero2} = {numero1 // numero2}")
    elif operador == "**":
        return (f"{numero1} ** {numero2} = {numero1 ** numero2}")
    
numero1=int(input("Ingrese un número : "))
operador=input("Ingrese la operación: ")
numero2=int(input("Ingrese otro número : "))

print(ordenarNumeros(numero1,operador,numero2))