from . import preprocessing

class CTGViz:
    """
    Clase principal para visualización de datos CTG.
    """
    
    def __init__(self, dataframe):
        """
        Inicializa la clase con un DataFrame.
        
        :param dataframe: pd.DataFrame, el DataFrame a analizar.
        """
        self.df = dataframe
    
    def check_data_completeness_dafneelizabethzepedagonzalez(self):
        """
        Analiza la completitud de los datos.
        """
        return preprocessing.check_data_completeness(self)
    
