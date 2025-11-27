"""
Pruebas unitarias para el módulo de density plots
"""

import unittest
import pandas as pd
import numpy as np
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Agregar el directorio raíz al path para imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from ctg_viz.plots.density import plot_density


class TestPlotDensity(unittest.TestCase):
    """Pruebas unitarias para la función plot_density."""

    @patch('ctg_viz.plots.density.go.Figure')
    def test_plot_density_sin_grupos(self, mock_figure):
        """Verifica que la función genera density plots correctamente sin agrupación."""
        # Crear DataFrame de prueba con distribución normal
        np.random.seed(42)
        df = pd.DataFrame({
            'var_continua': np.random.randn(100),
            'var_categorica': np.random.choice(['A', 'B', 'C'], 100)
        })
        
        # Configurar mock
        mock_fig_instance = MagicMock()
        mock_figure.return_value = mock_fig_instance
        
        # Ejecutar la función sin color_by
        plot_density(df, color_by=None, show=False)
        
        # Verificar que se creó una figura
        self.assertTrue(mock_figure.called, "go.Figure debe ser llamado")
        
        # Verificar que add_trace fue llamado para agregar la curva de densidad
        self.assertTrue(mock_fig_instance.add_trace.called, 
                       "Debe agregar al menos una traza de densidad")
        
        # Verificar que update_layout fue llamado para configurar títulos
        self.assertTrue(mock_fig_instance.update_layout.called,
                       "Debe actualizar el layout con títulos")

    @patch('ctg_viz.plots.density.go.Figure')
    def test_plot_density_con_multiples_grupos(self, mock_figure):
        """Verifica que la función genera density plots con múltiples curvas por grupo."""
        # Crear DataFrame con grupos distintos
        np.random.seed(42)
        df = pd.DataFrame({
            'var_numerica': np.concatenate([
                np.random.normal(0, 1, 50),   # Grupo A
                np.random.normal(5, 1, 50),   # Grupo B
                np.random.normal(10, 1, 50)   # Grupo C
            ]),
            'grupo': ['A'] * 50 + ['B'] * 50 + ['C'] * 50
        })
        
        # Configurar mock
        mock_fig_instance = MagicMock()
        mock_figure.return_value = mock_fig_instance
        
        # Ejecutar la función con color_by
        plot_density(df, color_by='grupo', show=False)
        
        # Verificar que se creó una figura
        self.assertTrue(mock_figure.called, "go.Figure debe ser llamado")
        
        # Verificar que add_trace fue llamado múltiples veces (una por grupo)
        call_count = mock_fig_instance.add_trace.call_count
        self.assertGreaterEqual(call_count, 3, 
                               "Debe agregar al menos 3 trazas (una por grupo A, B, C)")
        
        # Verificar que update_layout fue llamado con información del grupo
        self.assertTrue(mock_fig_instance.update_layout.called,
                       "Debe actualizar el layout")


if __name__ == '__main__':
    unittest.main()
