import csv
from utils.ayudantes_entrada import obtener_posicion_estandarizada


def leer_dataset_jugadores(filepath):
    jugadores = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convertir valores numéricos
            row['kills'] = int(row['kills'])
            row['deaths'] = int(row['deaths'])
            row['assists'] = int(row['assists'])
            row['damage_per_minute'] = float(row['damage_per_minute'])
            row['kda'] = float(row['kda'])
            jugadores.append(row)
    return jugadores

def filtrar_por_posicion(jugadores, posicion):
    posicion_estandarizada = obtener_posicion_estandarizada(posicion)
    if not posicion_estandarizada:
        return []
    return [jugador for jugador in jugadores if jugador['position'].upper() == posicion_estandarizada]


def obtener_mejores_jugadores(jugadores, metrica, top_n=5):
    jugadores_ordenados = sorted(jugadores, key=lambda x: x[metrica], reverse=True)
    return jugadores_ordenados[:top_n]

def listar_posiciones_disponibles(jugadores):
    posiciones = set(jugador['position'].upper() for jugador in jugadores)
    print("Posiciones disponibles en el dataset:", ", ".join(posiciones))
    return posiciones

def comparar_estadisticas_jugador(jugador, jugadores_posicion):
    """
    Compara las estadísticas del jugador del usuario con el promedio de los jugadores de la posición seleccionada.
    Devuelve una cadena con el resultado de la comparación.
    """
    # Calcular promedios de los jugadores en la posición seleccionada
    total_eliminaciones = sum(j['kills'] for j in jugadores_posicion)
    total_asistencias = sum(j['assists'] for j in jugadores_posicion)
    total_muertes = sum(j['deaths'] for j in jugadores_posicion)
    total_dano = sum(j['damage_per_minute'] for j in jugadores_posicion)
    total_kda = sum(j['kda'] for j in jugadores_posicion)
    
    promedio_eliminaciones = total_eliminaciones / len(jugadores_posicion)
    promedio_asistencias = total_asistencias / len(jugadores_posicion)
    promedio_muertes = total_muertes / len(jugadores_posicion)
    promedio_dano = total_dano / len(jugadores_posicion)
    promedio_kda = total_kda / len(jugadores_posicion)

    # Crear un mensaje de comparación
    resultado = (
        f"Comparación de estadísticas para {jugador.nombre}:\n\n"
        f"Tus eliminaciones: {jugador.eliminaciones} | Promedio en tu posición: {promedio_eliminaciones:.2f}\n"
        f"Tus asistencias: {jugador.asistencias} | Promedio en tu posición: {promedio_asistencias:.2f}\n"
        f"Tus muertes: {jugador.muertes} | Promedio en tu posición: {promedio_muertes:.2f}\n"
        f"Tu daño por minuto: {jugador.dano_infligido / jugador.minutos_jugados:.2f} | Promedio en tu posición: {promedio_dano:.2f}\n"
        f"Tu KDA: {jugador.kda} | Promedio en tu posición: {promedio_kda:.2f}\n"
    )

    return resultado, promedio_eliminaciones, promedio_asistencias, promedio_muertes, promedio_dano, promedio_kda



