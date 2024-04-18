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
 
col1, col2 = st.columns(2)
with col1 :
    st.write(casid_data['Current status'].value_counts())
with col2 :    
    domain = st.selectbox(label = 'Function / Domain', options = casid_data['CoC'].unique())
    try :     
        domain_casid_data = casid_data.loc[casid_data['CoC'] == domain]
        st.write(domain_casid_data['Current status'].value_counts())
    except :
        pass 
###########################################################################################################

st.session_state.casid_data = casid_data