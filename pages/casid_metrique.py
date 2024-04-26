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
def trans(x): 
    try :
        return(int(x[0]))
    except :
        return(0)
casid_data['statusus'] = casid_data['Current status'].apply(lambda x : trans(x))

###########################################################################################################
df =  casid_data.loc[(casid_data['statusus'] >=2)]

df = df[['CoC', 'statusus']].reset_index()
df['Status'] = ''
for i in df.index :
    if df.iloc[i, 'statusus']>= 4 :
        df.iloc[i,'Status'] = 'Kick-off'
    elif df.iloc[i, 'statusus']>= 2 :
        df.iloc[i,'Status'] = 'Nomination'

df = df.groupby(['CoC','Status']).size().reset_index()
df.rename(columns = {'CoC':'Function/Domain', '0': 'Count'})
fig = px.bar(df, x = 'Function/Domain', y = 'Count', color = 'Status', barmode='group')
st.plotly_chart(fig)