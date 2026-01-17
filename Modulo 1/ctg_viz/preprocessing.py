"""
Preprocessing utilities for CTG data
"""
import io
import html
from IPython.display import display, HTML

def check_data_completeness(self) -> None:
    """
    Analiza la completitud de los datos en el DataFrame.
    
    Calcula estadísticas sobre datos faltantes, tipos de datos y estadísticas
    descriptivas.

    Args:
        self: Instancia de CTGViz que contiene el DataFrame a analizar.
            Debe tener el atributo `df` con un DataFrame de pandas.
    
    Example:
        >>> from ctg_viz import CTGViz
        >>> viz = CTGViz(df)
        >>> preprocessing.check_data_completeness(viz)
    """
    # Capturar el output en un string
    output: io.StringIO = io.StringIO()
    
    # Calcula la cantidad de datos faltantes por columna
    total_missing = self.df.isnull().sum()

    # Calcula el porcentaje de datos faltantes
    total_cells: int = self.df.shape[0]
    percentage_missing = (total_missing / total_cells) * 100

    # Escribir los resultados en el buffer
    output.write(f"Total de datos faltantes:\n{total_missing}\n\n")
    output.write("------------------------------------------------------------\n\n")
    output.write(f"     Porcentaje de datos faltantes:\n{percentage_missing}%\n")
    output.write("------------------------------------------------------------\n\n")
    output.write(f"     Tipos de datos:\n{self.df.dtypes}\n")
    output.write("---------------------------------------------------------\n\n")
    output.write(f"     Estadisticas descriptivas:\n{self.df.describe()}\n")
    output.write("---------------------------------------------------------\n\n")
    
    # Obtener el contenido como string
    content: str = output.getvalue()
    output.close()
    
    # Escapar HTML y crear contenedor con scroll
    escaped_content: str = html.escape(content)
    
    html_content: str = f"""
    <div style="
        max-height: 500px;
        overflow-y: auto;
        overflow-x: auto;
        border: 1px solid #555;
        padding: 15px;
        background-color: #000000;
        color: #ffffff;
        font-family: 'Courier New', monospace;
        font-size: 12px;
        white-space: pre-wrap;
        word-wrap: break-word;
        border-radius: 5px;
    ">
    {escaped_content}
    </div>
    """
    
    # Mostrar el contenido con scroll
    display(HTML(html_content))