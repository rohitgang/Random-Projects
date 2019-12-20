import pandas as pd
import numpy as np

def missingData(df) :
    ret= dict()
    for col in df.columns:
        if df[col].isna().sum() > 0:
            ret[col]= df[col].isna().sum()

    return ret

def missingPercent(df) :
    miss= missingData(df)
    vals= np.asarray(list(miss.values()))
    vals= vals/len(df)* 100.00
    ret= dict()
    col= list(miss.keys())

    for i in range(len(vals)):
       ret[col[i]]= vals[i]
    return ret

def dropFeatures(df, threshold) :
    miss= missingPercent(df)
    dropList= list()
    ret= dict()

    for key,value in miss.items():
        if value > threshold :
            dropList.append(key)
        else:
            ret[key]= value

    df= df.drop(dropList, axis= 1)
    return df, ret