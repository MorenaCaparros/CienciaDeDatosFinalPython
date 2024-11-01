# StatForge

StatForge es una aplicación que permite comparar estadísticas de jugadores de League of Legends (LoL) utilizando gráficos interactivos. Este proyecto es el trabajo final para la materia de Python de la facultad de ingeniería de la UCASAL, en la carrera Licenciatura de Ciencia de Datos, en la Asignatura Programación II, a cargo del profesor Mario Ignacio Martinez

## Requisitos

- Python 3.x
- Kivy
- Matplotlib
- Pandas

## Instalación

1. Clona el repositorio:
    - `main_app.py`: Archivo principal que inicia la aplicación Kivy.
    - `visualizaciones.py`: Contiene funciones para mostrar gráficos.
    - `aplicacion/pantallas/menu.py`: Contiene la definición de la pantalla del menú.
    - `aplicacion/ui_config.py`: Configuración de colores y fuentes.
    - `dataset.csv`: Dataset con las estadísticas de los jugadores.
    - `log.jpg`: Logo de la aplicación.

## Uso

1. Ejecuta la aplicación:
    ```sh
    python src/main_app.py
    ```

2. En la pantalla principal, haz clic en el botón "Ver Jugadores" para abrir una ventana emergente con gráficos que comparan las estadísticas de los jugadores.

## Funcionalidades

- **Comparación de Jugadores**: Permite comparar estadísticas de diferentes jugadores de LoL mediante gráficos interactivos.
- **Visualización de Datos**: Utiliza Matplotlib para generar gráficos que muestran las estadísticas de los jugadores.
- **Interfaz de Usuario**: Desarrollada con Kivy, permite una navegación intuitiva y fácil de usar.
- **Personalización**: Los usuarios pueden modificar el dataset `dataset.csv` para incluir sus propios datos y personalizar la configuración de la interfaz en `aplicacion/ui_config.py`.

## Personalización

Puedes personalizar la aplicación modificando los archivos en el directorio `aplicacion` y actualizando el dataset `dataset.csv` con tus propios datos.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.