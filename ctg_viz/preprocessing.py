"""
Preprocessing utilities for CTG data
"""
import io
import html
from IPython.display import display, HTML

def check_data_completeness(self):
    """
    Analiza la completitud de los datos en el DataFrame.

    """
    # Capturar el output en un string
    output = io.StringIO()
    
    # Calcula la cantidad de datos faltantes por columna
    total_missing = self.df.isnull().sum()

    # Calcula el porcentaje de datos faltantes
    total_cells = self.df.size
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
    content = output.getvalue()
    output.close()
    
    # Escapar HTML y crear contenedor con scroll
    escaped_content = html.escape(content)
    
    html_content = f"""
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