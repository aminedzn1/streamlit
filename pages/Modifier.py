import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'Modifier',
     page_icon = 'lower_left_ballpoint_pen'
)
###########################################################################################################
st.title('2024 SMS in 1 & DOA Objectives')
st.subheader('Edit objective table', divider = "red")
try :
    obj_data = st.session_state.obj_data
except : 
    obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)

obj_data.columns = ["Objective category","Source","#","Objective","KPI / Achievement criteria","Owners/ Applicability","Target date","Global Status","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"]

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