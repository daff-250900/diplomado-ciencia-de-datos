"""
Categorization utilities for CTG data
"""

def categorization(self) -> tuple[list[str], list[str]]:
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
        if (self.df[col].dtype == 'int64' or self.df[col].dtype == 'float64') and self.df[col].nunique() > 10:
            varc.append(col)
        else:
            vard.append(col)

    return varc, vard