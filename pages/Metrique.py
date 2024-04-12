import streamlit as st 
import pandas as pd 
import numpy as np

obj_data = pd.read_csv(r"data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv")

accomplished = obj_data[obj_data.columns[8:]]

array_accomplished = accomplished.to_numpy().flatten()
def boolean_values(X) :
    if X == 'Yes' :
        return(1)
    else :
        return(0)
st.write(array_accomplished)
array_accomplished = np.array(pd.Series(array_accomplished).apply(lambda x : boolean_values(x)))

st.metric('Objective %',round(array_accomplished.mean()*100, 2))