"""
Barplot plotting functions
"""

def plot_barplot(self) -> None:
    """Plot an interactive barplot using Plotly.

    Parameters:
    - data: Sequence[float]: Numeric data to plot.
    - title: str: Title of the plot.
    - xlabel: str: Label for the x-axis.
    - ylabel: str: Label for the y-axis.
    - show: bool: Whether to immediately display the figure (default True).

    Returns:
    - None
    """
    import plotly.express as px
    from plotly.graph_objs import Figure

    xlabel: str = "Category"
    ylabel: str = "Count"
    show: bool = True

    for col in self.columns:
        title: str = col + " Barplot"
        databar = self[col].value_counts().reset_index()
        databar.columns = ['Category', 'Count']
        fig: Figure = px.bar(databar, x=xlabel, y=ylabel, title=title)
        fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel)
        if show:
            fig.show()
    