import csv

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
    return [jugador for jugador in jugadores if jugador['position'].upper() == posicion.upper()]

def obtener_mejores_jugadores(jugadores, metrica, top_n=5):
    jugadores_ordenados = sorted(jugadores, key=lambda x: x[metrica], reverse=True)
    return jugadores_ordenados[:top_n]

def listar_posiciones_disponibles(jugadores):
    posiciones = set(jugador['position'].upper() for jugador in jugadores)
    print("Posiciones disponibles en el dataset:", ", ".join(posiciones))
    return posiciones