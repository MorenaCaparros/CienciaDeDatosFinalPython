from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup #ventanas emergentes para manejo de errores
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner  # Importa Spinner para el desplegable
import aplicacion.ui_config
from modelos.jugador import Jugador
from utils.gestor_archivos import leer_jugadores_csv, guardar_jugadores_csv

class IngresarEstadisticas(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Crear los campos de texto para ingresar las estadísticas
        self.nombre_input = TextInput(hint_text="Nombre del jugador")
        self.posicion_input = Spinner(
            text="Selecciona posición",  # Texto inicial del desplegable
            values=("MID", "JUNGLE", "TOP", "ADC", "SUPPORT"),  # Opciones disponibles
            size_hint=(1, None),
            height=44
        )

        # Crear los campos de texto para ingresar las estadísticas
        self.eliminaciones_input = TextInput(hint_text="Eliminaciones", input_filter='int')
        self.asistencias_input = TextInput(hint_text="Asistencias", input_filter='int')
        self.muertes_input = TextInput(hint_text="Muertes", input_filter='int')
        self.dano_input = TextInput(hint_text="Daño infligido", input_filter='int')
        self.minutos_input = TextInput(hint_text="Minutos jugados", input_filter='int')

        # Agregar campos al layout
        self.add_widget(self.nombre_input)
        self.add_widget(self.posicion_input)
        self.add_widget(self.eliminaciones_input)
        self.add_widget(self.asistencias_input)
        self.add_widget(self.muertes_input)
        self.add_widget(self.dano_input)
        self.add_widget(self.minutos_input)

        # Botón de guardar
        btn_guardar = Button(
            text="Guardar",
            background_normal='',
            background_color=(0.2, 0.2, 0.2, 1),
            color=aplicacion.ui_config.COLOR_DORADO,
            font_name="EpicFont"
        )
        btn_guardar.bind(on_press=self.guardar_estadisticas)
        self.add_widget(btn_guardar)
    
    def limpiar_campos(self):
        self.nombre_input.text = ""
        self.posicion_input.text = "Selecciona posición"  # Restablece al valor inicial del Spinner
        self.eliminaciones_input.text = ""
        self.asistencias_input.text = ""
        self.muertes_input.text = ""
        self.dano_input.text = ""
        self.minutos_input.text = ""

    def guardar_estadisticas(self, instance):
        try:
            # Verifica si los campos obligatorios están completos
            nombre = self.nombre_input.text.strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")

            posicion = self.posicion_input.text  # Toma el valor seleccionado del Spinner
            if posicion == "Selecciona posición":
                raise ValueError("Debe seleccionar una posición válida.")

            # Validar campos numéricos y mostrar mensaje si alguno está vacío o no es un número
            if not self.eliminaciones_input.text or not self.eliminaciones_input.text.isdigit():
                raise ValueError("Eliminaciones debe ser un número.")
            if not self.asistencias_input.text or not self.asistencias_input.text.isdigit():
                raise ValueError("Asistencias debe ser un número.")
            if not self.muertes_input.text or not self.muertes_input.text.isdigit():
                raise ValueError("Muertes debe ser un número.")
            if not self.dano_input.text or not self.dano_input.text.isdigit():
                raise ValueError("Daño infligido debe ser un número.")
            if not self.minutos_input.text or not self.minutos_input.text.isdigit():
                raise ValueError("Minutos jugados debe ser un número.")
            
            # Convertir los valores a enteros una vez validados
            eliminaciones = int(self.eliminaciones_input.text)
            asistencias = int(self.asistencias_input.text)
            muertes = int(self.muertes_input.text)
            dano_infligido = int(self.dano_input.text)
            minutos_jugados = int(self.minutos_input.text)

            # Crear el objeto Jugador y guardar
            jugador = Jugador(nombre, posicion, eliminaciones, asistencias, muertes, dano_infligido, minutos_jugados)
            jugadores = leer_jugadores_csv('./data/jugadores_esports.csv')
            jugadores.append(jugador)
            guardar_jugadores_csv('./data/jugadores_esports.csv', jugadores)

            # Confirmación de guardado y cerrar solo el popup
            self.mostrar_popup("Estadísticas guardadas exitosamente.", tipo="info", cerrar_despues=True)

            self.limpiar_campos()

        except ValueError as e:
            self.mostrar_popup(f"Error: {str(e)}", tipo="error")
        except Exception as e:
            self.mostrar_popup(f"Error inesperado: {str(e)}", tipo="error")
                                
    def mostrar_popup(self, mensaje, tipo="info", cerrar_despues=False,popup_formulario=None):
        color = (1, 0, 0, 1) if tipo == "error" else (0.8, 0.8, 0.8, 1)
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text=mensaje, font_name="EpicFont", color=color))
        
        mensaje_popup = Popup(title="Mensaje", content=popup_content, size_hint=(0.7, 0.4), title_align='center')
        
        if cerrar_despues and popup_formulario:
            mensaje_popup.bind(on_dismiss=popup_formulario.dismiss)  # Cierra el popup principal después del mensaje
        
        mensaje_popup.open()




