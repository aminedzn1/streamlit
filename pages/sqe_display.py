import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'SQE display',
     page_icon = 'clipboard',
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

###########################################################################################################
st.title('SQE Data')
###########################################################################################################

try :
    sqe_data = st.session_state.sqe_data
except : 
    sqe_data = pd.read_csv(r'data/SQE Follow-up - Sheet1.csv', dtype = 'string',keep_default_na=False)

###########################################################################################################


#sqe_data.columns = ["Domain/Function","SQE Holder","Date of signature","End of validity","Part of active network?","SQE Active?"]
filtered = st.multiselect("Filter columns", options=list(sqe_data.columns), default=['SQE Holder','SQE Active?']) 
st.table(sqe_data[filtered])


###########################################################################################################
