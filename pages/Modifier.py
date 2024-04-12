import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'Modifier',
     page_icon = 'lower_left_ballpoint_pen'
)
###########################################################################################################

try :
    obj_data = st.session_state.obj_data
except : 
    obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)

###########################################################################################################


if 'obj_data' not in st.session_state:
    st.session_state.obj_data = st.data_editor(obj_data)
    output_df = st.session_state.obj_data

else:
    output_df = st.data_editor(
        st.session_state.obj_data
        )

if st.button('Save') :
     output_df.to_csv(r"data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv", index = False)
     st.session_state.obj_data = output_df