import pandas as pd
import numpy as np

#varPredict - variable predictiva
# varObj - variable objetivo 

def infoValue(df, varPredict, varObj):
    data = df[[varPredict, varObj]].copy()
    grupo = data.groupBy(varPredict)[varObj]
    dist = grupo.mean().to_frame("nok-Rate")
    dist["ok"] = 1-dist["nok-Rate"]
    dist["nok"]= dist["nok-Rate"]

    dist["woe"]=np.log((dist["ok"]/dist["ok"].sum()))/((dist["nok"]/dist["nok"].sum()))
    iv = ((dist["ok"]/dist["ok"].sum())-(dist["nok"]/dist["nok"].sum()))*dist["woe"]

    return iv.sum()     
