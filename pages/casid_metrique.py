import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import plotly.graph_objects as go

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
df =  casid_data.loc[casid_data['Current status'] in ['4. Internal Kick-off Meeting (KoM) performed',
                                                      '2. CASID introduced to the supplier']]

df = df[['CoC', 'Current status']]
df = df.replace({'4. Internal Kick-off Meeting (KoM) performed': 'Kick-off',
                 '2. CASID introduced to the supplier': 'Nomination'})

df = df.groupby(['CoC','Current status']).size()
st.write(df)
