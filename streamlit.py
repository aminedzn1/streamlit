import streamlit as st

st.set_page_config(
     page_title = 'Hello test',
     page_icon = '',
)
st.title('MAin page')

import pandas as pd
import numpy as np

obj_data = pd.read_csv(r'Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)
obj_data.columns = obj_data.iloc[0]
obj_data = obj_data.drop(0)
obj_data = obj_data[:39]

categories = ['Yes','No', 'N/A']
obj_data["Global Status"] = (
    obj_data["#"].astype("category").cat.remove_categories(obj_data['#']).cat.add_categories(categories)
)

st.write("objectives")
filtered = st.multiselect("Filter columns", options=list(obj_data.columns), default=['Objective','Global Status'])
edited_obj_data = st.experimental_data_editor(obj_data[filtered])

st.write(obj_data['Global Status'].iloc[0])

if 'obj_data' not in st.session_state:
    st.session_state['obj_data'] = obj_data