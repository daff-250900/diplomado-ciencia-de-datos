from . import preprocessing
import pandas as pd

class CTGViz:
    """
    Clase principal para visualización y análisis de datos CTG.
    
    Esta clase proporciona métodos para analizar, preprocesar y visualizar
    datos de Cardiotocografía (CTG). Permite realizar análisis de completitud
    de datos, clasificación de variables y generación de visualizaciones.
    
    Attributes:
        df (pd.DataFrame): DataFrame que contiene los datos CTG a analizar.
    
    Example:
        >>> import pandas as pd
        >>> from ctg_viz import CTGViz
        >>> df = pd.read_csv('datasets/CTG.csv')
        >>> viz = CTGViz(df)
        >>> viz.check_data_completeness_dafneelizabethzepedagonzalez()
    """
    
    def __init__(self, dataframe: pd.DataFrame) -> None:
        """
        Inicializa la clase con un DataFrame.
        
        Args:
            dataframe: DataFrame de pandas que contiene los datos CTG a analizar.
                Debe contener las columnas necesarias para el análisis.
        
        Example:
            >>> df = pd.read_csv('datasets/CTG.csv')
            >>> viz = CTGViz(df)
        """
        self.df: pd.DataFrame = dataframe
    
    def check_data_completeness_dafneelizabethzepedagonzalez(self) -> None:
        """
        Analiza la completitud de los datos en el DataFrame.
        
        Calcula y muestra información sobre:
        - Total de datos faltantes por columna
        - Porcentaje de datos faltantes
        - Tipos de datos de cada columna
        - Estadísticas descriptivas del DataFrame
        
        Returns:
            None: La función muestra el resultado directamente en el notebook.
        
        Example:
            >>> viz = CTGViz(df)
            >>> viz.check_data_completeness_dafneelizabethzepedagonzalez()
        """
        return preprocessing.check_data_completeness(self)

    def vars_classification(self) -> tuple[list[str], list[str]]:
        """
        Clasifica las variables del DataFrame en discretas y continuas.
        
        Clasifica cada columna como:
        - Continua: Si es de tipo int64 o float64 Y tiene más de 10 valores únicos
        - Discreta: Todos los demás casos (object, bool, o numéricas con <= 10 valores únicos)
        
        Returns:
            tuple[list[str], list[str]]: Tupla con dos listas:
                - Primera lista: Nombres de variables continuas
                - Segunda lista: Nombres de variables discretas
        
        Example:
            >>> viz = CTGViz(df)
            >>> continuas, discretas = viz.vars_classification()
            >>> print(f"Variables continuas: {len(continuas)}")
            >>> print(f"Variables discretas: {len(discretas)}")
        """
        return preprocessing.vars_clasification(self)
    
