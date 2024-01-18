import time

def realizar_movimiento(jugador, tiempo_movimiento):
    print(f"\nTurno de {jugador} - Tiempo restante: {tiempo_movimiento} segundos")
    while True:
        movimiento = input(f"Ingrese el movimiento para {jugador} (o 'Salir' para terminar): ").strip().lower()
        if movimiento == "salir":
            return movimiento
        elif jugador.lower() in movimiento:
            return movimiento
        else:
            print(f"Error: El movimiento debe contener el nombre del jugador en turno ({jugador}). Intente de nuevo.")

def iniciar_partida():
    tiempo_carlsen = 180
    tiempo_nakamura = 180
    tiempo_movimiento = 10

    turno_actual = "Carlsen"

    while True:
        print(f"\nTiempo restante - Magnus Carlsen: {tiempo_carlsen} segundos, Hikaru Nakamura: {tiempo_nakamura} segundos")
        if turno_actual == "Carlsen":
            movimiento = realizar_movimiento("Carlsen", tiempo_movimiento)
            tiempo_carlsen -= tiempo_movimiento
        else:
            movimiento = realizar_movimiento("Nakamura", tiempo_movimiento)
            tiempo_nakamura -= tiempo_movimiento

        if movimiento == "salir" or tiempo_carlsen <= 0 or tiempo_nakamura <= 0:
            break

        if min(tiempo_carlsen, tiempo_nakamura) <= 60:
            tiempo_movimiento = 5

        turno_actual = "Nakamura" if turno_actual == "Carlsen" else "Carlsen"

    if tiempo_carlsen <= 0 and tiempo_nakamura <= 0:
        print("\n¡La partida ha terminado en empate!")
    elif tiempo_carlsen <= 0:
        print("\n¡Hikaru Nakamura ha ganado la partida!")
    elif tiempo_nakamura <= 0:
        print("\n¡Magnus Carlsen ha ganado la partida!")

if __name__ == "__main__":
    iniciar_partida()
