
import matplotlib.pyplot as plt
from collections import defaultdict
from utils.analisis import filtrar_por_posicion, obtener_mejores_jugadores

def graficar_dano_promedio_por_posicion(jugadores):
    # Calcular daño promedio por posición
    danos_por_posicion = defaultdict(list)
    for jugador in jugadores:
        danos_por_posicion[jugador['position']].append(jugador['damage_per_minute'])
    
    posiciones = []
    promedios_dano = []
    
    for posicion, danos in danos_por_posicion.items():
        posiciones.append(posicion)
        promedios_dano.append(sum(danos) / len(danos))
    
    # Graficar
    plt.figure(figsize=(10, 6))
    plt.bar(posiciones, promedios_dano, color='skyblue')
    plt.title('Daño Promedio por Minuto por Posición')
    plt.xlabel('Posición')
    plt.ylabel('Daño Promedio por Minuto')
    plt.show()

def comparar_estadisticas_jugador(jugador, jugadores_posicion):
    # Obtener los mejores jugadores en la misma posición
    mejores_jugadores = obtener_mejores_jugadores(jugadores_posicion, 'damage_per_minute', top_n=5)
    
    # Estadísticas a comparar
    labels = ['Eliminaciones', 'Asistencias', 'Muertes', 'Daño por Minuto']
    jugador_stats = [
        jugador.eliminaciones,
        jugador.asistencias,
        jugador.muertes,
        jugador.dano_infligido / jugador.minutos_jugados
    ]
    
    # Promedios de los mejores jugadores
    promedios_mejores = [
        sum(j['kills'] for j in mejores_jugadores) / len(mejores_jugadores),
        sum(j['assists'] for j in mejores_jugadores) / len(mejores_jugadores),
        sum(j['deaths'] for j in mejores_jugadores) / len(mejores_jugadores),
        sum(j['damage_per_minute'] for j in mejores_jugadores) / len(mejores_jugadores)
    ]
    
    # Graficar comparativa
    x = range(len(labels))
    plt.figure(figsize=(10, 6))
    plt.bar(x, jugador_stats, width=0.4, label='Tus Estadísticas', color='green', align='center')
    plt.bar([i + 0.4 for i in x], promedios_mejores, width=0.4, label='Promedio Top 5', color='blue', align='center')
    plt.xticks([i + 0.2 for i in x], labels)
    plt.title(f'Comparación de Estadísticas en {jugador.posicion}')
    plt.xlabel('Estadísticas')
    plt.ylabel('Valores')
    plt.legend()
    plt.show()