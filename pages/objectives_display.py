import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'Objective display',
     page_icon = 'clipboard',
)
st.title('2024 SMS in 1 & DOA Objectives')
###########################################################################################################

try :
    obj_data = st.session_state.obj_data
except : 
    obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)

###########################################################################################################


obj_data.columns = ["Objective category","Source","#","Objective","KPI / Achievement criteria","Owners/ Applicability","Target date","Global Status","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"]
filtered = st.multiselect("Filter columns", options=list(obj_data.columns), default=['Objective','Global Status']) 
st.write(obj_data[filtered])


###########################################################################################################
st.page_link("pages/objective_modify_table.py", label = 'Update', icon = '🖊️')