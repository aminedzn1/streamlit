import streamlit as st 
import pandas as pd 
import numpy as np

###########################################################################################################

try :
    obj_data = st.session_state.obj_data
except : 
    obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)

###########################################################################################################

domain = st.selectbox('Fonction / Domaine', ("Global Status","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"))
try :    
    accomplished = obj_data[obj_data.columns[domain]]
except :
    accomplished = obj_data[obj_data.columns[8:]]

array_accomplished = accomplished.to_numpy().flatten()
def boolean_values(X) :
    if X == 'Yes' :
        return(1)
    else :
        return(0)

array_accomplished = np.array(pd.Series(array_accomplished).apply(lambda x : boolean_values(x)))

st.metric('Objective %',round(array_accomplished.mean()*100, 2))