import matplotlib.pyplot as plt

def graficar_estadisticas(jugadores):
    nombres = [jugador.nombre for jugador in jugadores]
    kdas = [jugador.kda for jugador in jugadores]
    danos = [jugador.dano_infligido for jugador in jugadores]
    
    plt.figure()
    
    plt.subplot(2, 1, 1)
    plt.bar(nombres, kdas, color='skyblue')
    plt.title('KDA por Jugador')
    plt.ylabel('KDA')

    plt.subplot(2, 1, 2)
    plt.bar(nombres, danos, color='orange')
    plt.title('Daño infligido por Jugador')
    plt.ylabel('Daño infligido')

    plt.tight_layout()
    plt.show()
