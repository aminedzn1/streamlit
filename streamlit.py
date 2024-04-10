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



st.write("objectives")
st.write(obj_data)

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

custom_cat = ['aaa', 'bbb']

df["command_as_category"] = (
    df["command"].astype("category").cat.remove_categories(df['command']).cat.add_categories(custom_cat)
)

edited_df = st.experimental_data_editor(df)