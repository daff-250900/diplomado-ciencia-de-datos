"""
Pruebas unitarias para el módulo de boxplots
"""

import unittest
import pandas as pd
import numpy as np
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Agregar el directorio raíz al path para imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from ctg_viz.plots.boxplots import plot_boxplot


class TestPlotBoxplot(unittest.TestCase):
    """Pruebas unitarias para la función plot_boxplot."""

    @patch('ctg_viz.plots.boxplots.make_subplots')
    @patch('ctg_viz.plots.boxplots.px.box')
    def test_plot_boxplot_con_variables_numericas_y_target(self, mock_px_box, mock_make_subplots):
        """Verifica que la función genera boxplots correctamente con variables numéricas y targets válidos."""
        # Crear DataFrame de prueba
        df = pd.DataFrame({
            'var_numerica1': np.random.randn(50),
            'var_numerica2': np.random.randn(50),
            'target1': np.random.choice(['A', 'B', 'C'], 50),
            'target2': np.random.choice([1, 2, 3], 50)
        })
        
        # Configurar mocks
        mock_fig = MagicMock()
        mock_make_subplots.return_value = mock_fig
        mock_px_box.return_value = MagicMock(data=[MagicMock()])
        
        # Ejecutar la función
        plot_boxplot(df, target=['target1', 'target2'], show=False)
        
        # Verificar que make_subplots fue llamado con parámetros correctos
        mock_make_subplots.assert_called_once()
        call_args = mock_make_subplots.call_args
        self.assertEqual(call_args[1]['rows'], 1, "Debe crear 1 fila de subplots")
        self.assertEqual(call_args[1]['cols'], 2, "Debe crear 2 columnas (una por target)")
        
        # Verificar que px.box fue llamado (una vez por variable numérica y por target)
        self.assertTrue(mock_px_box.called, "px.box debe ser llamado para crear boxplots")
        
        # Verificar que se agregaron trazas al subplot
        self.assertTrue(mock_fig.add_trace.called, "Debe agregar trazas al subplot")

if __name__ == '__main__':
    unittest.main()
