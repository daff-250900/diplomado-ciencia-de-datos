"""
Funciones para graficar heatmaps (mapas de calor)
"""

from typing import Literal

def plot_heatmap(
    self,
    method: Literal['pearson', 'spearman', 'kendall'] = 'pearson',
    annot: bool = True,
    show: bool = True
) -> None:
    """Grafica un heatmap de correlación entre variables numéricas.

    Parámetros:
    - self: DataFrame con datos numéricos.
    - method: str. Método de correlación ('pearson', 'spearman', 'kendall').
    - annot: bool. Si se muestran los valores de correlación en cada celda.
    - show: bool. Si se muestra inmediatamente la figura.

    Comportamiento:
    - Calcula la matriz de correlación entre todas las columnas numéricas.
    - Genera un mapa de calor con escala de colores (azul=negativa, rojo=positiva).
    """
    import plotly.graph_objects as go
    import numpy as np

    numeric_df = self.select_dtypes(include=[np.number])
    if numeric_df.empty:
        print("No hay columnas numéricas para calcular correlaciones.")
        return
    
    corr_matrix = numeric_df.corr(method=method)
    
    heatmap_params = {
        'z': corr_matrix.values,
        'x': corr_matrix.columns,
        'y': corr_matrix.columns,
        'colorscale': 'RdBu_r',
        'zmid': 0,
        'colorbar': dict(title="Correlación")
    }
    
    if annot:
        heatmap_params.update({
            'text': np.round(corr_matrix.values, 2).astype(str),
            'texttemplate': '%{text}',
            'textfont': {"size": 10}
        })
    
    fig = go.Figure(data=go.Heatmap(**heatmap_params))
    fig.update_layout(
        title=f"Matriz de Correlación ({method.capitalize()})",
        xaxis_title="Variables",
        yaxis_title="Variables",
        width=800,
        height=800,
        xaxis={'side': 'bottom'},
        yaxis={'autorange': 'reversed'}
    )
    
    if show:
        fig.show()
