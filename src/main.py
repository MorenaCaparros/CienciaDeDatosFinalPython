from utils.file_manager import leer_jugadores_csv, guardar_jugadores_csv
from utils.visualizations import graficar_estadisticas
from models.jugador import Jugador

def main():
    jugadores = leer_jugadores_csv('./data/jugadores_esports.csv')

    while True:
        opcion = input("¿Qué necesitas hacer? (1: Ingresar estadísticas, 2: Ver estadísticas, 3: Salir): ")
        
        if opcion == '1':
            nombre = input("Nombre del jugador: ").strip()
            juego = input("Juego (LoL, Valorant, CS): ").lower().strip()
            eliminaciones = int(input("Eliminaciones: "))
            asistencias = int(input("Asistencias: "))
            muertes = int(input("Muertes: "))
            dano_infligido = int(input("Daño infligido: "))
            rondas_o_minutos = int(input("Rondas ganadas o minutos jugados: "))
            
            nuevo_jugador = Jugador(nombre, juego, eliminaciones, asistencias, muertes, dano_infligido, rondas_o_minutos)
            jugadores.append(nuevo_jugador)
            guardar_jugadores_csv('./data/jugadores_esports.csv', jugadores)
        
        elif opcion == '2':
            graficar_estadisticas(jugadores)
        
        elif opcion == '3':
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == '__main__':
    main()
