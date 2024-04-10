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
obj_data['Nomination Letter'] = 0
obj_data['Nomination Letter'] = obj_data['Nomination Letter'].apply(lambda x : st.file_uploader(str(x))) 


st.write("objectives")
st.write(obj_data)
