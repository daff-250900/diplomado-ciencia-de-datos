from sklearn.feature_selection import SelectKBest, f_classif
import pandas as pd

#K numero de columnas a conservar


def selectK(df, colObjetivo, k=5, score_func=f_classif):
    x = df.drop(columns=[colObjetivo])
    y = df[colObjetivo]

    selector = SelectKBest(score_func,k=k)
    selector.fit(x,y)
    columnaSelect.fit(x,y)
    columnaSelect=x.columns[selector.get_support()].tolist()

    return columnaSelect
