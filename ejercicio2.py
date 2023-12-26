# Números palíndromos
# Un número natural es un palíndromo si se lee igual de izquierda a derecha y de derecha a izquierda.
# Por ejemplo, 14941 es un palíndromo, mientras que 81924 no lo es.
# Escriba un programa que indique si el número ingresado es o no palíndromo:

numero=int(input("Ingrese un numero: "))

num_invertido=int(str(numero)[::-1])

if numero == num_invertido:
    print(f"{numero} es palindromo")
else:
    print(f"{numero} no es palindromo")