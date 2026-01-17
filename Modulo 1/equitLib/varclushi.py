from varclushi import VarClusHi
import plotly.express as px
import pandas as pd

def graficar_matriz_correlacion(dataframe, features_list):
    """
    Genera un heatmap interactivo para detectar multicolinealidad visualmente.
    """
    corr_matrix = dataframe[features_list].corr()
    
    fig = px.imshow(
        corr_matrix, 
        text_auto='.2f',          
        aspect="auto",
        color_continuous_scale='RdBu_r',
        zmin=-1, zmax=1,
        title="Matriz de Correlación (Detección de Multicolinealidad)"
    )
    
    fig.show()

def analizar_varclushi(dataframe, features_list, max_eigval2=1):
    """
    Ejecuta VarClusHi y grafica los resultados para seleccionar variables.
    El varclushi agrupa variables correlacionadas en clusters y selecciona
    la mejor variable representante de cada cluster.
    Valores RS_Ratio bajos indican buenas variables líderes.
    """
    vc = VarClusHi(dataframe[features_list], maxeigval2=max_eigval2, maxclus=None)
    vc.varclus()
    
    resumen = vc.rsquare
    
    # 2. Seleccionar la mejor variable de cada cluster (la del Ratio más bajo)
    # El (1-RS_Own) bajo indica que se explica bien por su propio cluster
    # El (1-RS_Next) alto indica que NO se explica por el siguiente cluster
    # Por tanto, buscamos minimizar el RS_Ratio = (1-RS_Own)/(1-RS_Next)
    
    best_vars = resumen.sort_values('RS_Ratio').groupby('Cluster').first()
    
    print(f"--- VarClusHi: Se encontraron {len(best_vars)} clusters ---")
    print(f"Variables seleccionadas (Líderes): {best_vars['Variable'].tolist()}")
    
    fig = px.bar(
        resumen, 
        x='Cluster', 
        y='RS_Ratio', 
        color='Variable',
        barmode='group',
        title='VarClusHi: Selección de Variables (Barra más baja = Mejor Representante)',
        hover_data=['RS_Own', 'RS_NC']
    )
    
    fig.add_hline(y=0.5, line_dash="dot", annotation_text="Zona de Alta Calidad")
    fig.show()
    
    return resumen, best_vars['Variable'].tolist()
