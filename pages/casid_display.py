import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
     page_title = 'CASID Status',
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
st.title('1 & DOA CASID Status')
###########################################################################################################

casid_data = pd.read_csv(r'data/CASID status - CASID Status .csv', dtype = 'string',keep_default_na=False)

###########################################################################################################



filtered = st.multiselect("Filter columns", options=list(casid_data.columns), default=['Supplier','CoC','Current status']) 
st.write(casid_data[filtered])
 

