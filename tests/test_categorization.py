"""
Pruebas unitarias para el módulo de categorización de variables
"""

import unittest
import pandas as pd
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from ctg_viz.categorization import categorization


class MockCTGViz:
    """Clase auxiliar para simular una instancia de CTGViz en tests."""
    def __init__(self, df):
        self.df = df


class TestCategorization(unittest.TestCase):
    """Pruebas unitarias para la función categorization."""

    def test_categorization_variables_continuas(self):
        """Verifica que las variables continuas (numéricas con >10 valores únicos) se identifiquen correctamente."""
        # Crear DataFrame de prueba con una variable continua
        df = pd.DataFrame({
            'var_continua': range(1, 22),  # 21 valores únicos (1-21)
            'var_discreta': [1, 2, 3] * 7,  # 21 valores (3 únicos repetidos)
            'var_categorica': ['A', 'B', 'C'] * 7  # 21 valores (3 únicos repetidos)
        })
        
        viz_mock = MockCTGViz(df)
        continuas, discretas = categorization(viz_mock)
        
        # Aserciones
        self.assertIn('var_continua', continuas, "Variable con >10 valores únicos debe ser continua")
        self.assertNotIn('var_continua', discretas, "Variable continua no debe estar en discretas")
        self.assertEqual(len(continuas), 1, "Debe haber exactamente 1 variable continua")

    def test_categorization_variables_discretas(self):
        """Verifica que las variables discretas (<=10 valores únicos, object, bool) se identifiquen correctamente."""
        # Crear DataFrame de prueba con variables discretas (todos con 20 filas)
        df = pd.DataFrame({
            'var_numerica_pocos_valores': [1, 2, 3, 4, 5] * 4,  # 20 valores (5 únicos)
            'var_categorica': ['A', 'B', 'C', 'D'] * 5,  # 20 valores (4 únicos)
            'var_booleana': [True, False] * 10  # 20 valores (2 únicos)
        })
        
        viz_mock = MockCTGViz(df)
        continuas, discretas = categorization(viz_mock)
        
        # Aserciones
        self.assertIn('var_numerica_pocos_valores', discretas, "Variable numérica con <=10 valores debe ser discreta")
        self.assertIn('var_categorica', discretas, "Variable tipo object debe ser discreta")
        self.assertIn('var_booleana', discretas, "Variable booleana debe ser discreta")
        self.assertEqual(len(discretas), 3, "Debe haber exactamente 3 variables discretas")
        self.assertEqual(len(continuas), 0, "No debe haber variables continuas en este test")


if __name__ == '__main__':
    unittest.main()
