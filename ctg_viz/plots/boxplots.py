"""
Funciones para graficar boxplots
"""

def plot_boxplot(self, target: list = None, show: bool = True) -> None:
    """Graficar boxplots con subplots por cada variable target.

    Parámetros:
    - self: DataFrame con datos.
    - target: list: Lista de nombres de columnas objetivo (categóricas) para facetear.
    - show: bool: Si se muestra inmediatamente cada figura (True por defecto).

    Comportamiento:
    - Por cada columna numérica se crea una figura con subplots (una columna por cada target en la lista).
    - En cada subplot se grafica el boxplot de la variable numérica vs las categorías de esa columna target.
    """
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    from plotly.graph_objs import Figure
    import numpy as np

    y_axis_label: str = "Valor"
    x_axis_label: str = "Categoría"

    numeric_cols = list(self.select_dtypes(include=['number']).columns)

    for col in numeric_cols:
        fig = make_subplots(
            rows=1,
            cols=len(target),
            subplot_titles=[f"{t}" for t in target],
            shared_yaxes=True
        )

        for idx, target_col in enumerate(target, start=1):
            if target_col not in self.columns:
                continue
            df_sub = self[[target_col, col]].dropna()
            if df_sub.empty:
                continue
            tmp_fig: Figure = px.box(
                df_sub,
                x=target_col,
                y=col,
                points='outliers'
            )
            # Agregar trazas al subplot correspondiente
            for trace in tmp_fig.data:
                fig.add_trace(trace, row=1, col=idx)

        fig.update_layout(
            title_text=f"{col} - Boxplots por variables target",
            height=450,
        )
        # Etiquetas de ejes: solo el primero con Y para evitar repetición
        for c in range(1, len(target)+1):
            fig.update_xaxes(title_text=x_axis_label, row=1, col=c)
        fig.update_yaxes(title_text=y_axis_label, row=1, col=1)

        if show:
            fig.show()

