import streamlit as st

st.set_page_config(
     page_title = 'Hello test',
     page_icon = '',
)
from st_pages import Page, show_pages, add_page_title

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("streamlit.py", "Home", "🏠"),
        Page("pages/modifier.py", "Page 2", ":lower_left_ballpoint_pen:"),
    ]
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
#filtered = st.multiselect("Filter columns", options=list(obj_data.columns), default=['Objective','Global Status']) [filtered]

if 'obj_data' not in st.session_state:
    st.session_state.obj_data = st.data_editor(obj_data)
    output_df = st.session_state.obj_data

else:
    output_df = st.data_editor(
        st.session_state.obj_data
        )

if st.button('Save') :
     output_df.to_csv("new_obj_data.csv", index = False)

import glob
import os

cwd = os.getcwd()
st.write(cwd)

new_obj_data = pd.read_csv(r'/mount/src/streamlit/new_obj_data.csv')
st.write(new_obj_data)