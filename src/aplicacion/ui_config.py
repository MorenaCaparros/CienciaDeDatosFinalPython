from kivy.core.text import LabelBase
from kivy.core.window import Window

# Registramos la fuente personalizada
LabelBase.register(name="EpicFont", fn_regular="fuente.ttf")

# Configuramos el color del fondo
Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Fondo oscuro similar al estilo de LoL

# Colores personalizados
COLOR_DORADO = (1, 0.84, 0, 1)
COLOR_GRIS = (0.8, 0.8, 0.8, 1)
