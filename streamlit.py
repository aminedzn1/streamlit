import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'Home page',
     page_icon = '',
)
st.title('2024 SMS & DOA Objectives')
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
#obj_data = obj_data[:39]

# categories = ['Yes','No', 'N/A']

#obj_data["Global Status"] = (
#    obj_data["Global Status"].astype("category").cat.remove_categories(obj_data['Global Status']).cat.add_categories(categories)
#)

#filtered = st.multiselect("Filter columns", options=list(obj_data.columns), default=['Objective','Global Status']) [filtered]

