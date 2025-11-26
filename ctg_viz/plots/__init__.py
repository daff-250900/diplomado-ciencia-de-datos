"""
Plotting modules for CTG visualizations
"""

from . import histograms
from . import barplots
from . import boxplots
from . import density
from . import heatmap

import pandas as pd

class __PlotModules:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        """
        Inicializa la clase con un DataFrame.
        
        Args:
            dataframe: DataFrame de pandas que contiene los datos a graficar.
                Debe contener las columnas necesarias para el análisis.
        
        """
        self.df: pd.DataFrame = dataframe

__all__ = ['histograms', 'barplots', 'boxplots', 'density', 'heatmap', '__PlotModules']
