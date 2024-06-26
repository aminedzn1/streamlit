import streamlit as st 
import pandas as pd 
import numpy as np

st.set_page_config(
     page_title = 'Objectives Measure',
     page_icon = 'bar_chart',
     layout = 'wide',
     initial_sidebar_state = 'collapsed'
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

###########################################################################################################

st.page_link('home.py', label = 'Home', icon = '🏠', use_container_width=True)
st.title('1 & DOA SMS Budget')
###########################################################################################################

data_budg = pd.read_csv(r'data/sms_budget_yoy.csv')
st.subheader('Global budget')
filt = st.multiselect("Filter columns", options = data_budg.columns, default = list(data_budg.columns) )

st.table(data_budg[filt])

data_func = pd.read_csv(r'data/sms_budget_f.csv')
st.subheader('Budget status per function/domain')
filt2 = st.multiselect("Filter columns", options = data_func.columns, default = list(data_func.columns) )

st.table(data_func[filt2])