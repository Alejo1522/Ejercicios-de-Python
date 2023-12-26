# En cada ronda del juego del cachipún, los dos competidores deben elegir entre jugar tijera, papel o piedra.

# Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.

# El ganador del juego es el primero que gane tres rondas.

# Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra.
puntajeA=0
puntajeB=0
def jugar_ronda(jugadorA, jugadorB):
    if jugadorA==jugadorB:
        return 0
    elif(jugadorA == "piedra" and jugadorB == "tijera") or (jugadorA == "papel" and jugadorB == "piedra") or (jugadorA == "tijera" and jugadorB == "papel"):
        return (f"{puntajeA+1} - {puntajeB}")
    
    else:
        return (f"{puntajeA} - {puntajeB+1}")
        
def jugar_juego():
    rondas=3

    jugadores=["jugadorA", "jugadorB"]
    opciones=["piedra","tijera","papel"]

    for ronda in range(1, rondas+1):
        print(f"Ronda: {ronda}")

        for jugador in jugadores:
            seleccion=input(f"{jugador} elige una opcion piedra, papel o tijera: ").lower()

            while seleccion not in opciones:
                print("¡Opción no valida! Debes elegir piedra, papel o tijera")
                seleccion=input(f"{jugador} elige una opcion piedra, papel o tijera: ").lower()

        resultado=jugar_ronda(jugadores[0], jugadores[1])
        print(f"{resultado}")
        

jugar_juego()