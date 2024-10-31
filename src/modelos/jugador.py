class Jugador:
    def __init__(self, nombre, posicion, eliminaciones, asistencias, muertes, dano_infligido, minutos_jugados):
        self.nombre = nombre
        self.posicion = posicion
        self.eliminaciones = eliminaciones
        self.asistencias = asistencias
        self.muertes = muertes
        self.dano_infligido = dano_infligido
        self.minutos_jugados = minutos_jugados
        
    def __dict__(self):
            return {
                'nombre': self.nombre,
                'posicion': self.posicion,
                'eliminaciones': self.eliminaciones,
                'asistencias': self.asistencias,
                'muertes': self.muertes,
                'dano_infligido': self.dano_infligido,
                'minutos_jugados': self.minutos_jugados
            }