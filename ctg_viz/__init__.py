from . import preprocessing
import pandas as pd

class CTGViz:
    """
    Clase principal para visualización de datos CTG.
    """
    
    def __init__(self, dataframe: pd.DataFrame) -> None:
        """
        Inicializa la clase con un DataFrame.
        
        :param dataframe: pd.DataFrame, el DataFrame a analizar.
        """
        self.df: pd.DataFrame = dataframe
    
    def check_data_completeness_dafneelizabethzepedagonzalez(self) -> None:
        """
        Analiza la completitud de los datos.
        """
        return preprocessing.check_data_completeness(self)

    def vars_classification(self) -> tuple[list[str], list[str]]:
        """
        Clasifica las variables en discretas y continuas.
        """
        return preprocessing.vars_clasification(self)
    
