from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def aplicar_pca(dataframe, n_components=3):
    """
    Aplica PCA a un DataFrame después de escalar las variables. 
    Retorna un DataFrame con las componentes principales y el modelo PCA.
    El método Pca se utiliza para reducir la dimensionalidad de los datos 
    lo que se interpreta como la transformación de un conjunto de variables 
    posiblemente correlacionadas en un conjunto de valores de 
    variables no correlacionadas llamadas componentes principales.
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(dataframe)
    
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(X_scaled)

    cols = [f'PC{i+1}' for i in range(n_components)]
    pca_df = pd.DataFrame(data=components, columns=cols)
    
    print(f"Varianza explicada: {pca.explained_variance_ratio_}")
    
    return pca_df, pca

def resumen_componentes(pca_modelo, feature_names, n_top=5):
    """
    Muestra qué variables originales tienen más peso en cada componente.
    """

    componentes_df = pd.DataFrame(
        pca_modelo.components_, 
        columns=feature_names,
        index=[f'PC{i+1}' for i in range(len(pca_modelo.components_))]
    )

    print("--- Resumen: Variables más influyentes por Componente ---")
    for i in range(len(componentes_df)):
        pc = componentes_df.iloc[i]
        top_vars = pc.abs().sort_values(ascending=False).head(n_top)
        
        print(f"\nComponente Principal {i+1} (PC{i+1}):")
        for var_name in top_vars.index:
            peso = pc[var_name]
            print(f"   - {var_name}: {peso:.4f}")


def graficar_varianza_acumulada(pca_modelo):
    """
    Genera un 'Scree Plot' interactivo y retorna la figura.
    """
    varianza_acum = np.cumsum(pca_modelo.explained_variance_ratio_)
    num_componentes = len(varianza_acum)
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=[f'PC{i+1}' for i in range(num_componentes)],
        y=pca_modelo.explained_variance_ratio_,
        name='Varianza Individual'
    ))
    
    fig.add_trace(go.Scatter(
        x=[f'PC{i+1}' for i in range(num_componentes)],
        y=varianza_acum,
        mode='lines+markers',
        name='Varianza Acumulada'
    ))
    
    fig.update_layout(
        title='Scree Plot: Varianza Explicada por Componente',
        yaxis_title='Proporción de Varianza',
        hovermode='x unified'
    )
    
    fig.add_hline(y=0.8, line_dash="dash", annotation_text="80% Info")
    
    fig.show()  # Muestra el gráfico en el momento
    