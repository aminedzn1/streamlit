import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'Casid display',
     page_icon = 'clipboard',
)
st.title('CASID Status')
###########################################################################################################

casid_data = pd.read_csv(r'data/CASID status - CASID Status .csv', dtype = 'string',keep_default_na=False)

###########################################################################################################



filtered = st.multiselect("Filter columns", options=list(casid_data.columns), default=['Supplier','CoC','Current status']) 
st.write(casid_data[filtered])


###########################################################################################################
