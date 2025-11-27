"""
Funciones para graficar dotplots (gráficos de puntos)
"""

from typing import Optional, List



def plot_dotplot(
	self,
	x_col: str,
	y_col: str,
	color_by: Optional[str] = None,
	size_by: Optional[str] = None,
	overlay: bool = False,
	group_col: Optional[str] = None,
	group_values: Optional[List] = None,
	show: bool = True
) -> None:
	"""
	Grafica un dotplot simple o comparativo (overlay) entre dos variables.

	Parámetros:
	- self: DataFrame con datos.
	- x_col: str. Nombre de columna para el eje X.
	- y_col: str. Nombre de columna para el eje Y.
	- color_by: str opcional. Columna para colorear puntos por categoría (solo modo simple).
	- size_by: str opcional. Columna para dimensionar puntos por valor numérico (solo modo simple).
	- overlay: bool. Si True, compara dos grupos en overlay (por defecto False).
	- group_col: str opcional. Columna categórica para separar los grupos (solo modo overlay).
	- group_values: lista opcional con los dos valores de grupo a comparar (solo modo overlay).
	- show: bool. Si se muestra inmediatamente la figura (True por defecto).

	Comportamiento:
	- Si overlay=False: gráfico de dispersión simple, permite color_by y size_by.
	- Si overlay=True: superpone los puntos de dos grupos definidos por group_col y group_values.
	"""
	import plotly.express as px
	import plotly.graph_objs as go

	# Validar columnas principales
	if x_col not in self.columns or y_col not in self.columns:
		print(f"Error: Las columnas '{x_col}' o '{y_col}' no existen en el DataFrame.")
		return

	if overlay:
		if not group_col or group_col not in self.columns:
			print(f"Error: Debes especificar una columna de grupo válida en 'group_col' para overlay.")
			return
		grupos = self[group_col].dropna().unique().tolist()
		group_values = group_values or grupos[:2]
		group_values = [g for g in group_values if g in grupos]
		if len(group_values) < 2:
			print(f"Error: Se requieren dos grupos válidos en '{group_col}' para comparar.")
			return
		colores = ['#636EFA', '#EF553B']
		traces = [
			go.Scatter(
				x=self[self[group_col] == grupo][x_col],
				y=self[self[group_col] == grupo][y_col],
				mode='markers',
				name=f"{group_col}: {grupo}",
				marker=dict(color=colores[i % len(colores)], opacity=0.7, size=8)
			) for i, grupo in enumerate(group_values)
		]
		fig = go.Figure(data=traces)
		fig.update_layout(
			title=f"Dotplot Overlay: {y_col} vs {x_col} por {group_col}",
			xaxis_title=x_col,
			yaxis_title=y_col,
			legend_title=group_col,
			hovermode='closest'
		)
	else:
		if color_by and color_by not in self.columns:
			print(f"Advertencia: La columna '{color_by}' no existe. Se ignorará color_by.")
			color_by = None
		if size_by and size_by not in self.columns:
			print(f"Advertencia: La columna '{size_by}' no existe. Se ignorará size_by.")
			size_by = None
		fig = px.scatter(
			self,
			x=x_col,
			y=y_col,
			color=color_by,
			size=size_by,
			title=f"Dotplot: {y_col} vs {x_col}",
			opacity=0.7,
			hover_data=self.columns.tolist()
		)
		fig.update_layout(
			xaxis_title=x_col,
			yaxis_title=y_col,
			hovermode='closest'
		)
	if show:
		fig.show()
