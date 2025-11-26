"""
Histogram plotting functions
"""

from plotly.graph_objs import Figure
import pandas as pd

def plot_histogram(self) -> None:
    """Plot an interactive histogram using Plotly.

    Parameters:
    - data: Sequence[float]: Numeric data to plot.
    - bins: int: Number of bins for the histogram.
    - title: str: Title of the plot.
    - xlabel: str: Label for the x-axis.
    - ylabel: str: Label for the y-axis.
    - show: bool: Whether to immediately display the figure (default True).

    Returns:
    - None
    """
    import plotly.express as px

    bins: int = 10
    xlabel: str = "Value"
    ylabel: str = "Frequency"
    show: bool = True

    for col in self.columns:
        title: str = col + " Distribution"
        fig: Figure = px.histogram(self[col], nbins=bins, title=title, text_auto = True)
        fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel)
        if show:
            fig.show()