import streamlit as st

st.set_page_config(
     page_title = 'Hello test',
     page_icon = '',
)
st.title('MAin page')

import pandas as pd
import numpy as np

obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)
obj_data.columns = ["Objective category","Source","#","Objective","KPI / Achievement criteria","Owners/ Applicability","Target date","Global Status","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"]
obj_data = obj_data[:39]

categories = ['Yes','No', 'N/A']
obj_data["Global Status"] = (
    obj_data["Global Status"].astype("category").cat.remove_categories(obj_data['Global Status']).cat.add_categories(categories)
)

st.write("objectives")
#filtered = st.multiselect("Filter columns", options=list(obj_data.columns), default=['Objective','Global Status']) [filtered]

if 'obj_data' not in st.session_state:
    st.session_state.obj_data = st.data_editor(obj_data)
    output_df = st.session_state.obj_data

else:
    output_df = st.data_editor(
        st.session_state.obj_data
        )

if st.button('Save') :
     output_df.to_csv(r"data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv", index = False)

import glob
import os

cwd = os.getcwd()
st.write(cwd)

new_obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv')
st.write(new_obj_data)