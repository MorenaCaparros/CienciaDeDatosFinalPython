from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from utils.gestor_archivos import leer_jugadores_csv, guardar_jugadores_csv
from utils.visualizaciones import graficar_dano_promedio_por_posicion, comparar_estadisticas_jugador
from modelos.jugador import Jugador
from utils.analisis import leer_dataset_jugadores, filtrar_por_posicion, obtener_mejores_jugadores, listar_posiciones_disponibles
from utils.ayudantes_entrada import obtener_posicion_estandarizada, obtener_estadisticas_jugador

class MainApp(App):
    def build(self):
        self.title = "Estadísticas de Jugadores"
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="--- Menú Principal ---")
        layout.add_widget(self.label)

        btn_ingresar = Button(text="Ingresar tus estadísticas")
        btn_ingresar.bind(on_press=self.ingresar_estadisticas)
        layout.add_widget(btn_ingresar)

        btn_ver_mejores = Button(text="Ver mejores jugadores")
        btn_ver_mejores.bind(on_press=self.ver_mejores_jugadores)
        layout.add_widget(btn_ver_mejores)

        btn_comparar = Button(text="Comparar tus estadísticas")
        btn_comparar.bind(on_press=self.comparar_estadisticas)
        layout.add_widget(btn_comparar)

        btn_salir = Button(text="Salir")
        btn_salir.bind(on_press=self.salir)
        layout.add_widget(btn_salir)

        return layout

    def ingresar_estadisticas(self, instance):
        content = BoxLayout(orientation='vertical')
        self.nombre_input = TextInput(hint_text="Nombre del jugador")
        self.posicion_input = TextInput(hint_text="Posición (MID, JUNGLE, TOP, ADC, SUPPORT)")
        self.eliminaciones_input = TextInput(hint_text="Eliminaciones", input_filter='int')
        self.asistencias_input = TextInput(hint_text="Asistencias", input_filter='int')
        self.muertes_input = TextInput(hint_text="Muertes", input_filter='int')
        self.dano_input = TextInput(hint_text="Daño infligido", input_filter='int')
        self.minutos_input = TextInput(hint_text="Minutos jugados", input_filter='int')

        content.add_widget(self.nombre_input)
        content.add_widget(self.posicion_input)
        content.add_widget(self.eliminaciones_input)
        content.add_widget(self.asistencias_input)
        content.add_widget(self.muertes_input)
        content.add_widget(self.dano_input)
        content.add_widget(self.minutos_input)

        btn_guardar = Button(text="Guardar")
        btn_guardar.bind(on_press=self.guardar_estadisticas)
        content.add_widget(btn_guardar)

        self.popup = Popup(title="Ingresar Estadísticas", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def guardar_estadisticas(self, instance):
        nombre = self.nombre_input.text.strip()
        posicion = self.posicion_input.text.strip()
        posicion_estandarizada = obtener_posicion_estandarizada(posicion)
        if not posicion_estandarizada:
            self.popup.dismiss()
            self.mostrar_popup("Posición no válida. Intenta nuevamente.")
            return

        eliminaciones = int(self.eliminaciones_input.text)
        asistencias = int(self.asistencias_input.text)
        muertes = int(self.muertes_input.text)
        dano_infligido = int(self.dano_input.text)
        minutos_jugados = int(self.minutos_input.text)

        nuevo_jugador = Jugador(
            nombre=nombre,
            posicion=posicion_estandarizada,
            eliminaciones=eliminaciones,
            asistencias=asistencias,
            muertes=muertes,
            dano_infligido=dano_infligido,
            minutos_jugados=minutos_jugados
        )

        jugadores = leer_jugadores_csv('./data/jugadores_esports.csv')
        jugadores.append(nuevo_jugador)
        guardar_jugadores_csv('./data/jugadores_esports.csv', jugadores)
        self.popup.dismiss()
        self.mostrar_popup(f"Estadísticas de {nombre} guardadas exitosamente.")

    def ver_mejores_jugadores(self, instance):
        jugadores = leer_dataset_jugadores('./data/dataset_Mundial_2022/wc_players_main.csv')
        if not jugadores:
            self.mostrar_popup("No se encontraron jugadores en el dataset. Asegúrate de que el archivo exista y tenga datos.")
            return

        posiciones = listar_posiciones_disponibles(jugadores)
        self.mostrar_popup(f"Posiciones disponibles en el dataset: {', '.join(posiciones)}")

    def comparar_estadisticas(self, instance):
        jugadores = leer_dataset_jugadores('./data/dataset_Mundial_2022/wc_players_main.csv')
        if not jugadores:
            self.mostrar_popup("No se encontraron jugadores en el dataset. Asegúrate de que el archivo exista y tenga datos.")
            return

        content = BoxLayout(orientation='vertical')
        self.posicion_input = TextInput(hint_text="Posición (MID, JUNGLE, TOP, ADC, SUPPORT)")
        self.nombre_input = TextInput(hint_text="Tu nombre")
        self.eliminaciones_input = TextInput(hint_text="Tus eliminaciones", input_filter='int')
        self.asistencias_input = TextInput(hint_text="Tus asistencias", input_filter='int')
        self.muertes_input = TextInput(hint_text="Tus muertes", input_filter='int')
        self.dano_input = TextInput(hint_text="Tu daño total infligido", input_filter='int')
        self.minutos_input = TextInput(hint_text="Tus minutos jugados", input_filter='int')

        content.add_widget(self.posicion_input)
        content.add_widget(self.nombre_input)
        content.add_widget(self.eliminaciones_input)
        content.add_widget(self.asistencias_input)
        content.add_widget(self.muertes_input)
        content.add_widget(self.dano_input)
        content.add_widget(self.minutos_input)

        btn_comparar = Button(text="Comparar")
        btn_comparar.bind(on_press=self.realizar_comparacion)
        content.add_widget(btn_comparar)

        self.popup = Popup(title="Comparar Estadísticas", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def realizar_comparacion(self, instance):
        posicion = self.posicion_input.text.strip()
        posicion_estandarizada = obtener_posicion_estandarizada(posicion)
        if not posicion_estandarizada:
            self.popup.dismiss()
            self.mostrar_popup("Posición no válida. Intenta nuevamente.")
            return

        jugadores = leer_dataset_jugadores('./data/dataset_Mundial_2022/wc_players_main.csv')
        jugadores_posicion = filtrar_por_posicion(jugadores, posicion_estandarizada)
        if not jugadores_posicion:
            self.popup.dismiss()
            self.mostrar_popup(f"No se encontraron jugadores en la posición {posicion_estandarizada}.")
            return

        nombre = self.nombre_input.text.strip()
        eliminaciones = int(self.eliminaciones_input.text)
        asistencias = int(self.asistencias_input.text)
        muertes = int(self.muertes_input.text)
        dano_infligido = int(self.dano_input.text)
        minutos_jugados = int(self.minutos_input.text)

        jugador = Jugador(nombre, posicion_estandarizada, eliminaciones, asistencias, muertes, dano_infligido, minutos_jugados)
        comparar_estadisticas_jugador(jugador, jugadores_posicion)
        self.popup.dismiss()

    def mostrar_popup(self, mensaje):
        popup = Popup(title="Mensaje", content=Label(text=mensaje), size_hint=(0.8, 0.8))
        popup.open()

    def salir(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    MainApp().run()
