"""
Funciones para graficar density plots (gráficos de densidad)
"""

from typing import Optional

def plot_density(
    self,
    color_by: Optional[str] = None,
    show: bool = True
) -> None:
    """Grafica density plots (KDE) para cada columna numérica del DataFrame.

    Parámetros:
    - self: DataFrame con datos numéricos.
    - color_by: str opcional. Nombre de columna categórica para colorear por grupo.
    - show: bool. Si se muestra inmediatamente la figura (True por defecto).

    Comportamiento:
    - Para cada columna numérica se crea un gráfico de densidad (KDE).
    - Si color_by está especificado, se generan múltiples curvas de densidad superpuestas (una por categoría).
    - Útil para visualizar la distribución suavizada de variables continuas.
    """
    import plotly.graph_objects as go
    from scipy import stats
    import numpy as np

    def calcular_kde(data):
        """Calcula KDE si los datos tienen variación suficiente."""
        if len(data) > 1 and data.std() > 1e-10:
            try:
                kde = stats.gaussian_kde(data)
                x_range = np.linspace(data.min(), data.max(), 200)
                return x_range, kde(x_range)
            except np.linalg.LinAlgError:
                pass
        return None, None

    numeric_cols = list(self.select_dtypes(include=[np.number]).columns)

    if color_by and color_by in self.columns:
        # Con multiples clases
        classes = sorted(self[color_by].dropna().unique())
        for col in numeric_cols:
            if col == color_by:
                continue
            fig = go.Figure()
            for cls in classes:
                data_class = self[self[color_by] == cls][col].dropna()
                x_range, kde_values = calcular_kde(data_class)
                if x_range is not None:
                    fig.add_trace(go.Scatter(
                        x=x_range, y=kde_values, mode='lines',
                        name=f'{color_by}={cls}', fill='tozeroy', opacity=0.6
                    ))
            fig.update_layout(
                title=f"{col} - Distribución de Densidad por {color_by}",
                xaxis_title="Valor", yaxis_title="Densidad", hovermode='x unified'
            )
            if show:
                fig.show()
    else:
        # Sin grupos
        for col in numeric_cols:
            data = self[col].dropna()
            x_range, kde_values = calcular_kde(data)
            if x_range is not None:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=x_range, y=kde_values, mode='lines', name='Densidad',
                    fill='tozeroy', line=dict(color='#1f77b4', width=2)
                ))
                fig.update_layout(
                    title=f"{col} - Gráfico de Densidad",
                    xaxis_title="Valor", yaxis_title="Densidad"
                )
                if show:
                    fig.show()
