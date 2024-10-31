from utils.gestor_archivos import leer_jugadores_csv, guardar_jugadores_csv
from utils.visualizaciones import graficar_dano_promedio_por_posicion, comparar_estadisticas_jugador
from modelos.jugador import Jugador
from utils.analisis import leer_dataset_jugadores, filtrar_por_posicion, obtener_mejores_jugadores, listar_posiciones_disponibles
from utils.ayudantes_entrada import obtener_posicion_estandarizada, obtener_estadisticas_jugador
import difflib

def ingresar_estadisticas():
    nombre, posicion_estandarizada, eliminaciones, asistencias, muertes, dano_infligido, minutos_jugados = obtener_estadisticas_jugador()
    if not posicion_estandarizada:
        print("Posición no válida. Intenta nuevamente.")
        return

    nuevo_jugador = Jugador(
        nombre=nombre,
        posicion=posicion_estandarizada,
        eliminaciones=eliminaciones,
        asistencias=asistencias,
        muertes=muertes,
        dano_infligido=dano_infligido,
        minutos_jugados=minutos_jugados
    )

    jugadores = leer_jugadores_csv('./data/jugadores_esports.csv')
    jugadores.append(nuevo_jugador)
    guardar_jugadores_csv('./data/jugadores_esports.csv', jugadores)
    print(f"Estadísticas de {nombre} guardadas exitosamente.")

def ver_mejores_jugadores_por_posicion():
    jugadores = leer_dataset_jugadores('./data/dataset_Mundial_2022/wc_players_main.csv')
    
    if not jugadores:
        print("No se encontraron jugadores en el dataset. Asegúrate de que el archivo exista y tenga datos.")
        return

    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Ver posiciones disponibles")
        print("2. Seleccionar una posición para ver los mejores jugadores")
        print("3. Volver al menú principal")
        
        opcion = input("Elige una opción: ").strip().lower()

        if opcion == '1':
            posiciones = listar_posiciones_disponibles(jugadores)
            if posiciones:
                print("\nPosiciones disponibles en el dataset:", ", ".join(posiciones))
            else:
                print("No se encontraron posiciones en el dataset.")
        
        elif opcion == '2':
            posicion = input("¿Qué posición quieres ver? (MID, JUNGLE, TOP, ADC, SUPPORT): ").strip()
            posicion_estandarizada = obtener_posicion_estandarizada(posicion)
            if not posicion_estandarizada:
                print("Posición no válida. Intenta nuevamente.")
                continue
            
            jugadores_posicion = filtrar_por_posicion(jugadores, posicion_estandarizada)
            
            if not jugadores_posicion:
                print(f"No se encontraron jugadores en la posición {posicion_estandarizada}.")
            else:
                mejores_jugadores = obtener_mejores_jugadores(jugadores_posicion, 'damage_per_minute', top_n=5)
                print("\nMejores jugadores por daño por minuto:")
                for jugador in mejores_jugadores:
                    print(f"Jugador: {jugador['player']}, Equipo: {jugador['team']}, Daño por minuto: {jugador['damage_per_minute']}")
        
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def ver_estadisticas():
    jugadores = leer_dataset_jugadores('./data/dataset_Mundial_2022/wc_players_main.csv')
    graficar_dano_promedio_por_posicion(jugadores)

def comparar_estadisticas():
    jugadores = leer_dataset_jugadores('./data/dataset_Mundial_2022/wc_players_main.csv')
    posicion = input("Posición en la que juegas (MID, JUNGLE, TOP, ADC, SUPPORT): ").strip()
    posicion_estandarizada = obtener_posicion_estandarizada(posicion)
    if not posicion_estandarizada:
        print("Posición no válida. Intenta nuevamente.")
        return

    jugadores_posicion = filtrar_por_posicion(jugadores, posicion_estandarizada)

    if not jugadores_posicion:
        print(f"No se encontraron jugadores en la posición {posicion_estandarizada}.")
        return

    nombre, _, eliminaciones, asistencias, muertes, dano_infligido, minutos_jugados = obtener_estadisticas_jugador()
    jugador = Jugador(nombre, posicion_estandarizada, eliminaciones, asistencias, muertes, dano_infligido, minutos_jugados)
    comparar_estadisticas_jugador(jugador, jugadores_posicion)

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("Elige una opción:")
        print("1. Ingresar tus estadísticas")
        print("2. Ver mejores jugadores")
        print("3. Comparar tus estadísticas")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            ingresar_estadisticas()
        elif opcion == '2':
            ver_mejores_jugadores_por_posicion()
        elif opcion == '3':
            comparar_estadisticas()
        elif opcion == '4':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
            
if __name__ == '__main__':
    main()
