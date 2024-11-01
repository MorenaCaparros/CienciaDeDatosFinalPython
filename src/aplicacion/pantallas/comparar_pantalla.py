from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from modelos.jugador import Jugador
from utils.visualizaciones import mostrar_grafico_comparacion
from utils.analisis import leer_dataset_jugadores, filtrar_por_posicion, comparar_estadisticas_jugador
from utils.ayudantes_entrada import obtener_posicion_estandarizada
import aplicacion.ui_config  # Importar configuración visual
import logging

# Configuración del logger
logging.basicConfig(filename='app_log.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Comparar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Título
        titulo_label = Label(
            text="Comparar Estadísticas",
            font_name="EpicFont",
            font_size='24sp',
            color=aplicacion.ui_config.COLOR_DORADO,
            markup=True
        )
        self.add_widget(titulo_label)

        # Selector de posición
        self.posicion_input = Spinner(
            text="Seleccionar posición",
            values=("MID", "JUNGLE", "TOP", "ADC", "SUPPORT"),
            size_hint=(1, None),
            height=40  # Ajusta esta altura si es necesario
        )
        self.add_widget(self.posicion_input)

        self.nombre_input = TextInput(hint_text="Tu nombre")
        self.eliminaciones_input = TextInput(hint_text="Tus eliminaciones", input_filter='int')
        self.asistencias_input = TextInput(hint_text="Tus asistencias", input_filter='int')
        self.muertes_input = TextInput(hint_text="Tus muertes", input_filter='int')
        self.dano_input = TextInput(hint_text="Tu daño total infligido", input_filter='int')
        self.minutos_input = TextInput(hint_text="Tus minutos jugados", input_filter='int')

        # Añadir los campos al layout
        for widget in [self.nombre_input, self.eliminaciones_input, self.asistencias_input, self.muertes_input, self.dano_input, self.minutos_input]:
            self.add_widget(widget)

        # Botón de comparar
        btn_comparar = Button(
            text="Comparar",
            background_normal='',
            background_color=(0.2, 0.2, 0.2, 1),
            color=aplicacion.ui_config.COLOR_DORADO,
            font_name="EpicFont"
        )
        btn_comparar.bind(on_press=self.realizar_comparacion)
        self.add_widget(btn_comparar)

        # Botón de cerrar
        btn_cerrar = Button(
            text="Cerrar",
            background_normal='',
            background_color=(0.5, 0.1, 0.1, 1),
            color=(1, 1, 1, 1),
            font_name="EpicFont"
        )
        btn_cerrar.bind(on_press=self.cerrar_pantalla)
        self.add_widget(btn_cerrar)

    # def estandarizar_posicion(self, posicion):
    
    #     posiciones_estandar = {
    #         "MID": "MIDDLE",
    #         "MIDDLE": "MIDDLE",
    #         "JUNGLE": "JUNGLE",
    #         "TOP": "TOP",
    #         "ADC": "ADC",
    #         "SUPPORT": "SUPPORT"
    #     }
    #     return posiciones_estandar.get(posicion.upper())


    def realizar_comparacion(self, instance):
        logging.debug("Ejecutando realizar_comparacion")
        try:
            posicion = self.posicion_input.text
            logging.debug(f"[Posición seleccionada] {posicion}")
            posicion_estandarizada = obtener_posicion_estandarizada(posicion)
            logging.debug(f"[Posición estandarizada] {posicion_estandarizada}")
            
            if not posicion_estandarizada:
                self.mostrar_popup("Debe seleccionar una posición válida.", tipo="error")
                return

            jugadores = leer_dataset_jugadores('./data/dataset_Mundial_2022/wc_players_main.csv')
            logging.debug(f"[Jugadores cargados] {len(jugadores)}")

            jugadores_posicion = filtrar_por_posicion(jugadores, posicion_estandarizada)
            logging.debug(f"[Jugadores en la posición] {len(jugadores_posicion)}")

            if not jugadores_posicion:
                self.mostrar_popup(f"No se encontraron jugadores en la posición {posicion_estandarizada}.", tipo="error")
                return

            nombre = self.nombre_input.text.strip()
            eliminaciones = int(self.eliminaciones_input.text)
            asistencias = int(self.asistencias_input.text)
            muertes = int(self.muertes_input.text)
            dano_infligido = int(self.dano_input.text)
            minutos_jugados = int(self.minutos_input.text)

            jugador = Jugador(nombre, posicion_estandarizada, eliminaciones, asistencias, muertes, dano_infligido, minutos_jugados)
            logging.debug(f"[Jugador creado] {jugador}")
           
            resultado, promedio_eliminaciones, promedio_asistencias, promedio_muertes, promedio_dano, promedio_kda = comparar_estadisticas_jugador(jugador, jugadores_posicion)

            self.mostrar_popup("Comparación realizada exitosamente.", tipo="info")
            # Llamar a la función del gráfico
            mostrar_grafico_comparacion(jugador, promedio_eliminaciones, promedio_asistencias, promedio_muertes, promedio_dano, promedio_kda)
        
        except ValueError as e:
            logging.error(f"Error de valor: {e}")
            self.mostrar_popup(f"Error: {str(e)}", tipo="error")
        except Exception as e:
            logging.error(f"Error inesperado: {e}")
            self.mostrar_popup(f"Error inesperado: {str(e)}", tipo="error")

    def mostrar_popup(self, mensaje, tipo="info"):
        color = (1, 0, 0, 1) if tipo == "error" else (0.8, 0.8, 0.8, 1)
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text=mensaje, font_size='18sp', color=color))

        self.popup_instance = Popup(title="Mensaje", content=popup_content, size_hint=(0.7, 0.4), title_align='center')
        self.popup_instance.open()

    def cerrar_pantalla(self, instance):
        if hasattr(self, 'popup_instance'):
            self.popup_instance.dismiss()