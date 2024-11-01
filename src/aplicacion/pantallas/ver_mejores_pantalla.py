from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from utils.analisis import leer_dataset_jugadores, filtrar_por_posicion, obtener_mejores_jugadores
import aplicacion.ui_config
from aplicacion.ui_config import COLOR_DORADO, COLOR_GRIS
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import os
import plotly.graph_objects as go

COLOR_DORADO_HEX = '#FFD700'  # Dorado en hexadecimal
COLOR_GRIS_HEX = 'rgba(204, 204, 204, 1)'  # Gris claro en formato rgba

class VerMejores(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Título
        self.add_widget(Label(
            text="Ver Mejores Jugadores",
            font_name="EpicFont",
            font_size='24sp',
            color=aplicacion.ui_config.COLOR_DORADO
        ))

        # Dropdown para elegir la posición
        self.posicion_spinner = Spinner(
            text="Seleccionar posición",
            values=("MID", "JUNGLE", "TOP", "ADC", "SUPPORT"),
            size_hint=(1, None),
            height=44
        )
        self.posicion_spinner.bind(text=self.mostrar_mejores_jugadores)
        self.add_widget(self.posicion_spinner)

         # Aquí creamos el botón para mostrar los gráficos de los jugadores
        btn_mostrar_graficos = Button(
            text="Ver Gráficos de Jugadores",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 0, 1),
            font_name="EpicFont"
        )
        btn_mostrar_graficos.bind(on_press=self.mostrar_graficos)
        self.add_widget(btn_mostrar_graficos)

        # Contenedor para mostrar resultados
        self.resultado_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.7))
        self.add_widget(self.resultado_layout)

        # Botón para cerrar la pantalla
        btn_cerrar = Button(
            text="Cerrar",
            background_normal='',
            background_color=(0.5, 0.1, 0.1, 1),
            color=(1, 1, 1, 1),
            font_name="EpicFont",
            size_hint=(1, 0.2)
        )
        btn_cerrar.bind(on_press=self.cerrar_pantalla)
        self.add_widget(btn_cerrar)

    def mostrar_mejores_jugadores(self, spinner, text):
        # Limpiar el contenedor de resultados
        self.resultado_layout.clear_widgets()

        # Leer el dataset de jugadores
        jugadores = leer_dataset_jugadores('./data/dataset_Mundial_2022/wc_players_main.csv')

        # Filtrar por la posición seleccionada
        posicion = text
        jugadores_posicion = filtrar_por_posicion(jugadores, posicion)

        if not jugadores_posicion:
            self.resultado_layout.add_widget(Label(text=f"No se encontraron jugadores en la posición {posicion}."))
            return

        # Obtener los mejores jugadores
        mejores_jugadores = obtener_mejores_jugadores(jugadores_posicion, 'damage_per_minute', top_n=5)

        # Guardar los mejores jugadores para graficar
        self.mejores_jugadores = mejores_jugadores

        # Mostrar los resultados en la interfaz
        for jugador in mejores_jugadores:
            jugador_info = f"Jugador: {jugador['player']}, Equipo: {jugador['team']}, Daño por minuto: {jugador['damage_per_minute']}"
            self.resultado_layout.add_widget(Label(text=jugador_info))
        
    def mostrar_graficos(self, instance):
       # Verifica si ya hay una lista de jugadores para graficar
        if not hasattr(self, 'mejores_jugadores') or not self.mejores_jugadores:
            self.resultado_layout.add_widget(Label(text="Selecciona una posición primero para ver los gráficos."))
            return

        # Datos para el gráfico
        nombres = [jugador['player'] for jugador in self.mejores_jugadores]
        danos = [jugador['damage_per_minute'] for jugador in self.mejores_jugadores]

        # Crear gráfico de barras en matplotlib
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.barh(nombres, danos, color=COLOR_DORADO)
        ax.set_xlabel("Daño por Minuto", color=COLOR_GRIS)
        ax.set_title("Top 5 Jugadores - Daño por Minuto", color=COLOR_GRIS)
        ax.invert_yaxis()  # Para que el mejor jugador esté en la parte superior

        # Personalización del gráfico
        ax.spines['top'].set_color(COLOR_GRIS)
        ax.spines['right'].set_color(COLOR_GRIS)
        ax.spines['bottom'].set_color(COLOR_GRIS)
        ax.spines['left'].set_color(COLOR_GRIS)
        ax.tick_params(axis='x', colors=COLOR_GRIS)
        ax.tick_params(axis='y', colors=COLOR_GRIS)
        ax.xaxis.label.set_color(COLOR_GRIS)
        ax.yaxis.label.set_color(COLOR_GRIS)

        # Mostrar el gráfico en una ventana emergente de matplotlib
        plt.show()
    def cerrar_pantalla(self, instance):
        if hasattr(self, 'popup_instance'):
            self.popup_instance.dismiss()  # Cierra el popup solo si existe `popup_instance`