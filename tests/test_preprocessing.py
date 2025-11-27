"""
Pruebas unitarias para el módulo de preprocesamiento de datos
"""

import unittest
import pandas as pd
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
from io import StringIO

# Agregar el directorio raíz al path para imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from ctg_viz.preprocessing import check_data_completeness


class MockCTGViz:
    """Clase auxiliar para simular una instancia de CTGViz en tests."""
    def __init__(self, df):
        self.df = df


class TestCheckDataCompleteness(unittest.TestCase):
    """Pruebas unitarias para la función check_data_completeness."""

    @patch('ctg_viz.preprocessing.display')
    def test_check_data_completeness_sin_datos_faltantes(self, mock_display):
        """Verifica que la función procesa correctamente DataFrames sin datos faltantes."""
        # Crear DataFrame de prueba sin datos faltantes
        df = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5],
            'col2': [10.5, 20.5, 30.5, 40.5, 50.5],
            'col3': ['A', 'B', 'C', 'D', 'E']
        })
        
        viz_mock = MockCTGViz(df)
        
        # Ejecutar la función
        check_data_completeness(viz_mock)
        
        # Verificar que display fue llamado
        self.assertTrue(mock_display.called, "La función display debe ser llamada")
        
        # Verificar que no hay valores faltantes
        total_missing = df.isnull().sum().sum()
        self.assertEqual(total_missing, 0, "No debe haber datos faltantes en este DataFrame")

    @patch('ctg_viz.preprocessing.display')
    def test_check_data_completeness_con_datos_faltantes(self, mock_display):
        """Verifica que la función identifica y reporta correctamente datos faltantes."""
        # Crear DataFrame de prueba con datos faltantes
        df = pd.DataFrame({
            'col1': [1, None, 3, None, 5],  # 2 valores faltantes
            'col2': [10.5, 20.5, None, 40.5, 50.5],  # 1 valor faltante
            'col3': ['A', 'B', 'C', 'D', 'E']  # Sin valores faltantes
        })
        
        viz_mock = MockCTGViz(df)
        
        # Ejecutar la función
        check_data_completeness(viz_mock)
        
        # Verificar que display fue llamado
        self.assertTrue(mock_display.called, "La función display debe ser llamada")
        
        # Verificar cantidades de datos faltantes
        missing_col1 = df['col1'].isnull().sum()
        missing_col2 = df['col2'].isnull().sum()
        missing_col3 = df['col3'].isnull().sum()
        
        self.assertEqual(missing_col1, 2, "col1 debe tener 2 valores faltantes")
        self.assertEqual(missing_col2, 1, "col2 debe tener 1 valor faltante")
        self.assertEqual(missing_col3, 0, "col3 no debe tener valores faltantes")
        
        # Verificar porcentajes
        percentage_col1 = (missing_col1 / len(df)) * 100
        self.assertEqual(percentage_col1, 40.0, "col1 debe tener 40% de datos faltantes")


if __name__ == '__main__':
    unittest.main()
