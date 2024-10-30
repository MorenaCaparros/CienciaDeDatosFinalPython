class Jugador:
    def __init__(self, nombre, juego, eliminaciones, asistencias, muertes, dano_infligido, rondas_o_minutos):
        self.nombre = nombre
        self.juego = juego
        self.eliminaciones = eliminaciones
        self.asistencias = asistencias
        self.muertes = muertes
        self.dano_infligido = dano_infligido
        self.rondas_o_minutos = rondas_o_minutos
        self.kda = self.calcular_kda()

    def calcular_kda(self):
        return (self.eliminaciones + self.asistencias) / self.muertes if self.muertes != 0 else (self.eliminaciones + self.asistencias)

    def actualizar_estadisticas(self, eliminaciones, asistencias, muertes, dano_infligido):
        self.eliminaciones += eliminaciones
        self.asistencias += asistencias
        self.muertes += muertes
        self.dano_infligido += dano_infligido
        self.kda = self.calcular_kda()
