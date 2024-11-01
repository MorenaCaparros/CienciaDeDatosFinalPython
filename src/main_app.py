# Universidad Católica de Salta (UCASAL)
# Facultad de Ingeniería
# Licenciatura en Ciencia de Datos

# Proyecto Final: Calculadora de Rendimiento en League of Legends
# Estudiante: Morena Caparros

# Objetivo:
# Desarrollar una aplicación interactiva que funcione como calculadora y herramienta de análisis para 
# jugadores de League of Legends (LoL). El sistema permitirá a los usuarios ingresar sus estadísticas 
# personales y compararlas con las de los mejores jugadores de competencias globales. Además, ofrecerá 
# visualizaciones y análisis de datos para identificar fortalezas y áreas de mejora en el rendimiento del jugador.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from aplicacion.pantallas.menu import MenuScreen
from kivy.core.text import LabelBase
import aplicacion.ui_config  # Para aplicar los colores y fuentes
import os
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scatterlayout import ScatterLayout

from utils.visualizaciones import mostrar_graficos, mostrar_grafico_comparacion

class MainApp(App):
    def build(self):
        # Configuración de fondo de pantalla
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        # Layout principal para todo el contenido
        layout_principal = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Encabezado con título, logo y subtítulo
        encabezado = BoxLayout(orientation='vertical', size_hint=(1, 0.3), spacing=10)

        welcome_label = Label(
            text="Bienvenidos a [b]StatForge[/b]",
            font_name="EpicFont",
            font_size='40sp',
            color=aplicacion.ui_config.COLOR_DORADO,
            markup=True
        )
        subtitle_label = Label(
            text="La calculadora y gráfica de estadísticas que te compara con los mejores jugadores de LoL",
            font_name="EpicFont",
            font_size='16sp',
            color=aplicacion.ui_config.COLOR_GRIS,
            markup=True
        )

        # Añadir el título al encabezado
        encabezado.add_widget(welcome_label)

        # Logo
        logo_path = os.path.join(os.path.dirname(__file__), 'log.jpg')
        if os.path.exists(logo_path):
            logo = Image(source=logo_path, size_hint=(1, 1))
            encabezado.add_widget(logo)
        else:
            error_label = Label(
                text="Logo no encontrado. Verifica la ruta.",
                font_name="EpicFont",
                font_size='14sp',
                color=(1, 0, 0, 1)  # Color rojo para el mensaje de error
            )
            encabezado.add_widget(error_label)

        # Añadir el subtítulo al encabezado
        encabezado.add_widget(subtitle_label)

        # Añadir el encabezado al layout principal
        layout_principal.add_widget(encabezado)

        # Sección de menú para los botones, ocupa el espacio restante
        menu_seccion = BoxLayout(orientation='vertical', size_hint=(1, 0.5))
        menu_seccion.add_widget(MenuScreen())

        

        # Añadir la sección del menú al layout principal
        layout_principal.add_widget(menu_seccion)

        return layout_principal

if __name__ == '__main__':
    MainApp().run()
