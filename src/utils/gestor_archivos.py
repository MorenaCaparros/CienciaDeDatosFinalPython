import csv
from modelos.jugador import Jugador

def leer_jugadores_csv(filepath):
    jugadores = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            jugador = Jugador(
                nombre=row['nombre'],
                posicion=row['posicion'],
                eliminaciones=int(row['eliminaciones']),
                asistencias=int(row['asistencias']),
                muertes=int(row['muertes']),
                dano_infligido=int(row['dano_infligido']),
                minutos_jugados=int(row['minutos_jugados'])
            )
            jugadores.append(jugador)
    return jugadores

def guardar_jugadores_csv(filepath, jugadores):
    with open(filepath, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ['nombre', 'posicion', 'eliminaciones', 'asistencias', 'muertes', 'dano_infligido', 'minutos_jugados']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for jugador in jugadores:
            writer.writerow({
                'nombre': jugador.nombre,
                'posicion': jugador.posicion,
                'eliminaciones': jugador.eliminaciones,
                'asistencias': jugador.asistencias,
                'muertes': jugador.muertes,
                'dano_infligido': jugador.dano_infligido,
                'minutos_jugados': jugador.minutos_jugados
            })
