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
    descriptivas. El resultado se muestra en un contenedor HTML con scroll
    y fondo negro para mejor visualización en notebooks.
    
    Args:
        self: Instancia de CTGViz que contiene el DataFrame a analizar.
            Debe tener el atributo `df` con un DataFrame de pandas.
    
    Returns:
        None: La función muestra el resultado directamente usando IPython.display.
    
    Note:
        El output se muestra en un contenedor HTML con las siguientes características:
        - Altura máxima de 500px con scroll vertical y horizontal
        - Fondo negro con texto blanco
        - Fuente monospace para mejor legibilidad
    
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
    total_cells: int = self.df.size
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


def vars_clasification(self) -> tuple[list[str], list[str]]:
    """
    Clasifica las variables del DataFrame en discretas y continuas.
    
    Analiza cada columna del DataFrame y la clasifica según:
    - Variables continuas: Columnas de tipo int64 o float64 con más de 10 valores únicos
    - Variables discretas: Todas las demás (object, bool, o numéricas con <= 10 valores únicos)
    
    Args:
        self: Instancia de CTGViz que contiene el DataFrame a analizar.
            Debe tener el atributo `df` con un DataFrame de pandas.
    
    Returns:
        tuple[list[str], list[str]]: Tupla con dos listas:
            - Primera lista (list[str]): Nombres de las variables continuas
            - Segunda lista (list[str]): Nombres de las variables discretas
    
    Note:
        La lógica de clasificación considera que una variable numérica con
        muchos valores únicos (>10) es continua, mientras que las que tienen
        pocos valores únicos o son de tipo object se consideran discretas.
    
    Example:
        >>> from ctg_viz import CTGViz
        >>> viz = CTGViz(df)
        >>> continuas, discretas = preprocessing.vars_clasification(viz)
        >>> print(f"Continuas: {continuas}")
        >>> print(f"Discretas: {discretas}")
    """
    varc: list[str] = []
    vard: list[str] = []
    
    for col in self.df.columns:
        if self.df[col].dtype == 'int64' or self.df[col].dtype == 'float64' and self.df[col].nunique() > 10:
            varc.append(col)
        else:
            vard.append(col)

    return varc, vard