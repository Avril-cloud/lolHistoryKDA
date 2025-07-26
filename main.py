from clases import player
from clases.partida import Partida
from clases.player import Player
from persistencia import guardar_datos, cargar_datos 

def registro_player():
    nick = input("Nickname: ")
    elo = input("Elo: ")
    player = Player(nick, elo)
    return player

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingresá un número válido.")

def registro_partida():
    campeon = input("Campeón usado: ")
    kill = pedir_entero("Número de Asesinatos: ")
    death = pedir_entero("Número de Muertes: ")
    assist = pedir_entero("Número de Assistencias: ")
    farm = pedir_entero("Cantidad de Minions: ")
    vision = pedir_entero("Puntuación de visión: ")
    partida = Partida(campeon, kill, death, assist, vision, farm)
    return partida



def agregar_partida(players):
    nickname = input("Nickname: ")
    nick = next((n for n in players if n.nick == nickname), None)
    if not nick:
        print("Player no encontrado.")
        return
    nueva_partida = registro_partida()
    nick.agregar_partida(nueva_partida)
    print("Partida registrada con éxito.")

def buscar_player(players):
    nickname = input("Nickname: ")
    nick = next((n for n in players if n.nick == nickname), None)
    if not nick:
        print("Player no encontrado.")
    return nick



def mostrar_menu():
    print("\n--- Estadisticas de Player ---")
    print("1. Registrar Player")
    print("2. Agregar Partida")
    print("3. Mostrar Historial")
    print("4. Mostrar Estadistica")
    print("5. Salir")

def main():


    players = cargar_datos("jugadores.json")

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue

        if opcion == 1:
            nick = registro_player()
            if nick:
                players.append(nick)
                print("Player registrado con éxito.")
        
        elif opcion == 2:
            agregar_partida(players)
        
        elif opcion == 3:
            nick = buscar_player(players)
            if nick:
                print(nick.resumen_historial())
        
        elif opcion == 4:
            nick = buscar_player(players)
            if nick:
                print(f"Promedio de KDA de {nick.nick}: {nick.promedio_kda():.2f}")
        
        elif opcion == 5:
            guardar_datos(players, "jugadores.json")
            print(
                "Saliendo del sistema."
            )
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()

