import pandas as pd

def variablesClas(series: pd.Series, threshold: int = 10) -> bool:
    """
    Helper interno para determinar si una columna es 'Continua'
    según la regla del proyecto: Numérica y > 10 valores únicos.
    """
    return pd.api.types.is_numeric_dtype(series) and series.nunique() > threshold

def separar_variables(df: pd.DataFrame, target_col: str = None, threshold: int = 10):
    """
    Clasifica las columnas del DataFrame en dos listas:
    1. Continuas: Numéricas con alta cardinalidad.
    2. Discretas/Categóricas: El resto (texto o numéricas con pocos valores).
    """
    continuas = []
    otras = []
    
    features_list = df.columns.tolist()
    
    if target_col and target_col in features_list:
        features_list.remove(target_col)
        print(f"-> Variable objetivo '{target_col}' excluida de las features.")
    # -------------------------

    for col in features_list:
        if variablesClas(df[col], threshold):
            continuas.append(col)
        else:
            otras.append(col)
            
    print(f"-> Se detectaron {len(continuas)} variables continuas y {len(otras)} discretas/categóricas.")
    return continuas, otras