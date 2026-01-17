from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

def calcular_vif(dataframe, features_list):
    """
    Calcula el Factor de Inflación de Varianza (VIF) para detectar multicolinealidad
    multivariante.
    Regla de dedo: VIF > 5 o 10 indica problemas severos.
    """
    X = dataframe[features_list].dropna()
    
    vif_data = pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) 
                       for i in range(len(X.columns))]
    
    vif_data = vif_data.sort_values(by='VIF', ascending=False)
    
    print("--- Reporte VIF (Multicolinealidad) ---")
    print(vif_data.head(10)) # Mostrar las 10 peores