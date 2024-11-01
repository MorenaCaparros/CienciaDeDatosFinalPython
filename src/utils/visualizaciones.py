from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import pandas as pd
from modelos.jugador import Jugador
import os

def mostrar_graficos(instance):
    # Crear una ventana emergente para mostrar los gráficos
    popup_layout = ScatterLayout()
    popup = Popup(title='Comparación de Jugadores', content=popup_layout, size_hint=(0.9, 0.9))

    # Cargar datos del dataset
    dataset_path = os.path.join(os.path.dirname(__file__), 'dataset.csv')
    if os.path.exists(dataset_path):
        df = pd.read_csv(dataset_path)
        fig, ax = plt.subplots()
        df.plot(ax=ax)
        canvas = FigureCanvasKivyAgg(fig)
        popup_layout.add_widget(canvas)
    else:
        error_label = Label(
            text="Dataset no encontrado. Verifica la ruta.",
            font_name="EpicFont",
            font_size='14sp',
            color=(1, 0, 0, 1)  # Color rojo para el mensaje de error
        )
        popup_layout.add_widget(error_label)

    popup.open()




def mostrar_grafico_comparacion(jugador, promedio_eliminaciones, promedio_asistencias, promedio_muertes, promedio_dano, promedio_kda):
    fig, ax = plt.subplots(figsize=(8, 6))

    # Datos para el gráfico
    etiquetas = ["Eliminaciones", "Asistencias", "Muertes", "Daño por Minuto", "KDA"]
    valores_jugador = [
        jugador.eliminaciones,
        jugador.asistencias,
        jugador.muertes,
        jugador.dano_infligido / jugador.minutos_jugados,
        jugador.kda
    ]
    valores_promedio = [
        promedio_eliminaciones,
        promedio_asistencias,
        promedio_muertes,
        promedio_dano,
        promedio_kda
    ]

    # Crear gráfico de barras
    ancho_barra = 0.35
    ax.barh(etiquetas, valores_jugador, height=ancho_barra, label="Jugador", color="skyblue")
    ax.barh([label + " " for label in etiquetas], valores_promedio, height=ancho_barra, label="Promedio", color="orange")

    ax.set_xlabel("Valores")
    ax.set_title("Comparación de Estadísticas del Jugador vs Promedio")
    ax.legend()

    # Mostrar el gráfico en una ventana de matplotlib
    plt.show()
