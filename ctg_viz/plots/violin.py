"""
Funciones para graficar violin plots (gráficos de violín)
"""

from typing import Optional, List

def plot_violinplot(
    self,
    cols: Optional[List[str]] = None,
    group_by: Optional[str] = None,
    show: bool = True,
    points: str = 'all',
    side: str = 'positive',
    swarm: bool = False,
    swarm_jitter: float = 0.4,
    swarm_marker_size: int = 6
) -> None:
    """Grafica uno o múltiples violin plots para visualizar la distribución de variables.

    Parámetros:
    - self: DataFrame con los datos.
    - cols: lista opcional de columnas numéricas a graficar. Si None, se usan todas las numéricas.
    - group_by: str opcional. Columna categórica para separar distribuciones dentro de cada violín.
    - show: bool. Si True muestra inmediatamente la figura.
    - points: str. Cómo mostrar puntos individuales ('all', 'suspectedoutliers', 'outliers', 'none').
    - side: str. Lado del violín en caso de múltiple (por defecto 'positive').
    - swarm: bool. Si True agrega overlay tipo swarm (dispersión con jitter) sobre cada violín.
    - swarm_jitter: float. Intensidad del jitter horizontal para los puntos (0 a 1 aprox.).
    - swarm_marker_size: int. Tamaño de los puntos del swarm.

    Comportamiento:
    - Si group_by está definido, cada categoría genera un violín separado por variable.
    - Si no, se grafican violines independientes por cada columna numérica.
    - Muestra la distribución, densidad y valores individuales.
    - Si swarm=True se superpone una capa de puntos dispersos (simulación de swarmplot/seaborn).

    Ejemplos:
        # Violines para todas las variables numéricas
        plot_violinplot(df)

        # Violines para columnas específicas
        plot_violinplot(df, cols=['LB', 'AC', 'FM'])

        # Violines agrupados por clase
        plot_violinplot(df, cols=['LB', 'AC'], group_by='NSP')

        # Violines con overlay de swarm
        plot_violinplot(df, cols=['LB', 'AC'], group_by='NSP', swarm=True)
    """
    import plotly.graph_objects as go
    import numpy as np

    # Columnas numéricas objetivo
    if cols is None:
        cols = list(self.select_dtypes(include=[np.number]).columns)
    else:
        cols = [c for c in cols if c in self.columns and np.issubdtype(self[c].dtype, np.number)]
    if not cols:
        print("No hay columnas numéricas válidas para graficar violines.")
        return

    usar_grupos = group_by in self.columns if group_by else False
    if group_by and not usar_grupos:
        print(f"Advertencia: La columna '{group_by}' no existe. Se ignora group_by.")

    fig = go.Figure()

    def agregar_swarm(x_vals, y_vals, nombre):
        if not swarm or len(y_vals) == 0:
            return
        jitter = (np.random.rand(len(y_vals)) - 0.5) * swarm_jitter
        fig.add_trace(go.Scatter(
            x=[x + j for x, j in zip(x_vals, jitter)],
            y=y_vals,
            mode='markers',
            name=nombre + ' (swarm)',
            marker=dict(size=swarm_marker_size, opacity=0.5,
                        line=dict(width=0.5, color='rgba(0,0,0,0.3)')),
            showlegend=False
        ))

    categorias = sorted(self[group_by].dropna().unique()) if usar_grupos else [None]
    for col in cols:
        for cat in categorias:
            data = (self[self[group_by] == cat][col].dropna() if usar_grupos else self[col].dropna())
            if data.empty:
                continue
            x_base = [col] * len(data)
            fig.add_trace(go.Violin(
                x=x_base if usar_grupos else None,
                y=data,
                name=f"{col} ({group_by}={cat})" if usar_grupos else col,
                legendgroup=f"{col}-{cat}" if usar_grupos else col,
                scalegroup=col,
                side=side if usar_grupos else 'both',
                points=points,
                spanmode='hard',
                meanline_visible=True,
                opacity=0.75
            ))
            agregar_swarm(x_base if usar_grupos else [col] * len(data), data, f"{col} {cat}" if usar_grupos else col)

    fig.update_layout(
        title="Gráfico(s) de Violín" + (f" por {group_by}" if usar_grupos else ""),
        yaxis_title="Valor",
        xaxis_title="Variable",
        hovermode='closest',
        violingap=0.3,
        violingroupgap=0.1,
        violinmode='overlay' if usar_grupos else 'group'
    )

    fig.show()

