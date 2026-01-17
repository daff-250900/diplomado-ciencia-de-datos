"""
Funciones para graficar histogramas con soporte KDE
"""

from typing import Optional
from plotly.graph_objs import Figure
import pandas as pd

def plot_histogram(
    self,
    bins: int = 10,
    color_by: Optional[str] = None,
    show: bool = True
) -> None:
    """Grafica un histograma interactivo usando Plotly con línea KDE y agrupación opcional.

    Parámetros:
    - self: DataFrame o Series con datos numéricos a graficar
    - bins: int: Número de bins para el histograma (por defecto 10)
    - color_by: Optional str: Nombre de columna para agrupar/colorear histogramas por categoría
    - show: bool: Si se muestra inmediatamente la figura (por defecto True)

    Retorna:
    - None

    Ejemplos:
        # Histograma simple con línea KDE automática
        plot_histogram(df[['age', 'income']])
        
        # Agrupado por categoría con colores
        plot_histogram(df[['age']], color_by='gender')
    """
    import plotly.express as px
    import plotly.graph_objects as go
    from scipy import stats
    import numpy as np

    xlabel: str = "Value"
    ylabel: str = "Frequency"

    # Si se especifica una columna color_by, necesitamos el dataframe completo
    if color_by and isinstance(self, pd.DataFrame):
        for col in self.select_dtypes(include=[np.number]).columns:
            if col == color_by:
                continue
            title: str = f"{col} Distribution by {color_by}"
            fig: Figure = px.histogram(
                self, 
                x=col, 
                color=color_by,
                nbins=bins, 
                title=title,
                barmode='overlay',
                opacity=0.7
            )
            fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel)
            if show:
                fig.show()
    else:
        for col in self.columns:
            title: str = col + " Distribution"
            
            # Crear histograma
            fig: Figure = px.histogram(
                self[col].dropna(), 
                nbins=bins, 
                title=title
            )
            fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel)
            
            # Agregar línea KDE superpuesta
            data = self[col].dropna()
            if len(data) > 1:
                # Verificar si los datos tienen suficiente variación para KDE
                data_std = data.std()
                data_range = data.max() - data.min()
                
                # Solo agregar KDE si los datos tienen variación significativa
                # Omitir si todos los valores son iguales o muy cercanos (datos constantes/casi constantes)
                if data_std > 1e-10 and data_range > 1e-10 and len(data.unique()) > 1:
                    try:
                        # Calcular KDE
                        kde = stats.gaussian_kde(data)
                        x_range = np.linspace(data.min(), data.max(), 200)
                        kde_values = kde(x_range)
                        
                        # Escalar KDE para que coincida con la altura del histograma
                        hist_max = len(data) / bins
                        kde_scaled = kde_values * hist_max * data_range / bins
                        
                        # Agregar trazo KDE
                        fig.add_trace(go.Scatter(
                            x=x_range,
                            y=kde_scaled,
                            mode='lines',
                            name='Densidad (KDE)',
                            line=dict(color='red', width=2),
                            yaxis='y'
                        ))
                    except np.linalg.LinAlgError:
                        # Omitir KDE si los datos son degenerados (en subespacio de menor dimensión)
                        pass
            
            if show:
                fig.show()