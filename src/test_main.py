import unittest
from unittest.mock import patch, MagicMock
from main import main
from utils.file_manager import leer_jugadores_csv, guardar_jugadores_csv

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'TestPlayer', 'MID', '10', '5', '2', '300', '20', '4'])
    @patch('utils.file_manager.guardar_jugadores_csv')  # Simular la función de guardado
    @patch('builtins.print')
    def test_main_ingresar_tus_estadisticas_y_guardado(self, mock_print, mock_guardar, mock_input):
        # Ejecutar main, que debería llamar a guardar_jugadores_csv
        main()
        
        # Confirmar que se llamó a guardar_jugadores_csv
        mock_guardar.assert_called_once()
        
        # Obtener los argumentos con los que fue llamado guardar_jugadores_csv
        args, _ = mock_guardar.call_args
        nuevo_jugador = args[1][0]  # Obtener el primer jugador del argumento de jugadores
        
        # Verificar los datos del jugador
        self.assertEqual(nuevo_jugador.nombre, 'TestPlayer')
        self.assertEqual(nuevo_jugador.posicion, 'MID')
        self.assertEqual(nuevo_jugador.eliminaciones, 10)
        self.assertEqual(nuevo_jugador.dano_infligido, 300)

if __name__ == '__main__':
    unittest.main()
