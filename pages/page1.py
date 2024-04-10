import streamlit as st 
import pandas as pd 
import numpy as np

obj_data = st.session_state['obj_data']

accomplished = obj_data[obj_data.columns[8:]]

array_accomplished = accomplished.to_numpy().flatten()
def boolean_values(x) :
    match x :
        case 'Yes' :
            return(1)
        case 'No' :
            return(0)
        case _ : 
            return(0)

array_accomplished = array_accomplished.apply(lambda x : boolean_values(x))

st.write(f"{array_accomplished.astype(int).mean()*100}%")