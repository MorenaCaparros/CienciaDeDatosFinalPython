import difflib

POSICIONES_VALIDAS = {
    "MID": "MIDDLE",
    "JUNGLE": "JUNGLE",
    "TOP": "TOP",
    "ADC": "ADC",
    "SUPPORT": "SUPPORT"
}

def obtener_posicion_estandarizada(entrada):
    """
    Devuelve la posición estándar para el dataset basada en la entrada del usuario.
    """
    entrada = entrada.upper()
    coincidencias = difflib.get_close_matches(entrada, POSICIONES_VALIDAS.keys(), n=1, cutoff=0.6)
    if coincidencias:
        return POSICIONES_VALIDAS[coincidencias[0]]
    return None

def obtener_estadisticas_jugador():
    nombre = input("Nombre del jugador: ").strip()
    posicion = input("Posición (MID, JUNGLE, TOP, ADC, SUPPORT): ").strip()
    posicion_estandarizada = obtener_posicion_estandarizada(posicion)
    eliminaciones = int(input("Eliminaciones: "))
    asistencias = int(input("Asistencias: "))
    muertes = int(input("Muertes: "))
    dano_infligido = int(input("Daño infligido: "))
    minutos_jugados = int(input("Minutos jugados: "))
    return nombre, posicion_estandarizada, eliminaciones, asistencias, muertes, dano_infligido, minutos_jugados
