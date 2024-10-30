def calcular_crecimiento(actual, anterior):
    return (actual - anterior) / anterior * 100 if anterior != 0 else 0
