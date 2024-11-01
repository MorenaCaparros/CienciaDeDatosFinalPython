from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from aplicacion.pantallas.ingresar_estadisticas_pantalla import IngresarEstadisticas
from aplicacion.pantallas.ver_mejores_pantalla import VerMejores
from aplicacion.pantallas.comparar_pantalla import Comparar
from kivy.uix.popup import Popup
import aplicacion.ui_config  # Importar configuración visual

class MenuScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        # Configuración común para los botones
        button_config = {
            "size_hint_y": None,
            "height": 60,  # Ajuste de altura para hacer los botones más grandes
            "background_normal": '',
            "background_color": (0.2, 0.2, 0.2, 1),
            "color": aplicacion.ui_config.COLOR_DORADO,
            "font_name": "EpicFont",
            "font_size": '18sp'  # Tamaño de texto en los botones
        }


        btn_ingresar = Button(text="Ingresar tus estadísticas", **button_config)
        btn_ingresar.bind(on_press=self.ingresar_estadisticas)
        self.add_widget(btn_ingresar)

        btn_ver_mejores = Button(text="Ver mejores jugadores", **button_config)
        btn_ver_mejores.bind(on_press=self.ver_mejores_jugadores)
        self.add_widget(btn_ver_mejores)

        btn_comparar = Button(text="Comparar tus estadísticas", **button_config)
        btn_comparar.bind(on_press=self.comparar_estadisticas)
        self.add_widget(btn_comparar)

       

        btn_salir = Button(
            text="Salir",
            size_hint_y=None,
            height=60,
            background_normal='',
            background_color=(0.5, 0.1, 0.1, 1),
            color=(1, 1, 1, 1),
            font_name="EpicFont",
            font_size='18sp'
        )
        btn_salir.bind(on_press=self.salir)
        self.add_widget(btn_salir)

    def ingresar_estadisticas(self, instance):
        self.popup = Popup(title="Ingresar Estadísticas", content=IngresarEstadisticas(), size_hint=(0.9, 0.9))
        self.popup.open()

    def ver_mejores_jugadores(self, instance):
        # Crea el popup y su contenido
        self.popup = Popup(title="Ver Mejores Jugadores", size_hint=(0.9, 0.9))
        ver_mejores = VerMejores()  # No pasar popup aquí
        self.popup.content = ver_mejores
        self.popup.open()
        ver_mejores.popup_instance = self.popup  # Pasa la instancia del popup para que pueda cerrarlo si es necesario



    def comparar_estadisticas(self, instance):
        self.popup = Popup(title="Comparar Estadísticas", content=Comparar(), size_hint=(0.9, 0.9))
        self.popup.open()

    def salir(self, instance):
        App.get_running_app().stop()
