"""
Funciones para graficar lineplots (gráficos de líneas)
"""

from typing import Optional, List

def plot_lineplot(
    self,
    x_col: Optional[str] = None,
    y_cols: Optional[List[str]] = None,
    group_by: Optional[str] = None,
    show: bool = True
) -> None:
    """
    Grafica un lineplot para visualizar tendencias a lo largo del tiempo o secuencias.

    Parámetros:
    - self: DataFrame con datos.
    - x_col: str opcional. Columna para el eje X. Si es None, usa el índice.
    - y_cols: lista opcional de columnas para el eje Y. Si es None, grafica todas las numéricas.
    - group_by: str opcional. Columna categórica para crear líneas separadas por grupo.
    - show: bool. Si se muestra inmediatamente la figura.
    """
    import plotly.graph_objects as go
    import numpy as np

    x_data = self[x_col] if x_col and x_col in self.columns else self.index
    x_label = x_col if x_col else "Índice"

    if y_cols is None:
        y_cols = list(self.select_dtypes(include=[np.number]).columns)
        y_cols = [col for col in y_cols if col not in [x_col, group_by]]
    
    if not y_cols:
        print("No hay columnas numéricas para graficar.")
        return

    fig = go.Figure()

    if group_by and group_by in self.columns:
        for grupo in sorted(self[group_by].dropna().unique()):
            df_grupo = self[self[group_by] == grupo]
            x_grupo = df_grupo[x_col] if x_col and x_col in df_grupo.columns else df_grupo.index
            for y_col in y_cols:
                if y_col in df_grupo.columns:
                    fig.add_trace(go.Scatter(
                        x=x_grupo, y=df_grupo[y_col], mode='lines+markers',
                        name=f"{y_col} ({group_by}={grupo})",
                        line=dict(width=2), marker=dict(size=6)
                    ))
    else:
        for y_col in y_cols:
            if y_col in self.columns:
                fig.add_trace(go.Scatter(
                    x=x_data, y=self[y_col], mode='lines+markers',
                    name=y_col, line=dict(width=2), marker=dict(size=6)
                ))

    fig.update_layout(
        title=f"Lineplot por {group_by}" if group_by else "Lineplot",
        xaxis_title=x_label,
        yaxis_title="Valor",
        hovermode='x unified',
        showlegend=True
    )
    
    if show:
        fig.show()
