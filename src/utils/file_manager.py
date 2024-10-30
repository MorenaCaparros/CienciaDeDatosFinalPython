import csv

def leer_jugadores_csv(filename):
    jugadores = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            jugador = Jugador(
                row['nombre'],
                row['juego'],
                int(row['eliminaciones']),
                int(row['asistencias']),
                int(row['muertes']),
                int(row['dano_infligido']),
                int(row['rondas_o_minutos'])
            )
            jugadores.append(jugador)
    return jugadores

def guardar_jugadores_csv(filename, jugadores):
    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ['nombre', 'juego', 'eliminaciones', 'asistencias', 'muertes', 'dano_infligido', 'rondas_o_minutos', 'kda']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for jugador in jugadores:
            writer.writerow({
                'nombre': jugador.nombre,
                'juego': jugador.juego,
                'eliminaciones': jugador.eliminaciones,
                'asistencias': jugador.asistencias,
                'muertes': jugador.muertes,
                'dano_infligido': jugador.dano_infligido,
                'rondas_o_minutos': jugador.rondas_o_minutos,
                'kda': jugador.kda
            })
