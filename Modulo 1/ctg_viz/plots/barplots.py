"""
Barplot plotting functions
"""

def plot_barplot(self, asc: bool | None = None, show: bool = True) -> None:
    """Plot an interactive horizontal barplot using Plotly.

    Parámetros:
    - self: DataFrame que contiene las columnas a graficar.
    - asc: bool | None: Orden de las barras.
        * True  -> orden ascendente (menor a mayor frecuencia, barras grandes abajo)
        * False -> orden descendente (mayor a menor frecuencia, barras grandes arriba)
        * None  -> valor por defecto (False: descendente)
    - show: bool: Si se muestra inmediatamente la figura (True por defecto).

    Comportamiento:
    - Barras horizontales (orientación 'h').
    - Eje X: frecuencia (conteo). Eje Y: categoría.
    - Se ordena por frecuencia según parámetro asc.
    """
    import plotly.express as px
    from plotly.graph_objs import Figure
    
    x_axis_label: str = "Frecuencia"
    y_axis_label: str = "Categoría"
    ascending: bool = False if asc is None else asc

    for col in self.columns:
        title: str = f"{col} - Gráfico de Barras"
        databar = self[col].value_counts().reset_index()
        databar.columns = ['Category', 'Count'] 
        # Ordenar por frecuencia
        databar = databar.sort_values('Count', ascending=ascending)
        fig: Figure = px.bar(
            databar,
            x='Count',
            y='Category',
            title=title,
            orientation='h',
            text='Count'
        )
        fig.update_traces(textposition='outside')
        fig.update_layout(xaxis_title=x_axis_label, yaxis_title=y_axis_label)
        if show:
            fig.show()
    