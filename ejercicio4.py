# En cada ronda del juego del cachipún, los dos competidores deben elegir entre jugar tijera, papel o piedra.

# Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.

# El ganador del juego es el primero que gane tres rondas.

# Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra.
def obtener_jugada():
    jugada=input("Elige una opción piedra, papel o tijera.: ")
    while jugada.lower() not in ["piedra", "papel", "tijera"]:
        print("Opción incorrecta, intentelo de nuevo")
        jugada=input("Elige una opción piedra, papel o tijera.: ")
    return jugada.lower()

def determinarGanador(jugador1, jugador2):
    if jugador1==jugador2:
        return "empate"
    elif(jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"): 
        return "jugador1"
    else:
        return "jugador2"
        
def mostrar_puntaje(puntaje_jugador1,puntaje_jugador2):
    return (f"Marcador: A: {puntaje_jugador1} - B: {puntaje_jugador2}")
    
puntaje_jugador1=0
puntaje_jugador2=0

while puntaje_jugador1 < 3 and puntaje_jugador2 < 3:
    jugador1=obtener_jugada()
    jugador2=obtener_jugada()

    ganador=determinarGanador(jugador1, jugador2)

    if ganador=="jugador1":
        puntaje_jugador1+=1
    elif ganador=="jugador2":
        puntaje_jugador2+=1

    print(mostrar_puntaje(puntaje_jugador1,puntaje_jugador2))

if puntaje_jugador1==3:
    print("El ganador es el jugador 1!!")
else:
    print("El ganador es el jugador 2!!")